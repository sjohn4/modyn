#include <cuda.h>
#include <cuda_fp16.h>
#include <cuda_runtime_api.h>
#include <device_launch_parameters.h>
#include <mma.h>
#include <cuda_fp16.hpp>

#include <fstream>
#include <iomanip>
#include <iostream>
#include <vector>

#include <ATen/cuda/CUDAContext.h>
#include <torch/extension.h>

#include "shared_utils.cuh"

using namespace nvcuda;

template <uint WARPS_PER_BLOCK,
          uint THREADBLOCK_SIZE,
          uint ROW_TILES_PER_STEP,
          uint COL_TILES_PER_STEP,
          uint WARP_SIZE,
          uint WARP_SIZE_LOG_2,
          uint TILE_DIM,
          uint TILE_DIM_LOG_2>
__launch_bounds__(THREADBLOCK_SIZE) __global__
    void dotBasedInteractBwdKernelNonAligned(const __half *__restrict input,
                                             const __half *__restrict upstream_grad,
                                             half __restrict *grad,
                                             half __restrict *bottom_mlp_grad,
                                             uint batch_size,
                                             uint num_rows,
                                             uint num_cols,
                                             uint num_rows_after_padding,
                                             uint num_cols_after_padding,
                                             uint sample_size,
                                             uint interaction_ugrad_size,
                                             uint interaction_ugrad_size_with_padding,
                                             uint interaction_ugrad_2D_size_elems,
                                             uint interaction_ugrad_2D_stride,
                                             uint input_size_elems,
                                             uint input_stride,
                                             uint num_row_steps,
                                             uint num_col_steps,
                                             uint row_tiles_per_step,
                                             uint shared_mem_per_warp_size_byte) {
  extern __shared__ half shared_mem[];
  uint warp_id = (threadIdx.x >> WARP_SIZE_LOG_2);
  uint sample_id = blockIdx.x * WARPS_PER_BLOCK + warp_id;
  if (sample_id >= batch_size) {
    return;
  }
  uint lane_id = threadIdx.x & (WARP_SIZE - 1);
  // ">> 1" to convert to half pointer
  uint smem_warp_offset = warp_id * (shared_mem_per_warp_size_byte >> 1);

  half *smem_in = &shared_mem[smem_warp_offset];
  half *smem_temp = &shared_mem[smem_warp_offset + input_size_elems];
  float *smem_out = reinterpret_cast<float *>(smem_temp);

  // Global memory pointers for the current sample
  // Input
  uint gmem_input_sample_offset = sample_id * sample_size;
  const half *gmem_input = &input[gmem_input_sample_offset];

  // Interaction Gradient
  const uint &gmem_grad_sample_offset = gmem_input_sample_offset;
  half *gmem_grad = &grad[gmem_grad_sample_offset];

  // Bottom MLP gradient
  half *gmem_mlp_grad = &bottom_mlp_grad[sample_id * num_cols];

  // Upstream gradient vector
  uint gmem_ugrad_sample_offset = sample_id * (num_cols + interaction_ugrad_size_with_padding);
  const half *gmem_ugrad = &upstream_grad[gmem_ugrad_sample_offset];

  // Upstream gradient vector for interactions
  const half *gmem_ugrad_interactions = &gmem_ugrad[num_cols];

  // upstream grad -> shared memory (place in input section temporarily)
#pragma unroll
  for (uint idx = lane_id; idx < interaction_ugrad_size; idx += WARP_SIZE) {
    smem_in[idx] = gmem_ugrad_interactions[idx];
  }
  __syncwarp();
  // Form the 2D ugrad matrix.
  if (lane_id < num_rows_after_padding) {
    uint ugrad_flat_index = ((lane_id * (lane_id - 1)) >> 1);
    uint ugrad_offset_1 = lane_id * interaction_ugrad_2D_stride;
    for (uint row = 0; row < num_rows; row++) {
      half ugrad_val = __float2half(0.0f);
      if (row < lane_id && lane_id < num_rows) {
        ugrad_val = smem_in[ugrad_flat_index + row];
        smem_temp[ugrad_offset_1 + row] = ugrad_val;
      }
      if (row <= lane_id && lane_id < num_rows_after_padding) {
        smem_temp[row * interaction_ugrad_2D_stride + lane_id] = ugrad_val;
      }
    }
    for (uint row = num_rows; row < num_rows_after_padding; row++) {
      smem_temp[row * interaction_ugrad_2D_stride + lane_id] = __float2half(0.0f);
    }
  }
  __syncwarp();

  // Input -> Shared Memory

  for (uint row = 0; row < num_rows; row++) {
    half *smem_row_ptr = &smem_in[row * input_stride];
    const half *gmem_row_ptr = &gmem_input[row * num_cols];
    for (uint idx = lane_id; idx < num_cols; idx += WARP_SIZE) {
      smem_row_ptr[idx] = gmem_row_ptr[idx];
    }
    uint idx = lane_id + num_cols;
    if (idx < num_cols_after_padding) {
      smem_row_ptr[idx] = __float2half(0);
    }
  }

#pragma unroll 2
  for (uint row = num_rows; row < num_rows_after_padding; row++) {
    half *smem_row_ptr = &smem_in[row * input_stride];
    for (uint idx = lane_id; idx < num_cols_after_padding; idx += WARP_SIZE) {
      smem_row_ptr[idx] = __float2half(0);
    }
  }
  __syncwarp();

  wmma::fragment<wmma::matrix_a, TILE_DIM, TILE_DIM, TILE_DIM, half, wmma::row_major> a[ROW_TILES_PER_STEP]
                                                                                       [ROW_TILES_PER_STEP];
  for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
    for (uint j = 0; j < ROW_TILES_PER_STEP; j++) {
      const half *tile_ptr = smem_temp + ((i * interaction_ugrad_2D_stride + j) << TILE_DIM_LOG_2);
      wmma::load_matrix_sync(a[i][j], tile_ptr, interaction_ugrad_2D_stride);
    }
  }

  wmma::fragment<wmma::accumulator, TILE_DIM, TILE_DIM, TILE_DIM, float> acc[ROW_TILES_PER_STEP];
  wmma::fragment<wmma::matrix_b, TILE_DIM, TILE_DIM, TILE_DIM, half, wmma::row_major> b[ROW_TILES_PER_STEP];
  for (int col_step = 0; col_step < num_col_steps; col_step++) {
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      const half *tile_ptr = smem_in + ((i * input_stride + col_step) << TILE_DIM_LOG_2);
      wmma::fill_fragment(acc[i], 0);
      wmma::load_matrix_sync(b[i], tile_ptr, input_stride);
    }
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      for (uint j = 0; j < ROW_TILES_PER_STEP; j++) {
        wmma::mma_sync(acc[i], a[i][j], b[j], acc[i]);
      }
    }
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      float *tile_ptr = smem_out + i * TILE_DIM * TILE_DIM;
      wmma::store_matrix_sync(tile_ptr, acc[i], TILE_DIM, wmma::mem_row_major);
    }
    __syncwarp();
    uint gmem_grad_col = (col_step << TILE_DIM_LOG_2) + lane_id;
    if (gmem_grad_col < num_cols) {
      for (uint i = 0; i < num_rows; i++) {
        gmem_grad[i * num_cols + gmem_grad_col] = __float2half(smem_out[(i << TILE_DIM_LOG_2) + lane_id]);
      }
    }
  }

  for (uint idx = lane_id; idx < num_cols; idx += WARP_SIZE) {
    gmem_mlp_grad[idx] = gmem_ugrad[idx];
  }
}


