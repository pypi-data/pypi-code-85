# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='state_service.proto',
  package='escrow',
  syntax='proto3',
  serialized_options=_b('\n\037io.singularitynet.daemon.escrow'),
  serialized_pb=_b('\n\x13state_service.proto\x12\x06\x65scrow\"S\n\x13\x43hannelStateRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x15\n\rcurrent_block\x18\x03 \x01(\x04\"\xa2\x01\n\x11\x43hannelStateReply\x12\x15\n\rcurrent_nonce\x18\x01 \x01(\x0c\x12\x1d\n\x15\x63urrent_signed_amount\x18\x02 \x01(\x0c\x12\x19\n\x11\x63urrent_signature\x18\x03 \x01(\x0c\x12\x1f\n\x17old_nonce_signed_amount\x18\x04 \x01(\x0c\x12\x1b\n\x13old_nonce_signature\x18\x05 \x01(\x0c\"\x8f\x01\n\x14\x46reeCallStateRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1b\n\x13token_for_free_call\x18\x02 \x01(\x0c\x12\x1f\n\x17token_expiry_date_block\x18\x03 \x01(\x04\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x15\n\rcurrent_block\x18\x05 \x01(\x04\"C\n\x12\x46reeCallStateReply\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1c\n\x14\x66ree_calls_available\x18\x02 \x01(\x04\x32i\n\x1aPaymentChannelStateService\x12K\n\x0fGetChannelState\x12\x1b.escrow.ChannelStateRequest\x1a\x19.escrow.ChannelStateReply\"\x00\x32k\n\x14\x46reeCallStateService\x12S\n\x15GetFreeCallsAvailable\x12\x1c.escrow.FreeCallStateRequest\x1a\x1a.escrow.FreeCallStateReply\"\x00\x42!\n\x1fio.singularitynet.daemon.escrowb\x06proto3')
)




_CHANNELSTATEREQUEST = _descriptor.Descriptor(
  name='ChannelStateRequest',
  full_name='escrow.ChannelStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='escrow.ChannelStateRequest.channel_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.ChannelStateRequest.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_block', full_name='escrow.ChannelStateRequest.current_block', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=114,
)


_CHANNELSTATEREPLY = _descriptor.Descriptor(
  name='ChannelStateReply',
  full_name='escrow.ChannelStateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_nonce', full_name='escrow.ChannelStateReply.current_nonce', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_signed_amount', full_name='escrow.ChannelStateReply.current_signed_amount', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_signature', full_name='escrow.ChannelStateReply.current_signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='old_nonce_signed_amount', full_name='escrow.ChannelStateReply.old_nonce_signed_amount', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='old_nonce_signature', full_name='escrow.ChannelStateReply.old_nonce_signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=117,
  serialized_end=279,
)


_FREECALLSTATEREQUEST = _descriptor.Descriptor(
  name='FreeCallStateRequest',
  full_name='escrow.FreeCallStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='escrow.FreeCallStateRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_for_free_call', full_name='escrow.FreeCallStateRequest.token_for_free_call', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_expiry_date_block', full_name='escrow.FreeCallStateRequest.token_expiry_date_block', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.FreeCallStateRequest.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_block', full_name='escrow.FreeCallStateRequest.current_block', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=282,
  serialized_end=425,
)


_FREECALLSTATEREPLY = _descriptor.Descriptor(
  name='FreeCallStateReply',
  full_name='escrow.FreeCallStateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='escrow.FreeCallStateReply.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_calls_available', full_name='escrow.FreeCallStateReply.free_calls_available', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=427,
  serialized_end=494,
)

DESCRIPTOR.message_types_by_name['ChannelStateRequest'] = _CHANNELSTATEREQUEST
DESCRIPTOR.message_types_by_name['ChannelStateReply'] = _CHANNELSTATEREPLY
DESCRIPTOR.message_types_by_name['FreeCallStateRequest'] = _FREECALLSTATEREQUEST
DESCRIPTOR.message_types_by_name['FreeCallStateReply'] = _FREECALLSTATEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelStateRequest = _reflection.GeneratedProtocolMessageType('ChannelStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSTATEREQUEST,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.ChannelStateRequest)
  ))
_sym_db.RegisterMessage(ChannelStateRequest)

ChannelStateReply = _reflection.GeneratedProtocolMessageType('ChannelStateReply', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELSTATEREPLY,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.ChannelStateReply)
  ))
_sym_db.RegisterMessage(ChannelStateReply)

FreeCallStateRequest = _reflection.GeneratedProtocolMessageType('FreeCallStateRequest', (_message.Message,), dict(
  DESCRIPTOR = _FREECALLSTATEREQUEST,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.FreeCallStateRequest)
  ))
_sym_db.RegisterMessage(FreeCallStateRequest)

FreeCallStateReply = _reflection.GeneratedProtocolMessageType('FreeCallStateReply', (_message.Message,), dict(
  DESCRIPTOR = _FREECALLSTATEREPLY,
  __module__ = 'state_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.FreeCallStateReply)
  ))
_sym_db.RegisterMessage(FreeCallStateReply)


DESCRIPTOR._options = None

_PAYMENTCHANNELSTATESERVICE = _descriptor.ServiceDescriptor(
  name='PaymentChannelStateService',
  full_name='escrow.PaymentChannelStateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=496,
  serialized_end=601,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetChannelState',
    full_name='escrow.PaymentChannelStateService.GetChannelState',
    index=0,
    containing_service=None,
    input_type=_CHANNELSTATEREQUEST,
    output_type=_CHANNELSTATEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYMENTCHANNELSTATESERVICE)

DESCRIPTOR.services_by_name['PaymentChannelStateService'] = _PAYMENTCHANNELSTATESERVICE


_FREECALLSTATESERVICE = _descriptor.ServiceDescriptor(
  name='FreeCallStateService',
  full_name='escrow.FreeCallStateService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=603,
  serialized_end=710,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFreeCallsAvailable',
    full_name='escrow.FreeCallStateService.GetFreeCallsAvailable',
    index=0,
    containing_service=None,
    input_type=_FREECALLSTATEREQUEST,
    output_type=_FREECALLSTATEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FREECALLSTATESERVICE)

DESCRIPTOR.services_by_name['FreeCallStateService'] = _FREECALLSTATESERVICE

# @@protoc_insertion_point(module_scope)
