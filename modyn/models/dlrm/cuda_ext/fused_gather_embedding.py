# Copyright (c) 2021 NVIDIA CORPORATION. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa
# mypy: ignore-errors
"""Fused Buckle Embedding."""

import apex
from torch.autograd import Function


class BuckleEmbeddingFusedGatherFunction(Function):
    """Customized embedding gather."""

    @staticmethod
    def forward(ctx, embedding, indices, offsets, amp_train):
        from modyn.models.dlrm.cuda_ext import fused_embedding

        output = fused_embedding.gather_gpu_fused_fwd(embedding, indices, offsets, amp_train)
        ctx.save_for_backward(embedding, indices, offsets)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        from modyn.models.dlrm.cuda_ext import fused_embedding

        embedding, indices, offsets = ctx.saved_tensors

        grad_weights = fused_embedding.gather_gpu_fused_bwd(embedding, indices, offsets, grad_output)
        return grad_weights, None, None, None


buckle_embedding_fused_gather = apex.amp.float_function(BuckleEmbeddingFusedGatherFunction.apply)
