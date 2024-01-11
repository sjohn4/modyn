# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import modyn.model_storage.internal.grpc.generated.model_storage_pb2 as model__storage__pb2


class ModelStorageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterModel = channel.unary_unary(
            '/modyn.model_storage.ModelStorage/RegisterModel',
            request_serializer=model__storage__pb2.RegisterModelRequest.SerializeToString,
            response_deserializer=model__storage__pb2.RegisterModelResponse.FromString,
        )
        self.FetchModel = channel.unary_unary(
            '/modyn.model_storage.ModelStorage/FetchModel',
            request_serializer=model__storage__pb2.FetchModelRequest.SerializeToString,
            response_deserializer=model__storage__pb2.FetchModelResponse.FromString,
        )
        self.DeleteModel = channel.unary_unary(
            '/modyn.model_storage.ModelStorage/DeleteModel',
            request_serializer=model__storage__pb2.DeleteModelRequest.SerializeToString,
            response_deserializer=model__storage__pb2.DeleteModelResponse.FromString,
        )


class ModelStorageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'RegisterModel': grpc.unary_unary_rpc_method_handler(
            servicer.RegisterModel,
            request_deserializer=model__storage__pb2.RegisterModelRequest.FromString,
            response_serializer=model__storage__pb2.RegisterModelResponse.SerializeToString,
        ),
        'FetchModel': grpc.unary_unary_rpc_method_handler(
            servicer.FetchModel,
            request_deserializer=model__storage__pb2.FetchModelRequest.FromString,
            response_serializer=model__storage__pb2.FetchModelResponse.SerializeToString,
        ),
        'DeleteModel': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteModel,
            request_deserializer=model__storage__pb2.DeleteModelRequest.FromString,
            response_serializer=model__storage__pb2.DeleteModelResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'modyn.model_storage.ModelStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class ModelStorage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterModel(request,
                      target,
                      options=(),
                      channel_credentials=None,
                      call_credentials=None,
                      insecure=False,
                      compression=None,
                      wait_for_ready=None,
                      timeout=None,
                      metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modyn.model_storage.ModelStorage/RegisterModel',
                                             model__storage__pb2.RegisterModelRequest.SerializeToString,
                                             model__storage__pb2.RegisterModelResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchModel(request,
                   target,
                   options=(),
                   channel_credentials=None,
                   call_credentials=None,
                   insecure=False,
                   compression=None,
                   wait_for_ready=None,
                   timeout=None,
                   metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modyn.model_storage.ModelStorage/FetchModel',
                                             model__storage__pb2.FetchModelRequest.SerializeToString,
                                             model__storage__pb2.FetchModelResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteModel(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modyn.model_storage.ModelStorage/DeleteModel',
                                             model__storage__pb2.DeleteModelRequest.SerializeToString,
                                             model__storage__pb2.DeleteModelResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
