# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
import common_pb2 as common__pb2
import integration_source_pb2 as integration__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='action.proto',
  package='calixa.domain.action',
  syntax='proto3',
  serialized_options=b'\n\027io.calixa.domain.action',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x61\x63tion.proto\x12\x14\x63\x61lixa.domain.action\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/protobuf/field_mask.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0c\x63ommon.proto\x1a\x18integration_source.proto\"R\n\x12\x43hargeRefundParams\x12,\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x1c.calixa.domain.common.Amount\x12\x0e\n\x06reason\x18\x02 \x01(\t\"Q\n\x1dSubscriptionTrialUpdateParams\x12\x30\n\x0ctrial_end_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"&\n\x11\x43ouponApplyParams\x12\x11\n\tcoupon_id\x18\x01 \x01(\t\"\xc4\x01\n\x17OpportunityCreateParams\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\tclosed_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x06\x61mount\x18\x03 \x01(\x0b\x32\x1c.calixa.domain.common.Amount\x12\x12\n\nstage_name\x18\x04 \x01(\t\x12\x10\n\x08owner_id\x18\x05 \x01(\t\x12\x18\n\x10opportunity_type\x18\x06 \x01(\t\"\x1c\n\rWebhookParams\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xb4\x03\n\x0c\x41\x63tionParams\x12H\n\x14\x63harge_refund_params\x18\x01 \x01(\x0b\x32(.calixa.domain.action.ChargeRefundParamsH\x00\x12_\n subscription_trial_update_params\x18\x64 \x01(\x0b\x32\x33.calixa.domain.action.SubscriptionTrialUpdateParamsH\x00\x12G\n\x13\x63oupon_apply_params\x18\xc8\x01 \x01(\x0b\x32\'.calixa.domain.action.CouponApplyParamsH\x00\x12S\n\x19opportunity_create_params\x18\xac\x02 \x01(\x0b\x32-.calixa.domain.action.OpportunityCreateParamsH\x00\x12>\n\x0ewebhook_params\x18\x90N \x01(\x0b\x32#.calixa.domain.action.WebhookParamsH\x00\x12\x11\n\x05\x66orce\x18\xff\xff\xff\xff\x01 \x01(\x08\x42\x08\n\x06params\"\xb9\x02\n\"ThirdPartyActionInvocationResponse\x12V\n\x07headers\x18\x01 \x03(\x0b\x32\x45.calixa.domain.action.ThirdPartyActionInvocationResponse.HeadersEntry\x12P\n\x04meta\x18\x02 \x03(\x0b\x32\x42.calixa.domain.action.ThirdPartyActionInvocationResponse.MetaEntry\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x80\x03\n\x0c\x41\x63tionConfig\x12\r\n\x05title\x18\x01 \x01(\t\x12<\n\x06source\x18\x02 \x01(\x0e\x32,.calixa.domain.integration.IntegrationSource\x12\x35\n\x0b\x65ntity_type\x18\x03 \x01(\x0e\x32 .calixa.domain.common.EntityType\x12$\n\x1c\x63reated_by_organization_user\x18\x04 \x01(\t\x12\x41\n\x15\x64\x65\x66\x61ult_action_params\x18\x05 \x01(\x0b\x32\".calixa.domain.action.ActionParams\x12\x37\n\x0c\x61\x63tion_state\x18\x06 \x01(\x0e\x32!.calixa.domain.action.ActionState\x12\x35\n\x0b\x61\x63tion_type\x18\x07 \x01(\x0e\x32 .calixa.domain.action.ActionType\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t*`\n\x0b\x41\x63tionState\x12\x1c\n\x18\x41\x43TION_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x43TION_STATE_ENABLED\x10\x01\x12\x19\n\x15\x41\x43TION_STATE_DISABLED\x10\x02*\x8d\x01\n\x16\x41\x63tionInvocationStatus\x12(\n$ACTION_INVOCATION_STATUS_UNSPECIFIED\x10\x00\x12$\n ACTION_INVOCATION_STATUS_SUCCESS\x10\x01\x12#\n\x1f\x41\x43TION_INVOCATION_STATUS_FAILED\x10\x02*\xd1\x01\n\nActionType\x12\x1b\n\x17\x41\x43TION_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x41\x43TION_TYPE_CHARGE_REFUND\x10\x01\x12)\n%ACTION_TYPE_SUBSCRIPTION_TRIAL_UPDATE\x10\x64\x12\x1d\n\x18\x41\x43TION_TYPE_COUPON_APPLY\x10\xc8\x01\x12#\n\x1e\x41\x43TION_TYPE_OPPORTUNITY_CREATE\x10\xac\x02\x12\x18\n\x13\x41\x43TION_TYPE_WEBHOOK\x10\x90NB\x19\n\x17io.calixa.domain.actionb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,integration__source__pb2.DESCRIPTOR,])

_ACTIONSTATE = _descriptor.EnumDescriptor(
  name='ActionState',
  full_name='calixa.domain.action.ActionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_STATE_ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_STATE_DISABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1782,
  serialized_end=1878,
)
_sym_db.RegisterEnumDescriptor(_ACTIONSTATE)

ActionState = enum_type_wrapper.EnumTypeWrapper(_ACTIONSTATE)
_ACTIONINVOCATIONSTATUS = _descriptor.EnumDescriptor(
  name='ActionInvocationStatus',
  full_name='calixa.domain.action.ActionInvocationStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_INVOCATION_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_INVOCATION_STATUS_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_INVOCATION_STATUS_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1881,
  serialized_end=2022,
)
_sym_db.RegisterEnumDescriptor(_ACTIONINVOCATIONSTATUS)

ActionInvocationStatus = enum_type_wrapper.EnumTypeWrapper(_ACTIONINVOCATIONSTATUS)
_ACTIONTYPE = _descriptor.EnumDescriptor(
  name='ActionType',
  full_name='calixa.domain.action.ActionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_CHARGE_REFUND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_SUBSCRIPTION_TRIAL_UPDATE', index=2, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_COUPON_APPLY', index=3, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_OPPORTUNITY_CREATE', index=4, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TYPE_WEBHOOK', index=5, number=10000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2025,
  serialized_end=2234,
)
_sym_db.RegisterEnumDescriptor(_ACTIONTYPE)

ActionType = enum_type_wrapper.EnumTypeWrapper(_ACTIONTYPE)
ACTION_STATE_UNSPECIFIED = 0
ACTION_STATE_ENABLED = 1
ACTION_STATE_DISABLED = 2
ACTION_INVOCATION_STATUS_UNSPECIFIED = 0
ACTION_INVOCATION_STATUS_SUCCESS = 1
ACTION_INVOCATION_STATUS_FAILED = 2
ACTION_TYPE_UNSPECIFIED = 0
ACTION_TYPE_CHARGE_REFUND = 1
ACTION_TYPE_SUBSCRIPTION_TRIAL_UPDATE = 100
ACTION_TYPE_COUPON_APPLY = 200
ACTION_TYPE_OPPORTUNITY_CREATE = 300
ACTION_TYPE_WEBHOOK = 10000



_CHARGEREFUNDPARAMS = _descriptor.Descriptor(
  name='ChargeRefundParams',
  full_name='calixa.domain.action.ChargeRefundParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='calixa.domain.action.ChargeRefundParams.amount', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reason', full_name='calixa.domain.action.ChargeRefundParams.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=204,
  serialized_end=286,
)


_SUBSCRIPTIONTRIALUPDATEPARAMS = _descriptor.Descriptor(
  name='SubscriptionTrialUpdateParams',
  full_name='calixa.domain.action.SubscriptionTrialUpdateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trial_end_at', full_name='calixa.domain.action.SubscriptionTrialUpdateParams.trial_end_at', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=288,
  serialized_end=369,
)


_COUPONAPPLYPARAMS = _descriptor.Descriptor(
  name='CouponApplyParams',
  full_name='calixa.domain.action.CouponApplyParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='coupon_id', full_name='calixa.domain.action.CouponApplyParams.coupon_id', index=0,
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
  serialized_start=371,
  serialized_end=409,
)


_OPPORTUNITYCREATEPARAMS = _descriptor.Descriptor(
  name='OpportunityCreateParams',
  full_name='calixa.domain.action.OpportunityCreateParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='calixa.domain.action.OpportunityCreateParams.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closed_at', full_name='calixa.domain.action.OpportunityCreateParams.closed_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='calixa.domain.action.OpportunityCreateParams.amount', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stage_name', full_name='calixa.domain.action.OpportunityCreateParams.stage_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_id', full_name='calixa.domain.action.OpportunityCreateParams.owner_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opportunity_type', full_name='calixa.domain.action.OpportunityCreateParams.opportunity_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=412,
  serialized_end=608,
)


_WEBHOOKPARAMS = _descriptor.Descriptor(
  name='WebhookParams',
  full_name='calixa.domain.action.WebhookParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='calixa.domain.action.WebhookParams.url', index=0,
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
  serialized_start=610,
  serialized_end=638,
)


_ACTIONPARAMS = _descriptor.Descriptor(
  name='ActionParams',
  full_name='calixa.domain.action.ActionParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='charge_refund_params', full_name='calixa.domain.action.ActionParams.charge_refund_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subscription_trial_update_params', full_name='calixa.domain.action.ActionParams.subscription_trial_update_params', index=1,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coupon_apply_params', full_name='calixa.domain.action.ActionParams.coupon_apply_params', index=2,
      number=200, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opportunity_create_params', full_name='calixa.domain.action.ActionParams.opportunity_create_params', index=3,
      number=300, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='webhook_params', full_name='calixa.domain.action.ActionParams.webhook_params', index=4,
      number=10000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force', full_name='calixa.domain.action.ActionParams.force', index=5,
      number=536870911, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
    _descriptor.OneofDescriptor(
      name='params', full_name='calixa.domain.action.ActionParams.params',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=641,
  serialized_end=1077,
)


_THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1302,
  serialized_end=1348,
)

_THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY = _descriptor.Descriptor(
  name='MetaEntry',
  full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.MetaEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.MetaEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.MetaEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1350,
  serialized_end=1393,
)

_THIRDPARTYACTIONINVOCATIONRESPONSE = _descriptor.Descriptor(
  name='ThirdPartyActionInvocationResponse',
  full_name='calixa.domain.action.ThirdPartyActionInvocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='headers', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.headers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.meta', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='calixa.domain.action.ThirdPartyActionInvocationResponse.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY, _THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1080,
  serialized_end=1393,
)


_ACTIONCONFIG = _descriptor.Descriptor(
  name='ActionConfig',
  full_name='calixa.domain.action.ActionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='calixa.domain.action.ActionConfig.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='calixa.domain.action.ActionConfig.source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_type', full_name='calixa.domain.action.ActionConfig.entity_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_by_organization_user', full_name='calixa.domain.action.ActionConfig.created_by_organization_user', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_action_params', full_name='calixa.domain.action.ActionConfig.default_action_params', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action_state', full_name='calixa.domain.action.ActionConfig.action_state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action_type', full_name='calixa.domain.action.ActionConfig.action_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='calixa.domain.action.ActionConfig.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=1396,
  serialized_end=1780,
)

_CHARGEREFUNDPARAMS.fields_by_name['amount'].message_type = common__pb2._AMOUNT
_SUBSCRIPTIONTRIALUPDATEPARAMS.fields_by_name['trial_end_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPPORTUNITYCREATEPARAMS.fields_by_name['closed_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPPORTUNITYCREATEPARAMS.fields_by_name['amount'].message_type = common__pb2._AMOUNT
_ACTIONPARAMS.fields_by_name['charge_refund_params'].message_type = _CHARGEREFUNDPARAMS
_ACTIONPARAMS.fields_by_name['subscription_trial_update_params'].message_type = _SUBSCRIPTIONTRIALUPDATEPARAMS
_ACTIONPARAMS.fields_by_name['coupon_apply_params'].message_type = _COUPONAPPLYPARAMS
_ACTIONPARAMS.fields_by_name['opportunity_create_params'].message_type = _OPPORTUNITYCREATEPARAMS
_ACTIONPARAMS.fields_by_name['webhook_params'].message_type = _WEBHOOKPARAMS
_ACTIONPARAMS.oneofs_by_name['params'].fields.append(
  _ACTIONPARAMS.fields_by_name['charge_refund_params'])
_ACTIONPARAMS.fields_by_name['charge_refund_params'].containing_oneof = _ACTIONPARAMS.oneofs_by_name['params']
_ACTIONPARAMS.oneofs_by_name['params'].fields.append(
  _ACTIONPARAMS.fields_by_name['subscription_trial_update_params'])
_ACTIONPARAMS.fields_by_name['subscription_trial_update_params'].containing_oneof = _ACTIONPARAMS.oneofs_by_name['params']
_ACTIONPARAMS.oneofs_by_name['params'].fields.append(
  _ACTIONPARAMS.fields_by_name['coupon_apply_params'])
_ACTIONPARAMS.fields_by_name['coupon_apply_params'].containing_oneof = _ACTIONPARAMS.oneofs_by_name['params']
_ACTIONPARAMS.oneofs_by_name['params'].fields.append(
  _ACTIONPARAMS.fields_by_name['opportunity_create_params'])
_ACTIONPARAMS.fields_by_name['opportunity_create_params'].containing_oneof = _ACTIONPARAMS.oneofs_by_name['params']
_ACTIONPARAMS.oneofs_by_name['params'].fields.append(
  _ACTIONPARAMS.fields_by_name['webhook_params'])
_ACTIONPARAMS.fields_by_name['webhook_params'].containing_oneof = _ACTIONPARAMS.oneofs_by_name['params']
_THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY.containing_type = _THIRDPARTYACTIONINVOCATIONRESPONSE
_THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY.containing_type = _THIRDPARTYACTIONINVOCATIONRESPONSE
_THIRDPARTYACTIONINVOCATIONRESPONSE.fields_by_name['headers'].message_type = _THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY
_THIRDPARTYACTIONINVOCATIONRESPONSE.fields_by_name['meta'].message_type = _THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY
_ACTIONCONFIG.fields_by_name['source'].enum_type = integration__source__pb2._INTEGRATIONSOURCE
_ACTIONCONFIG.fields_by_name['entity_type'].enum_type = common__pb2._ENTITYTYPE
_ACTIONCONFIG.fields_by_name['default_action_params'].message_type = _ACTIONPARAMS
_ACTIONCONFIG.fields_by_name['action_state'].enum_type = _ACTIONSTATE
_ACTIONCONFIG.fields_by_name['action_type'].enum_type = _ACTIONTYPE
DESCRIPTOR.message_types_by_name['ChargeRefundParams'] = _CHARGEREFUNDPARAMS
DESCRIPTOR.message_types_by_name['SubscriptionTrialUpdateParams'] = _SUBSCRIPTIONTRIALUPDATEPARAMS
DESCRIPTOR.message_types_by_name['CouponApplyParams'] = _COUPONAPPLYPARAMS
DESCRIPTOR.message_types_by_name['OpportunityCreateParams'] = _OPPORTUNITYCREATEPARAMS
DESCRIPTOR.message_types_by_name['WebhookParams'] = _WEBHOOKPARAMS
DESCRIPTOR.message_types_by_name['ActionParams'] = _ACTIONPARAMS
DESCRIPTOR.message_types_by_name['ThirdPartyActionInvocationResponse'] = _THIRDPARTYACTIONINVOCATIONRESPONSE
DESCRIPTOR.message_types_by_name['ActionConfig'] = _ACTIONCONFIG
DESCRIPTOR.enum_types_by_name['ActionState'] = _ACTIONSTATE
DESCRIPTOR.enum_types_by_name['ActionInvocationStatus'] = _ACTIONINVOCATIONSTATUS
DESCRIPTOR.enum_types_by_name['ActionType'] = _ACTIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChargeRefundParams = _reflection.GeneratedProtocolMessageType('ChargeRefundParams', (_message.Message,), {
  'DESCRIPTOR' : _CHARGEREFUNDPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.ChargeRefundParams)
  })
_sym_db.RegisterMessage(ChargeRefundParams)

SubscriptionTrialUpdateParams = _reflection.GeneratedProtocolMessageType('SubscriptionTrialUpdateParams', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONTRIALUPDATEPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.SubscriptionTrialUpdateParams)
  })
