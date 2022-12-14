# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import backend.odm.odm_pb2 as odm__pb2


class ODMStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetByKeys = channel.unary_unary(
            '/odm.ODM/GetByKeys',
            request_serializer=odm__pb2.GetByKeysRequest.SerializeToString,
            response_deserializer=odm__pb2.GetResponse.FromString,
        )
        self.GetByQuery = channel.unary_unary(
            '/odm.ODM/GetByQuery',
            request_serializer=odm__pb2.GetByQueryRequest.SerializeToString,
            response_deserializer=odm__pb2.GetResponse.FromString,
        )
        self.GetKeysByQuery = channel.unary_unary(
            '/odm.ODM/GetKeysByQuery',
            request_serializer=odm__pb2.GetByQueryRequest.SerializeToString,
            response_deserializer=odm__pb2.GetKeysResponse.FromString,
        )
        self.Set = channel.unary_unary(
            '/odm.ODM/Set',
            request_serializer=odm__pb2.SetRequest.SerializeToString,
            response_deserializer=odm__pb2.SetResponse.FromString,
        )
        self.DeleteTraining = channel.unary_unary(
            '/odm.ODM/DeleteTraining',
            request_serializer=odm__pb2.DeleteRequest.SerializeToString,
            response_deserializer=odm__pb2.DeleteResponse.FromString,
        )


class ODMServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetByKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetKeysByQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTraining(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ODMServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetByKeys': grpc.unary_unary_rpc_method_handler(
            servicer.GetByKeys,
            request_deserializer=odm__pb2.GetByKeysRequest.FromString,
            response_serializer=odm__pb2.GetResponse.SerializeToString,
        ),
        'GetByQuery': grpc.unary_unary_rpc_method_handler(
            servicer.GetByQuery,
            request_deserializer=odm__pb2.GetByQueryRequest.FromString,
            response_serializer=odm__pb2.GetResponse.SerializeToString,
        ),
        'GetKeysByQuery': grpc.unary_unary_rpc_method_handler(
            servicer.GetKeysByQuery,
            request_deserializer=odm__pb2.GetByQueryRequest.FromString,
            response_serializer=odm__pb2.GetKeysResponse.SerializeToString,
        ),
        'Set': grpc.unary_unary_rpc_method_handler(
            servicer.Set,
            request_deserializer=odm__pb2.SetRequest.FromString,
            response_serializer=odm__pb2.SetResponse.SerializeToString,
        ),
        'DeleteTraining': grpc.unary_unary_rpc_method_handler(
            servicer.DeleteTraining,
            request_deserializer=odm__pb2.DeleteRequest.FromString,
            response_serializer=odm__pb2.DeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'odm.ODM', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


class ODM(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetByKeys(request,
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
            '/odm.ODM/GetByKeys',
            odm__pb2.GetByKeysRequest.SerializeToString,
            odm__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def GetByQuery(request,
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
            '/odm.ODM/GetByQuery',
            odm__pb2.GetByQueryRequest.SerializeToString,
            odm__pb2.GetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def GetKeysByQuery(request,
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
            '/odm.ODM/GetKeysByQuery',
            odm__pb2.GetByQueryRequest.SerializeToString,
            odm__pb2.GetKeysResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def Set(request,
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
            '/odm.ODM/Set',
            odm__pb2.SetRequest.SerializeToString,
            odm__pb2.SetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)

    @staticmethod
    def DeleteTraining(request,
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
            '/odm.ODM/DeleteTraining',
            odm__pb2.DeleteRequest.SerializeToString,
            odm__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata)
