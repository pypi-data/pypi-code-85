# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: control_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='control_service.proto',
  package='escrow',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15\x63ontrol_service.proto\x12\x06\x65scrow\"W\n\x16GetPaymentsListRequest\x12\x13\n\x0bmpe_address\x18\x01 \x01(\t\x12\x15\n\rcurrent_block\x18\x02 \x01(\x04\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"O\n\x11StartClaimRequest\x12\x13\n\x0bmpe_address\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"c\n\x0cPaymentReply\x12\x12\n\nchannel_id\x18\x01 \x01(\x0c\x12\x15\n\rchannel_nonce\x18\x02 \x01(\x0c\x12\x15\n\rsigned_amount\x18\x03 \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0c\";\n\x11PaymentsListReply\x12&\n\x08payments\x18\x01 \x03(\x0b\x32\x14.escrow.PaymentReply2\xfc\x01\n\x16ProviderControlService\x12O\n\x10GetListUnclaimed\x12\x1e.escrow.GetPaymentsListRequest\x1a\x19.escrow.PaymentsListReply\"\x00\x12P\n\x11GetListInProgress\x12\x1e.escrow.GetPaymentsListRequest\x1a\x19.escrow.PaymentsListReply\"\x00\x12?\n\nStartClaim\x12\x19.escrow.StartClaimRequest\x1a\x14.escrow.PaymentReply\"\x00\x62\x06proto3')
)




_GETPAYMENTSLISTREQUEST = _descriptor.Descriptor(
  name='GetPaymentsListRequest',
  full_name='escrow.GetPaymentsListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mpe_address', full_name='escrow.GetPaymentsListRequest.mpe_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_block', full_name='escrow.GetPaymentsListRequest.current_block', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.GetPaymentsListRequest.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=120,
)


_STARTCLAIMREQUEST = _descriptor.Descriptor(
  name='StartClaimRequest',
  full_name='escrow.StartClaimRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mpe_address', full_name='escrow.StartClaimRequest.mpe_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='escrow.StartClaimRequest.channel_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.StartClaimRequest.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=122,
  serialized_end=201,
)


_PAYMENTREPLY = _descriptor.Descriptor(
  name='PaymentReply',
  full_name='escrow.PaymentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='escrow.PaymentReply.channel_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_nonce', full_name='escrow.PaymentReply.channel_nonce', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signed_amount', full_name='escrow.PaymentReply.signed_amount', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='escrow.PaymentReply.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=203,
  serialized_end=302,
)


_PAYMENTSLISTREPLY = _descriptor.Descriptor(
  name='PaymentsListReply',
  full_name='escrow.PaymentsListReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payments', full_name='escrow.PaymentsListReply.payments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=304,
  serialized_end=363,
)

_PAYMENTSLISTREPLY.fields_by_name['payments'].message_type = _PAYMENTREPLY
DESCRIPTOR.message_types_by_name['GetPaymentsListRequest'] = _GETPAYMENTSLISTREQUEST
DESCRIPTOR.message_types_by_name['StartClaimRequest'] = _STARTCLAIMREQUEST
DESCRIPTOR.message_types_by_name['PaymentReply'] = _PAYMENTREPLY
DESCRIPTOR.message_types_by_name['PaymentsListReply'] = _PAYMENTSLISTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPaymentsListRequest = _reflection.GeneratedProtocolMessageType('GetPaymentsListRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPAYMENTSLISTREQUEST,
  __module__ = 'control_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.GetPaymentsListRequest)
  ))
_sym_db.RegisterMessage(GetPaymentsListRequest)

StartClaimRequest = _reflection.GeneratedProtocolMessageType('StartClaimRequest', (_message.Message,), dict(
  DESCRIPTOR = _STARTCLAIMREQUEST,
  __module__ = 'control_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.StartClaimRequest)
  ))
_sym_db.RegisterMessage(StartClaimRequest)

PaymentReply = _reflection.GeneratedProtocolMessageType('PaymentReply', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTREPLY,
  __module__ = 'control_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.PaymentReply)
  ))
_sym_db.RegisterMessage(PaymentReply)

PaymentsListReply = _reflection.GeneratedProtocolMessageType('PaymentsListReply', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTSLISTREPLY,
  __module__ = 'control_service_pb2'
  # @@protoc_insertion_point(class_scope:escrow.PaymentsListReply)
  ))
_sym_db.RegisterMessage(PaymentsListReply)



_PROVIDERCONTROLSERVICE = _descriptor.ServiceDescriptor(
  name='ProviderControlService',
  full_name='escrow.ProviderControlService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=366,
  serialized_end=618,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetListUnclaimed',
    full_name='escrow.ProviderControlService.GetListUnclaimed',
    index=0,
    containing_service=None,
    input_type=_GETPAYMENTSLISTREQUEST,
    output_type=_PAYMENTSLISTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetListInProgress',
    full_name='escrow.ProviderControlService.GetListInProgress',
    index=1,
    containing_service=None,
    input_type=_GETPAYMENTSLISTREQUEST,
    output_type=_PAYMENTSLISTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartClaim',
    full_name='escrow.ProviderControlService.StartClaim',
    index=2,
    containing_service=None,
    input_type=_STARTCLAIMREQUEST,
    output_type=_PAYMENTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROVIDERCONTROLSERVICE)

DESCRIPTOR.services_by_name['ProviderControlService'] = _PROVIDERCONTROLSERVICE

# @@protoc_insertion_point(module_scope)
