# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/malos/v1/driver.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from admobilize.proto.malos.v1 import maloseye_pb2 as admobilize_dot_malos_dot_v1_dot_maloseye__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admobilize/malos/v1/driver.proto',
  package='admobilize.malos.v1.driver',
  syntax='proto3',
  serialized_options=b'\n\035com.admobilize.proto.malos.v1B\013DriverProtoP\001Z7bitbucket.org/admobilize/admobilizeapis-go/pkg/malos/v1\252\002\032AdMobilize.Malos.Driver.V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n admobilize/malos/v1/driver.proto\x12\x1a\x61\x64mobilize.malos.v1.driver\x1a\"admobilize/malos/v1/maloseye.proto\"\xa4\x01\n\x0c\x44riverConfig\x12\x1d\n\x15\x64\x65lay_between_updates\x18\x01 \x01(\x02\x12\x1f\n\x17timeout_after_last_ping\x18\x02 \x01(\x02\x12\x46\n\x10malos_eye_config\x18\x04 \x01(\x0b\x32,.admobilize.malos.v1.maloseye.MalosEyeConfig\x12\x0c\n\x04uuid\x18\x0e \x01(\t\"\xbc\x01\n\nDriverInfo\x12\x13\n\x0b\x64river_name\x18\x01 \x01(\t\x12\x11\n\tbase_port\x18\x02 \x01(\x05\x12\x18\n\x10provides_updates\x18\x03 \x01(\x08\x12\x1d\n\x15\x64\x65lay_between_updates\x18\x04 \x01(\x05\x12\x13\n\x0bneeds_pings\x18\x05 \x01(\x08\x12\x1f\n\x17timeout_after_last_ping\x18\x06 \x01(\x05\x12\x17\n\x0fnotes_for_human\x18\x07 \x01(\t\"G\n\x0fMalosDriverInfo\x12\x34\n\x04info\x18\x01 \x03(\x0b\x32&.admobilize.malos.v1.driver.DriverInfo\"\xf6\x02\n\x06Status\x12<\n\x04type\x18\x01 \x01(\x0e\x32..admobilize.malos.v1.driver.Status.MessageType\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x8e\x02\n\x0bMessageType\x12\x1c\n\x18MESSAGE_TYPE_NOT_DEFINED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\x0b\n\x07STOPPED\x10\x02\x12\x13\n\x0f\x43ONFIG_RECEIVED\x10\x03\x12\x14\n\x10\x43OMMAND_EXECUTED\x10\x04\x12\x13\n\x0fSTATUS_CRITICAL\x10\x05\x12\x10\n\x0cSTATUS_ERROR\x10\x06\x12\x12\n\x0eSTATUS_WARNING\x10\x07\x12\x0f\n\x0bSTATUS_INFO\x10\x08\x12\x10\n\x0cSTATUS_DEBUG\x10\t\x12\x14\n\x10\x43\x41MERA_CONNECTED\x10\n\x12\x17\n\x13\x43\x41MERA_DISCONNECTED\x10\x0b\x12\x0f\n\x0bVIDEO_READY\x10\x0c\x42\x84\x01\n\x1d\x63om.admobilize.proto.malos.v1B\x0b\x44riverProtoP\x01Z7bitbucket.org/admobilize/admobilizeapis-go/pkg/malos/v1\xaa\x02\x1a\x41\x64Mobilize.Malos.Driver.V1b\x06proto3'
  ,
  dependencies=[admobilize_dot_malos_dot_v1_dot_maloseye__pb2.DESCRIPTOR,])



_STATUS_MESSAGETYPE = _descriptor.EnumDescriptor(
  name='MessageType',
  full_name='admobilize.malos.v1.driver.Status.MessageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESSAGE_TYPE_NOT_DEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STOPPED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONFIG_RECEIVED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMAND_EXECUTED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_CRITICAL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_ERROR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_WARNING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_INFO', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS_DEBUG', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_CONNECTED', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_DISCONNECTED', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_READY', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=636,
  serialized_end=906,
)
_sym_db.RegisterEnumDescriptor(_STATUS_MESSAGETYPE)