template <uint WARPS_PER_BLOCK,
          uint THREADBLOCK_SIZE,
          uint ROW_TILES_PER_STEP,
          uint COL_TILES_PER_STEP,
          uint WARP_SIZE,
          uint WARP_SIZE_LOG_2,
          uint TILE_DIM,
          uint TILE_DIM_LOG_2>
__launch_bounds__(THREADBLOCK_SIZE) __global__ void dotBasedInteractBwdKernel(const __half *__restrict input,
                                                                              const __half *__restrict upstream_grad,
                                                                              half __restrict *grad,
                                                                              half __restrict *bottom_mlp_grad,
                                                                              uint batch_size,
                                                                              uint num_rows,
                                                                              uint num_cols,
                                                                              uint num_rows_after_padding,
                                                                              uint num_cols_after_padding,
                                                                              uint sample_size,
                                                                              uint interaction_ugrad_size,
                                                                              uint interaction_ugrad_size_with_padding,
                                                                              uint interaction_ugrad_2D_size_elems,
                                                                              uint interaction_ugrad_2D_stride,
                                                                              uint input_size_elems,
                                                                              uint input_stride,
                                                                              uint num_row_steps,
                                                                              uint num_col_steps,
                                                                              uint row_tiles_per_step,
                                                                              uint shared_mem_per_warp_size_byte) {
  extern __shared__ half shared_mem[];
  uint warp_id = (threadIdx.x >> WARP_SIZE_LOG_2);
  uint sample_id = blockIdx.x * WARPS_PER_BLOCK + warp_id;
  if (sample_id >= batch_size) {
    return;
  }
  uint lane_id = threadIdx.x & (WARP_SIZE - 1);
  // ">> 1" to convert to half pointer
  uint smem_warp_offset = warp_id * (shared_mem_per_warp_size_byte >> 1);

  half *smem_in = &shared_mem[smem_warp_offset];
  half *smem_temp = &shared_mem[smem_warp_offset + input_size_elems];
  float *smem_out = reinterpret_cast<float *>(smem_temp);

  // Global memory pointers for the current sample
  // Input
  uint gmem_input_sample_offset = sample_id * sample_size;
  const half *gmem_input = &input[gmem_input_sample_offset];

  // Interaction Gradient
  const uint &gmem_grad_sample_offset = gmem_input_sample_offset;
  half *gmem_grad = &grad[gmem_grad_sample_offset];

  // Bottom MLP gradient
  half *gmem_mlp_grad = &bottom_mlp_grad[sample_id * num_cols];

  // Upstream gradient vector
  uint gmem_ugrad_sample_offset = sample_id * (num_cols + interaction_ugrad_size_with_padding);
  const half *gmem_ugrad = &upstream_grad[gmem_ugrad_sample_offset];

  // Upstream gradient vector for interactions
  const half *gmem_ugrad_interactions = &gmem_ugrad[num_cols];

  // upstream grad -> shared memory (place in input section temporarily)
#pragma unroll
  for (uint idx = lane_id; idx < (interaction_ugrad_size >> 3); idx += WARP_SIZE) {
    ((float4 *)smem_in)[idx] = ((float4 *)gmem_ugrad_interactions)[idx];
  }
  uint offset = (interaction_ugrad_size >> 3) << 3;
  for (uint idx = lane_id + offset; idx < interaction_ugrad_size; idx += WARP_SIZE) {
    smem_in[idx] = gmem_ugrad_interactions[idx];
  }
  __syncwarp();
  // Form the 2D ugrad matrix.
  if (lane_id < num_rows_after_padding) {
    uint ugrad_flat_index = ((lane_id * (lane_id - 1)) >> 1);
    uint ugrad_offset_1 = lane_id * interaction_ugrad_2D_stride;
    for (uint row = 0; row < num_rows; row++) {
      half ugrad_val = __float2half(0.0f);
      if (row < lane_id && lane_id < num_rows) {
        ugrad_val = smem_in[ugrad_flat_index + row];
        smem_temp[ugrad_offset_1 + row] = ugrad_val;
      }
      if (row <= lane_id && lane_id < num_rows_after_padding) {
        smem_temp[row * interaction_ugrad_2D_stride + lane_id] = ugrad_val;
      }
    }
    for (uint row = num_rows; row < num_rows_after_padding; row++) {
      smem_temp[row * interaction_ugrad_2D_stride + lane_id] = __float2half(0.0f);
    }
  }
  __syncwarp();

  // Input -> Shared Memory

  if (lane_id < (num_cols >> 2)) {
    for (uint row = 0; row < num_rows; row++) {
      half *smem_row_ptr = &smem_in[row * input_stride];
      const half *gmem_row_ptr = &gmem_input[row * num_cols];
      ((float2 *)smem_row_ptr)[lane_id] = ((float2 *)gmem_row_ptr)[lane_id];
    }
  }

  uint idx = lane_id + num_cols;
  if (idx < num_cols_after_padding) {
    for (uint row = 0; row < num_rows; row++) {
      half *smem_row_ptr = &smem_in[row * input_stride];
      smem_row_ptr[idx] = __float2half(0);
    }
  }

  half4 zeros;
  zeros.vals[0].x = __float2half(0);
  zeros.vals[0].y = __float2half(0);
  zeros.vals[1].x = __float2half(0);
  zeros.vals[1].y = __float2half(0);
  if (lane_id < (num_cols_after_padding >> 2)) {
#pragma unroll 2
    for (uint row = num_rows; row < num_rows_after_padding; row++) {
      half *smem_row_ptr = &smem_in[row * input_stride];
      ((half4 *)smem_row_ptr)[lane_id] = zeros;
    }
  }
  __syncwarp();

  wmma::fragment<wmma::matrix_a, TILE_DIM, TILE_DIM, TILE_DIM, half, wmma::row_major> a[ROW_TILES_PER_STEP]
                                                                                       [ROW_TILES_PER_STEP];
  for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
    for (uint j = 0; j < ROW_TILES_PER_STEP; j++) {
      const half *tile_ptr = smem_temp + ((i * interaction_ugrad_2D_stride + j) << TILE_DIM_LOG_2);
      wmma::load_matrix_sync(a[i][j], tile_ptr, interaction_ugrad_2D_stride);
    }
  }

  wmma::fragment<wmma::accumulator, TILE_DIM, TILE_DIM, TILE_DIM, float> acc[ROW_TILES_PER_STEP];
  wmma::fragment<wmma::matrix_b, TILE_DIM, TILE_DIM, TILE_DIM, half, wmma::row_major> b[ROW_TILES_PER_STEP];
  for (int col_step = 0; col_step < num_col_steps; col_step++) {
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      const half *tile_ptr = smem_in + ((i * input_stride + col_step) << TILE_DIM_LOG_2);
      wmma::fill_fragment(acc[i], 0);
      wmma::load_matrix_sync(b[i], tile_ptr, input_stride);
    }
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      for (uint j = 0; j < ROW_TILES_PER_STEP; j++) {
        wmma::mma_sync(acc[i], a[i][j], b[j], acc[i]);
      }
    }
    for (uint i = 0; i < ROW_TILES_PER_STEP; i++) {
      float *tile_ptr = smem_out + i * TILE_DIM * TILE_DIM;
      wmma::store_matrix_sync(tile_ptr, acc[i], TILE_DIM, wmma::mem_row_major);
    }
    __syncwarp();
    uint gmem_grad_col = (col_step << TILE_DIM_LOG_2) + lane_id;
    if (gmem_grad_col < num_cols) {
      for (uint i = 0; i < num_rows; i++) {
        gmem_grad[i * num_cols + gmem_grad_col] = __float2half(smem_out[(i << TILE_DIM_LOG_2) + lane_id]);
      }
    }
  }
  if (lane_id < (num_cols >> 2)) {
    ((float2 *)gmem_mlp_grad)[lane_id] = ((float2 *)gmem_ugrad)[lane_id];
  }
}