_sym_db.RegisterMessage(SubscriptionTrialUpdateParams)

CouponApplyParams = _reflection.GeneratedProtocolMessageType('CouponApplyParams', (_message.Message,), {
  'DESCRIPTOR' : _COUPONAPPLYPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.CouponApplyParams)
  })
_sym_db.RegisterMessage(CouponApplyParams)

OpportunityCreateParams = _reflection.GeneratedProtocolMessageType('OpportunityCreateParams', (_message.Message,), {
  'DESCRIPTOR' : _OPPORTUNITYCREATEPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.OpportunityCreateParams)
  })
_sym_db.RegisterMessage(OpportunityCreateParams)

WebhookParams = _reflection.GeneratedProtocolMessageType('WebhookParams', (_message.Message,), {
  'DESCRIPTOR' : _WEBHOOKPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.WebhookParams)
  })
_sym_db.RegisterMessage(WebhookParams)

ActionParams = _reflection.GeneratedProtocolMessageType('ActionParams', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONPARAMS,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.ActionParams)
  })
_sym_db.RegisterMessage(ActionParams)

ThirdPartyActionInvocationResponse = _reflection.GeneratedProtocolMessageType('ThirdPartyActionInvocationResponse', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY,
    '__module__' : 'action_pb2'
    # @@protoc_insertion_point(class_scope:calixa.domain.action.ThirdPartyActionInvocationResponse.HeadersEntry)
    })
  ,

  'MetaEntry' : _reflection.GeneratedProtocolMessageType('MetaEntry', (_message.Message,), {
    'DESCRIPTOR' : _THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY,
    '__module__' : 'action_pb2'
    # @@protoc_insertion_point(class_scope:calixa.domain.action.ThirdPartyActionInvocationResponse.MetaEntry)
    })
  ,
  'DESCRIPTOR' : _THIRDPARTYACTIONINVOCATIONRESPONSE,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.ThirdPartyActionInvocationResponse)
  })
_sym_db.RegisterMessage(ThirdPartyActionInvocationResponse)
_sym_db.RegisterMessage(ThirdPartyActionInvocationResponse.HeadersEntry)
_sym_db.RegisterMessage(ThirdPartyActionInvocationResponse.MetaEntry)

ActionConfig = _reflection.GeneratedProtocolMessageType('ActionConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONCONFIG,
  '__module__' : 'action_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.action.ActionConfig)
  })
_sym_db.RegisterMessage(ActionConfig)


DESCRIPTOR._options = None
_THIRDPARTYACTIONINVOCATIONRESPONSE_HEADERSENTRY._options = None
_THIRDPARTYACTIONINVOCATIONRESPONSE_METAENTRY._options = None
# @@protoc_insertion_point(module_scope)
