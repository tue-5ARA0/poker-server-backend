# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/game/game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/game/game.proto',
  package='game',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15proto/game/game.proto\x12\x04game\"\"\n\x11\x43reateGameRequest\x12\r\n\x05token\x18\x01 \x01(\t\" \n\x12\x43reateGameResponse\x12\n\n\x02id\x18\x01 \x01(\t\" \n\x0fListGameRequest\x12\r\n\x05token\x18\x01 \x01(\t\"$\n\x10ListGameResponse\x12\x10\n\x08game_ids\x18\x01 \x03(\t\"!\n\x0fPlayGameRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\"\"\n\x10PlayGameResponse\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t2\xd0\x01\n\x19GameCoordinatorController\x12=\n\x06\x43reate\x12\x17.game.CreateGameRequest\x1a\x18.game.CreateGameResponse\"\x00\x12\x37\n\x04List\x12\x15.game.ListGameRequest\x1a\x16.game.ListGameResponse\"\x00\x12;\n\x04Play\x12\x15.game.PlayGameRequest\x1a\x16.game.PlayGameResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_CREATEGAMEREQUEST = _descriptor.Descriptor(
  name='CreateGameRequest',
  full_name='game.CreateGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='game.CreateGameRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=65,
)


_CREATEGAMERESPONSE = _descriptor.Descriptor(
  name='CreateGameResponse',
  full_name='game.CreateGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='game.CreateGameResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=99,
)


_LISTGAMEREQUEST = _descriptor.Descriptor(
  name='ListGameRequest',
  full_name='game.ListGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='game.ListGameRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=133,
)


_LISTGAMERESPONSE = _descriptor.Descriptor(
  name='ListGameResponse',
  full_name='game.ListGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_ids', full_name='game.ListGameResponse.game_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=171,
)


_PLAYGAMEREQUEST = _descriptor.Descriptor(
  name='PlayGameRequest',
  full_name='game.PlayGameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='game.PlayGameRequest.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=206,
)


_PLAYGAMERESPONSE = _descriptor.Descriptor(
  name='PlayGameResponse',
  full_name='game.PlayGameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='game.PlayGameResponse.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=242,
)

DESCRIPTOR.message_types_by_name['CreateGameRequest'] = _CREATEGAMEREQUEST
DESCRIPTOR.message_types_by_name['CreateGameResponse'] = _CREATEGAMERESPONSE
DESCRIPTOR.message_types_by_name['ListGameRequest'] = _LISTGAMEREQUEST
DESCRIPTOR.message_types_by_name['ListGameResponse'] = _LISTGAMERESPONSE
DESCRIPTOR.message_types_by_name['PlayGameRequest'] = _PLAYGAMEREQUEST
DESCRIPTOR.message_types_by_name['PlayGameResponse'] = _PLAYGAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateGameRequest = _reflection.GeneratedProtocolMessageType('CreateGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGAMEREQUEST,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.CreateGameRequest)
  })
_sym_db.RegisterMessage(CreateGameRequest)

CreateGameResponse = _reflection.GeneratedProtocolMessageType('CreateGameResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGAMERESPONSE,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.CreateGameResponse)
  })
_sym_db.RegisterMessage(CreateGameResponse)

ListGameRequest = _reflection.GeneratedProtocolMessageType('ListGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTGAMEREQUEST,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.ListGameRequest)
  })
_sym_db.RegisterMessage(ListGameRequest)

ListGameResponse = _reflection.GeneratedProtocolMessageType('ListGameResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTGAMERESPONSE,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.ListGameResponse)
  })
_sym_db.RegisterMessage(ListGameResponse)

PlayGameRequest = _reflection.GeneratedProtocolMessageType('PlayGameRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYGAMEREQUEST,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.PlayGameRequest)
  })
_sym_db.RegisterMessage(PlayGameRequest)

PlayGameResponse = _reflection.GeneratedProtocolMessageType('PlayGameResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLAYGAMERESPONSE,
  '__module__' : 'proto.game.game_pb2'
  # @@protoc_insertion_point(class_scope:game.PlayGameResponse)
  })
_sym_db.RegisterMessage(PlayGameResponse)



_GAMECOORDINATORCONTROLLER = _descriptor.ServiceDescriptor(
  name='GameCoordinatorController',
  full_name='game.GameCoordinatorController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=245,
  serialized_end=453,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='game.GameCoordinatorController.Create',
    index=0,
    containing_service=None,
    input_type=_CREATEGAMEREQUEST,
    output_type=_CREATEGAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='game.GameCoordinatorController.List',
    index=1,
    containing_service=None,
    input_type=_LISTGAMEREQUEST,
    output_type=_LISTGAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Play',
    full_name='game.GameCoordinatorController.Play',
    index=2,
    containing_service=None,
    input_type=_PLAYGAMEREQUEST,
    output_type=_PLAYGAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMECOORDINATORCONTROLLER)

DESCRIPTOR.services_by_name['GameCoordinatorController'] = _GAMECOORDINATORCONTROLLER

# @@protoc_insertion_point(module_scope)
