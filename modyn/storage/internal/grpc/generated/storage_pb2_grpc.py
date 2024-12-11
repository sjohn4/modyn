# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import modyn.storage.internal.grpc.generated.storage_pb2 as storage__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in storage_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_stream(
                '/modyn.storage.Storage/Get',
                request_serializer=storage__pb2.GetRequest.SerializeToString,
                response_deserializer=storage__pb2.GetResponse.FromString,
                _registered_method=True)
        self.GetNL = channel.unary_stream(
                '/modyn.storage.Storage/GetNL',
                request_serializer=storage__pb2.GetRequest.SerializeToString,
                response_deserializer=storage__pb2.GetResponseNoLabels.FromString,
                _registered_method=True)
        self.GetNewDataSince = channel.unary_stream(
                '/modyn.storage.Storage/GetNewDataSince',
                request_serializer=storage__pb2.GetNewDataSinceRequest.SerializeToString,
                response_deserializer=storage__pb2.GetNewDataSinceResponse.FromString,
                _registered_method=True)
        self.GetDataInInterval = channel.unary_stream(
                '/modyn.storage.Storage/GetDataInInterval',
                request_serializer=storage__pb2.GetDataInIntervalRequest.SerializeToString,
                response_deserializer=storage__pb2.GetDataInIntervalResponse.FromString,
                _registered_method=True)
        self.GetDataPerWorker = channel.unary_stream(
                '/modyn.storage.Storage/GetDataPerWorker',
                request_serializer=storage__pb2.GetDataPerWorkerRequest.SerializeToString,
                response_deserializer=storage__pb2.GetDataPerWorkerResponse.FromString,
                _registered_method=True)
        self.GetDatasetSize = channel.unary_unary(
                '/modyn.storage.Storage/GetDatasetSize',
                request_serializer=storage__pb2.GetDatasetSizeRequest.SerializeToString,
                response_deserializer=storage__pb2.GetDatasetSizeResponse.FromString,
                _registered_method=True)
        self.CheckAvailability = channel.unary_unary(
                '/modyn.storage.Storage/CheckAvailability',
                request_serializer=storage__pb2.DatasetAvailableRequest.SerializeToString,
                response_deserializer=storage__pb2.DatasetAvailableResponse.FromString,
                _registered_method=True)
        self.RegisterNewDataset = channel.unary_unary(
                '/modyn.storage.Storage/RegisterNewDataset',
                request_serializer=storage__pb2.RegisterNewDatasetRequest.SerializeToString,
                response_deserializer=storage__pb2.RegisterNewDatasetResponse.FromString,
                _registered_method=True)
        self.GetCurrentTimestamp = channel.unary_unary(
                '/modyn.storage.Storage/GetCurrentTimestamp',
                request_serializer=storage__pb2.GetCurrentTimestampRequest.SerializeToString,
                response_deserializer=storage__pb2.GetCurrentTimestampResponse.FromString,
                _registered_method=True)
        self.DeleteDataset = channel.unary_unary(
                '/modyn.storage.Storage/DeleteDataset',
                request_serializer=storage__pb2.DatasetAvailableRequest.SerializeToString,
                response_deserializer=storage__pb2.DeleteDatasetResponse.FromString,
                _registered_method=True)
        self.DeleteData = channel.unary_unary(
                '/modyn.storage.Storage/DeleteData',
                request_serializer=storage__pb2.DeleteDataRequest.SerializeToString,
                response_deserializer=storage__pb2.DeleteDataResponse.FromString,
                _registered_method=True)


class StorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNL(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNewDataSince(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataInInterval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDataPerWorker(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDatasetSize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAvailability(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterNewDataset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCurrentTimestamp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDataset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_stream_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=storage__pb2.GetRequest.FromString,
                    response_serializer=storage__pb2.GetResponse.SerializeToString,
            ),
            'GetNL': grpc.unary_stream_rpc_method_handler(
                    servicer.GetNL,
                    request_deserializer=storage__pb2.GetRequest.FromString,
                    response_serializer=storage__pb2.GetResponseNoLabels.SerializeToString,
            ),
            'GetNewDataSince': grpc.unary_stream_rpc_method_handler(
                    servicer.GetNewDataSince,
                    request_deserializer=storage__pb2.GetNewDataSinceRequest.FromString,
                    response_serializer=storage__pb2.GetNewDataSinceResponse.SerializeToString,
            ),
            'GetDataInInterval': grpc.unary_stream_rpc_method_handler(
                    servicer.GetDataInInterval,
                    request_deserializer=storage__pb2.GetDataInIntervalRequest.FromString,
                    response_serializer=storage__pb2.GetDataInIntervalResponse.SerializeToString,
            ),
            'GetDataPerWorker': grpc.unary_stream_rpc_method_handler(
                    servicer.GetDataPerWorker,
                    request_deserializer=storage__pb2.GetDataPerWorkerRequest.FromString,
                    response_serializer=storage__pb2.GetDataPerWorkerResponse.SerializeToString,
            ),
            'GetDatasetSize': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDatasetSize,
                    request_deserializer=storage__pb2.GetDatasetSizeRequest.FromString,
                    response_serializer=storage__pb2.GetDatasetSizeResponse.SerializeToString,
            ),
            'CheckAvailability': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAvailability,
                    request_deserializer=storage__pb2.DatasetAvailableRequest.FromString,
                    response_serializer=storage__pb2.DatasetAvailableResponse.SerializeToString,
            ),
            'RegisterNewDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterNewDataset,
                    request_deserializer=storage__pb2.RegisterNewDatasetRequest.FromString,
                    response_serializer=storage__pb2.RegisterNewDatasetResponse.SerializeToString,
            ),
            'GetCurrentTimestamp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCurrentTimestamp,
                    request_deserializer=storage__pb2.GetCurrentTimestampRequest.FromString,
                    response_serializer=storage__pb2.GetCurrentTimestampResponse.SerializeToString,
            ),
            'DeleteDataset': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDataset,
                    request_deserializer=storage__pb2.DatasetAvailableRequest.FromString,
                    response_serializer=storage__pb2.DeleteDatasetResponse.SerializeToString,
            ),
            'DeleteData': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteData,
                    request_deserializer=storage__pb2.DeleteDataRequest.FromString,
                    response_serializer=storage__pb2.DeleteDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'modyn.storage.Storage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('modyn.storage.Storage', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Storage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/modyn.storage.Storage/Get',
            storage__pb2.GetRequest.SerializeToString,
            storage__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/modyn.storage.Storage/GetNL',
            storage__pb2.GetRequest.SerializeToString,
            storage__pb2.GetResponseNoLabels.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNewDataSince(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/modyn.storage.Storage/GetNewDataSince',
            storage__pb2.GetNewDataSinceRequest.SerializeToString,
            storage__pb2.GetNewDataSinceResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDataInInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/modyn.storage.Storage/GetDataInInterval',
            storage__pb2.GetDataInIntervalRequest.SerializeToString,
            storage__pb2.GetDataInIntervalResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDataPerWorker(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/modyn.storage.Storage/GetDataPerWorker',
            storage__pb2.GetDataPerWorkerRequest.SerializeToString,
            storage__pb2.GetDataPerWorkerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetDatasetSize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/GetDatasetSize',
            storage__pb2.GetDatasetSizeRequest.SerializeToString,
            storage__pb2.GetDatasetSizeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CheckAvailability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/CheckAvailability',
            storage__pb2.DatasetAvailableRequest.SerializeToString,
            storage__pb2.DatasetAvailableResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterNewDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/RegisterNewDataset',
            storage__pb2.RegisterNewDatasetRequest.SerializeToString,
            storage__pb2.RegisterNewDatasetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetCurrentTimestamp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/GetCurrentTimestamp',
            storage__pb2.GetCurrentTimestampRequest.SerializeToString,
            storage__pb2.GetCurrentTimestampResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteDataset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/DeleteDataset',
            storage__pb2.DatasetAvailableRequest.SerializeToString,
            storage__pb2.DeleteDatasetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/modyn.storage.Storage/DeleteData',
            storage__pb2.DeleteDataRequest.SerializeToString,
            storage__pb2.DeleteDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
