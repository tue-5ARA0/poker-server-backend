# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from game import game_pb2 as game_dot_game__pb2

GRPC_GENERATED_VERSION = '1.66.1'
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
        + f' but the generated code in game/game_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GameCoordinatorControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Rename = channel.unary_unary(
                '/game.GameCoordinatorController/Rename',
                request_serializer=game_dot_game__pb2.PlayerRenameRequest.SerializeToString,
                response_deserializer=game_dot_game__pb2.PlayerRenameResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/game.GameCoordinatorController/Create',
                request_serializer=game_dot_game__pb2.CreateGameRequest.SerializeToString,
                response_deserializer=game_dot_game__pb2.CreateGameResponse.FromString,
                _registered_method=True)
        self.Play = channel.stream_stream(
                '/game.GameCoordinatorController/Play',
                request_serializer=game_dot_game__pb2.PlayGameRequest.SerializeToString,
                response_deserializer=game_dot_game__pb2.PlayGameResponse.FromString,
                _registered_method=True)
        self.Tournament = channel.unary_unary(
                '/game.GameCoordinatorController/Tournament',
                request_serializer=game_dot_game__pb2.TournamentRequest.SerializeToString,
                response_deserializer=game_dot_game__pb2.TournamentResponse.FromString,
                _registered_method=True)


class GameCoordinatorControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Rename(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Play(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Tournament(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GameCoordinatorControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Rename': grpc.unary_unary_rpc_method_handler(
                    servicer.Rename,
                    request_deserializer=game_dot_game__pb2.PlayerRenameRequest.FromString,
                    response_serializer=game_dot_game__pb2.PlayerRenameResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=game_dot_game__pb2.CreateGameRequest.FromString,
                    response_serializer=game_dot_game__pb2.CreateGameResponse.SerializeToString,
            ),
            'Play': grpc.stream_stream_rpc_method_handler(
                    servicer.Play,
                    request_deserializer=game_dot_game__pb2.PlayGameRequest.FromString,
                    response_serializer=game_dot_game__pb2.PlayGameResponse.SerializeToString,
            ),
            'Tournament': grpc.unary_unary_rpc_method_handler(
                    servicer.Tournament,
                    request_deserializer=game_dot_game__pb2.TournamentRequest.FromString,
                    response_serializer=game_dot_game__pb2.TournamentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'game.GameCoordinatorController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('game.GameCoordinatorController', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GameCoordinatorController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Rename(request,
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
            '/game.GameCoordinatorController/Rename',
            game_dot_game__pb2.PlayerRenameRequest.SerializeToString,
            game_dot_game__pb2.PlayerRenameResponse.FromString,
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
    def Create(request,
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
            '/game.GameCoordinatorController/Create',
            game_dot_game__pb2.CreateGameRequest.SerializeToString,
            game_dot_game__pb2.CreateGameResponse.FromString,
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
    def Play(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/game.GameCoordinatorController/Play',
            game_dot_game__pb2.PlayGameRequest.SerializeToString,
            game_dot_game__pb2.PlayGameResponse.FromString,
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
    def Tournament(request,
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
            '/game.GameCoordinatorController/Tournament',
            game_dot_game__pb2.TournamentRequest.SerializeToString,
            game_dot_game__pb2.TournamentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
