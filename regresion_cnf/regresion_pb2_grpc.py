# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from grpcbigbuffer import buffer_pb2 as buffer__pb2


class RegresionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamLogs = channel.stream_stream(
                '/Regresion/StreamLogs',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.MakeRegresion = channel.stream_stream(
                '/Regresion/MakeRegresion',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )


class RegresionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamLogs(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeRegresion(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegresionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamLogs': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamLogs,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'MakeRegresion': grpc.stream_stream_rpc_method_handler(
                    servicer.MakeRegresion,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Regresion', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Regresion(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamLogs(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Regresion/StreamLogs',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MakeRegresion(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Regresion/MakeRegresion',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
