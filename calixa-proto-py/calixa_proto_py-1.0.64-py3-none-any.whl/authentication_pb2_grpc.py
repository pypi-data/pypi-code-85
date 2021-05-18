# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import authentication_pb2 as authentication__pb2


class AuthenticationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuthenticateUser = channel.unary_unary(
                '/calixa.domain.authentication.AuthenticationService/AuthenticateUser',
                request_serializer=authentication__pb2.AuthenticateUserRequest.SerializeToString,
                response_deserializer=authentication__pb2.AuthenticateUserResponse.FromString,
                )
        self.GetFirebaseUser = channel.unary_unary(
                '/calixa.domain.authentication.AuthenticationService/GetFirebaseUser',
                request_serializer=authentication__pb2.GetFirebaseUserRequest.SerializeToString,
                response_deserializer=authentication__pb2.FirebaseUser.FromString,
                )


class AuthenticationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AuthenticateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFirebaseUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthenticationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuthenticateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateUser,
                    request_deserializer=authentication__pb2.AuthenticateUserRequest.FromString,
                    response_serializer=authentication__pb2.AuthenticateUserResponse.SerializeToString,
            ),
            'GetFirebaseUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFirebaseUser,
                    request_deserializer=authentication__pb2.GetFirebaseUserRequest.FromString,
                    response_serializer=authentication__pb2.FirebaseUser.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calixa.domain.authentication.AuthenticationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthenticationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AuthenticateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calixa.domain.authentication.AuthenticationService/AuthenticateUser',
            authentication__pb2.AuthenticateUserRequest.SerializeToString,
            authentication__pb2.AuthenticateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFirebaseUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calixa.domain.authentication.AuthenticationService/GetFirebaseUser',
            authentication__pb2.GetFirebaseUserRequest.SerializeToString,
            authentication__pb2.FirebaseUser.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