_DRIVERCONFIG = _descriptor.Descriptor(
  name='DriverConfig',
  full_name='admobilize.malos.v1.driver.DriverConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='delay_between_updates', full_name='admobilize.malos.v1.driver.DriverConfig.delay_between_updates', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_after_last_ping', full_name='admobilize.malos.v1.driver.DriverConfig.timeout_after_last_ping', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='malos_eye_config', full_name='admobilize.malos.v1.driver.DriverConfig.malos_eye_config', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='admobilize.malos.v1.driver.DriverConfig.uuid', index=3,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_end=265,
)


_DRIVERINFO = _descriptor.Descriptor(
  name='DriverInfo',
  full_name='admobilize.malos.v1.driver.DriverInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_name', full_name='admobilize.malos.v1.driver.DriverInfo.driver_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_port', full_name='admobilize.malos.v1.driver.DriverInfo.base_port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provides_updates', full_name='admobilize.malos.v1.driver.DriverInfo.provides_updates', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay_between_updates', full_name='admobilize.malos.v1.driver.DriverInfo.delay_between_updates', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='needs_pings', full_name='admobilize.malos.v1.driver.DriverInfo.needs_pings', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timeout_after_last_ping', full_name='admobilize.malos.v1.driver.DriverInfo.timeout_after_last_ping', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes_for_human', full_name='admobilize.malos.v1.driver.DriverInfo.notes_for_human', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=268,
  serialized_end=456,
)


_MALOSDRIVERINFO = _descriptor.Descriptor(
  name='MalosDriverInfo',
  full_name='admobilize.malos.v1.driver.MalosDriverInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='admobilize.malos.v1.driver.MalosDriverInfo.info', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=458,
  serialized_end=529,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='admobilize.malos.v1.driver.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='admobilize.malos.v1.driver.Status.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='admobilize.malos.v1.driver.Status.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='admobilize.malos.v1.driver.Status.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATUS_MESSAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=906,
)

_DRIVERCONFIG.fields_by_name['malos_eye_config'].message_type = admobilize_dot_malos_dot_v1_dot_maloseye__pb2._MALOSEYECONFIG
_MALOSDRIVERINFO.fields_by_name['info'].message_type = _DRIVERINFO
_STATUS.fields_by_name['type'].enum_type = _STATUS_MESSAGETYPE
_STATUS_MESSAGETYPE.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['DriverConfig'] = _DRIVERCONFIG
DESCRIPTOR.message_types_by_name['DriverInfo'] = _DRIVERINFO
DESCRIPTOR.message_types_by_name['MalosDriverInfo'] = _MALOSDRIVERINFO
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DriverConfig = _reflection.GeneratedProtocolMessageType('DriverConfig', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERCONFIG,
  '__module__' : 'admobilize.malos.v1.driver_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.malos.v1.driver.DriverConfig)
  })
_sym_db.RegisterMessage(DriverConfig)

DriverInfo = _reflection.GeneratedProtocolMessageType('DriverInfo', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERINFO,
  '__module__' : 'admobilize.malos.v1.driver_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.malos.v1.driver.DriverInfo)
  })
_sym_db.RegisterMessage(DriverInfo)

MalosDriverInfo = _reflection.GeneratedProtocolMessageType('MalosDriverInfo', (_message.Message,), {
  'DESCRIPTOR' : _MALOSDRIVERINFO,
  '__module__' : 'admobilize.malos.v1.driver_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.malos.v1.driver.MalosDriverInfo)
  })
_sym_db.RegisterMessage(MalosDriverInfo)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'admobilize.malos.v1.driver_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.malos.v1.driver.Status)
  })
_sym_db.RegisterMessage(Status)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