inline void dotBasedInteractBwd(void *input,
                                void *upstream_grad,
                                void *grad,
                                void *bottom_mlp_grad,
                                uint batch_size,
                                uint num_rows,
                                uint num_cols) {
  const uint kWarpSize = 32;
  const uint kWarpSizeLog2 = Log2<kWarpSize>::value;
  const uint kTileDim = 16;
  const uint kTileDimLog2 = Log2<kTileDim>::value;
  const uint mem_skew_size = 8;
  const uint kWarpsPerBlock = 4;
  const uint kWarpsPerBlockLog2 = Log2<kWarpsPerBlock>::value;
  const uint kNumThreads = kWarpsPerBlock * kWarpSize;
  const uint kRowTilesPerStep = 2;
  const uint kColTilesPerStep = 1;

  uint row_tiles_per_step = num_rows > kTileDim ? kRowTilesPerStep : 1;

  // num tiles
  uint num_row_tiles = (num_rows + kTileDim - 1) >> kTileDimLog2;
  uint num_col_tiles = (num_cols + kTileDim - 1) >> kTileDimLog2;

  // number of rows and columns after padding
  uint num_rows_after_padding = kTileDim << 1;
  uint num_cols_after_padding = num_col_tiles << kTileDimLog2;

  // 2D ugrad size and stride
  uint interaction_ugrad_2D_stride = num_rows_after_padding + mem_skew_size;
  uint interaction_ugrad_2D_size_elems = num_rows_after_padding * interaction_ugrad_2D_stride;
  uint interaction_ugrad_2D_size_bytes = interaction_ugrad_2D_size_elems * sizeof(half);

  // 1D ugrad size
  uint interaction_ugrad_size = num_rows * (num_rows - 1) >> 1;
  uint interaction_ugrad_size_with_padding = ((interaction_ugrad_size-1)/8 + 1)*8; //round up to multiple of 8

  // in_out place size and stride
  uint input_stride = num_cols_after_padding + mem_skew_size;
  uint input_size_elems = num_rows_after_padding * input_stride;
  uint input_size_bytes = input_size_elems * sizeof(half);

  // sample size
  uint sample_size = num_rows * num_cols;

  // output size
  uint output_size_elems = kTileDim * kTileDim * kRowTilesPerStep * kColTilesPerStep;
  uint output_size_bytes = output_size_elems * sizeof(float);

  // staging area size
  uint staging_area_size_bytes =
      output_size_bytes > interaction_ugrad_2D_size_bytes ? output_size_bytes : interaction_ugrad_2D_size_bytes;

  // Shared memory size
  uint shared_mem_per_warp_size_byte = input_size_bytes + staging_area_size_bytes;
  uint shared_mem_size_bytes = kWarpsPerBlock * shared_mem_per_warp_size_byte;

  uint num_blocks = (batch_size + kWarpsPerBlock - 1) >> kWarpsPerBlockLog2;
  uint num_row_steps = num_row_tiles / row_tiles_per_step;
  uint num_col_steps = num_col_tiles / kColTilesPerStep;

  bool float4_predicate = !((interaction_ugrad_size_with_padding & 7) || (num_cols & 7));
  if (float4_predicate) {
    dotBasedInteractBwdKernel<kWarpsPerBlock,
                              kNumThreads,
                              kRowTilesPerStep,
                              kColTilesPerStep,
                              kWarpSize,
                              kWarpSizeLog2,
                              kTileDim,
                              kTileDimLog2>
        <<<num_blocks, kNumThreads, shared_mem_size_bytes,
           at::cuda::getCurrentCUDAStream()>>>((const half *)input,
                                              (const half *)upstream_grad,
                                              (half *)grad,
                                              (half *)bottom_mlp_grad,
                                              batch_size,
                                              num_rows,
                                              num_cols,
                                              num_rows_after_padding,
                                              num_cols_after_padding,
                                              sample_size,
                                              interaction_ugrad_size,
                                              interaction_ugrad_size_with_padding,
                                              interaction_ugrad_2D_size_elems,
                                              interaction_ugrad_2D_stride,
                                              input_size_elems,
                                              input_stride,
                                              num_row_steps,
                                              num_col_steps,
                                              row_tiles_per_step,
                                              shared_mem_per_warp_size_byte);
  } else {
    dotBasedInteractBwdKernelNonAligned<kWarpsPerBlock,
                                        kNumThreads,
                                        kRowTilesPerStep,
                                        kColTilesPerStep,
                                        kWarpSize,
                                        kWarpSizeLog2,
                                        kTileDim,
                                        kTileDimLog2>
        <<<num_blocks, kNumThreads, shared_mem_size_bytes,
           at::cuda::getCurrentCUDAStream()>>>((const half *)input,
                                              (const half *)upstream_grad,
                                              (half *)grad,
                                              (half *)bottom_mlp_grad,
                                              batch_size,
                                              num_rows,
                                              num_cols,
                                              num_rows_after_padding,
                                              num_cols_after_padding,
                                              sample_size,
                                              interaction_ugrad_size,
                                              interaction_ugrad_size_with_padding,
                                              interaction_ugrad_2D_size_elems,
                                              interaction_ugrad_2D_stride,
                                              input_size_elems,
                                              input_stride,
                                              num_row_steps,
                                              num_col_steps,
                                              row_tiles_per_step,
                                              shared_mem_per_warp_size_byte);
  }
}
