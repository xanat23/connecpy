# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import haberdasher_pb2 as haberdasher__pb2


class HaberdasherStub(object):
    """A Haberdasher makes hats for clients.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MakeHat = channel.unary_unary(
                '/i2y.conpy.example.Haberdasher/MakeHat',
                request_serializer=haberdasher__pb2.Size.SerializeToString,
                response_deserializer=haberdasher__pb2.Hat.FromString,
                )


class HaberdasherServicer(object):
    """A Haberdasher makes hats for clients.
    """

    def MakeHat(self, request, context):
        """MakeHat produces a hat of mysterious, randomly-selected color!
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HaberdasherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MakeHat': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeHat,
                    request_deserializer=haberdasher__pb2.Size.FromString,
                    response_serializer=haberdasher__pb2.Hat.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'i2y.conpy.example.Haberdasher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Haberdasher(object):
    """A Haberdasher makes hats for clients.
    """

    @staticmethod
    def MakeHat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/i2y.conpy.example.Haberdasher/MakeHat',
            haberdasher__pb2.Size.SerializeToString,
            haberdasher__pb2.Hat.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)