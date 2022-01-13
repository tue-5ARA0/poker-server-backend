# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto.game import game_pb2 as proto_dot_game_dot_game__pb2


class GameCoordinatorControllerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/game.GameCoordinatorController/Create',
        request_serializer=proto_dot_game_dot_game__pb2.CreateGameRequest.SerializeToString,
        response_deserializer=proto_dot_game_dot_game__pb2.CreateGameResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/game.GameCoordinatorController/List',
        request_serializer=proto_dot_game_dot_game__pb2.ListGameRequest.SerializeToString,
        response_deserializer=proto_dot_game_dot_game__pb2.ListGameResponse.FromString,
        )
    self.Play = channel.stream_stream(
        '/game.GameCoordinatorController/Play',
        request_serializer=proto_dot_game_dot_game__pb2.PlayGameRequest.SerializeToString,
        response_deserializer=proto_dot_game_dot_game__pb2.PlayGameResponse.FromString,
        )


class GameCoordinatorControllerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Play(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GameCoordinatorControllerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=proto_dot_game_dot_game__pb2.CreateGameRequest.FromString,
          response_serializer=proto_dot_game_dot_game__pb2.CreateGameResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=proto_dot_game_dot_game__pb2.ListGameRequest.FromString,
          response_serializer=proto_dot_game_dot_game__pb2.ListGameResponse.SerializeToString,
      ),
      'Play': grpc.stream_stream_rpc_method_handler(
          servicer.Play,
          request_deserializer=proto_dot_game_dot_game__pb2.PlayGameRequest.FromString,
          response_serializer=proto_dot_game_dot_game__pb2.PlayGameResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'game.GameCoordinatorController', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
