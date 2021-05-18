# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datawarehouse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import integration_source_pb2 as integration__source__pb2
import common_pb2 as common__pb2
import entity_pb2 as entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='datawarehouse.proto',
  package='calixa.domain.warehouse',
  syntax='proto3',
  serialized_options=b'\n\036io.calixa.domain.datawarehouseH\001P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64\x61tawarehouse.proto\x12\x17\x63\x61lixa.domain.warehouse\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18integration_source.proto\x1a\x0c\x63ommon.proto\x1a\x0c\x65ntity.proto\"~\n\x13\x42igQueryCredentials\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x15\n\rdata_location\x18\x02 \x01(\t\x12 \n\x18\x64\x61ta_processing_location\x18\x03 \x01(\t\x12\x1a\n\x12service_account_id\x18\x04 \x01(\t\"\x16\n\x14SnowflakeCredentials\"\x15\n\x13RedshiftCredentials\"\xfd\x01\n\x0b\x43redentials\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12@\n\x08\x62igquery\x18\n \x01(\x0b\x32,.calixa.domain.warehouse.BigQueryCredentialsH\x00\x12\x42\n\tsnowflake\x18\x0b \x01(\x0b\x32-.calixa.domain.warehouse.SnowflakeCredentialsH\x00\x12@\n\x08redshift\x18\x0c \x01(\x0b\x32,.calixa.domain.warehouse.RedshiftCredentialsH\x00\x42\r\n\x0b\x63redentials\"{\n\x0b\x46ieldMapper\x12\x36\n\nfield_type\x18\x01 \x01(\x0e\x32\".calixa.domain.warehouse.FieldType\x12\x17\n\x0fsql_column_name\x18\x02 \x01(\t\x12\x1b\n\x13\x65ntity_field_number\x18\x03 \x01(\x05\"\xa0\x02\n\x0cQueryContext\x12\x17\n\x0forganization_id\x18\x01 \x01(\t\x12\r\n\x05query\x18\x02 \x01(\t\x12;\n\rfield_mappers\x18\x03 \x03(\x0b\x32$.calixa.domain.warehouse.FieldMapper\x12<\n\x12output_entity_type\x18\x04 \x01(\x0e\x32 .calixa.domain.common.EntityType\x12<\n\x06source\x18\x05 \x01(\x0e\x32,.calixa.domain.integration.IntegrationSource\x12/\n\x0blast_run_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x8e\x01\n\x13\x45xecuteQueryRequest\x12\x39\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32$.calixa.domain.warehouse.Credentials\x12<\n\rquery_context\x18\x02 \x01(\x0b\x32%.calixa.domain.warehouse.QueryContext\"a\n\x14\x45xecuteQueryResponse\x12\x17\n\x0f\x65ntitiesUpdated\x18\x01 \x01(\x05\x12\x17\n\x0f\x65ntitiesCreated\x18\x02 \x01(\x05\x12\x17\n\x0f\x65ntitiesDeleted\x18\x03 \x01(\x05\"U\n\x18VerifyCredentialsRequest\x12\x39\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32$.calixa.domain.warehouse.Credentials\"\x1b\n\x19VerifyCredentialsResponse*\xc2\x01\n\tFieldType\x12\x1a\n\x16\x46IELD_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x46IELD_TYPE_INTEGER\x10\x01\x12\x15\n\x11\x46IELD_TYPE_STRING\x10\x02\x12\x13\n\x0f\x46IELD_TYPE_ENUM\x10\x03\x12\x16\n\x12\x46IELD_TYPE_BOOLEAN\x10\x04\x12\x18\n\x14\x46IELD_TYPE_TIMESTAMP\x10\x05\x12#\n\x1e\x46IELD_TYPE_PRIMARY_EXTERNAL_ID\x10\xe8\x07\x32\xf0\x01\n\x14\x44\x61taWarehouseService\x12\\\n\x0c\x45xecuteQuery\x12,.calixa.domain.warehouse.ExecuteQueryRequest\x1a\x1c.calixa.domain.entity.Entity0\x01\x12z\n\x11VerifyCredentials\x12\x31.calixa.domain.warehouse.VerifyCredentialsRequest\x1a\x32.calixa.domain.warehouse.VerifyCredentialsResponseB$\n\x1eio.calixa.domain.datawarehouseH\x01P\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,integration__source__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,entity__pb2.DESCRIPTOR,])

_FIELDTYPE = _descriptor.EnumDescriptor(
  name='FieldType',
  full_name='calixa.domain.warehouse.FieldType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_INTEGER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_STRING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_ENUM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_BOOLEAN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_TIMESTAMP', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FIELD_TYPE_PRIMARY_EXTERNAL_ID', index=6, number=1000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1372,
  serialized_end=1566,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPE)

FieldType = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPE)
FIELD_TYPE_UNSPECIFIED = 0
FIELD_TYPE_INTEGER = 1
FIELD_TYPE_STRING = 2
FIELD_TYPE_ENUM = 3
FIELD_TYPE_BOOLEAN = 4
FIELD_TYPE_TIMESTAMP = 5
FIELD_TYPE_PRIMARY_EXTERNAL_ID = 1000



_BIGQUERYCREDENTIALS = _descriptor.Descriptor(
  name='BigQueryCredentials',
  full_name='calixa.domain.warehouse.BigQueryCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='calixa.domain.warehouse.BigQueryCredentials.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_location', full_name='calixa.domain.warehouse.BigQueryCredentials.data_location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_processing_location', full_name='calixa.domain.warehouse.BigQueryCredentials.data_processing_location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account_id', full_name='calixa.domain.warehouse.BigQueryCredentials.service_account_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=164,
  serialized_end=290,
)


_SNOWFLAKECREDENTIALS = _descriptor.Descriptor(
  name='SnowflakeCredentials',
  full_name='calixa.domain.warehouse.SnowflakeCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=292,
  serialized_end=314,
)


_REDSHIFTCREDENTIALS = _descriptor.Descriptor(
  name='RedshiftCredentials',
  full_name='calixa.domain.warehouse.RedshiftCredentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=316,
  serialized_end=337,
)


_CREDENTIALS = _descriptor.Descriptor(
  name='Credentials',
  full_name='calixa.domain.warehouse.Credentials',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='calixa.domain.warehouse.Credentials.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bigquery', full_name='calixa.domain.warehouse.Credentials.bigquery', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='snowflake', full_name='calixa.domain.warehouse.Credentials.snowflake', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redshift', full_name='calixa.domain.warehouse.Credentials.redshift', index=3,
      number=12, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='credentials', full_name='calixa.domain.warehouse.Credentials.credentials',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=340,
  serialized_end=593,
)


_FIELDMAPPER = _descriptor.Descriptor(
  name='FieldMapper',
  full_name='calixa.domain.warehouse.FieldMapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_type', full_name='calixa.domain.warehouse.FieldMapper.field_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql_column_name', full_name='calixa.domain.warehouse.FieldMapper.sql_column_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity_field_number', full_name='calixa.domain.warehouse.FieldMapper.entity_field_number', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=595,
  serialized_end=718,
)


_QUERYCONTEXT = _descriptor.Descriptor(
  name='QueryContext',
  full_name='calixa.domain.warehouse.QueryContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_id', full_name='calixa.domain.warehouse.QueryContext.organization_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='calixa.domain.warehouse.QueryContext.query', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mappers', full_name='calixa.domain.warehouse.QueryContext.field_mappers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_entity_type', full_name='calixa.domain.warehouse.QueryContext.output_entity_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='calixa.domain.warehouse.QueryContext.source', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_run_at', full_name='calixa.domain.warehouse.QueryContext.last_run_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=721,
  serialized_end=1009,
)


_EXECUTEQUERYREQUEST = _descriptor.Descriptor(
  name='ExecuteQueryRequest',
  full_name='calixa.domain.warehouse.ExecuteQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='credentials', full_name='calixa.domain.warehouse.ExecuteQueryRequest.credentials', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query_context', full_name='calixa.domain.warehouse.ExecuteQueryRequest.query_context', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1012,
  serialized_end=1154,
)


_EXECUTEQUERYRESPONSE = _descriptor.Descriptor(
  name='ExecuteQueryResponse',
  full_name='calixa.domain.warehouse.ExecuteQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entitiesUpdated', full_name='calixa.domain.warehouse.ExecuteQueryResponse.entitiesUpdated', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entitiesCreated', full_name='calixa.domain.warehouse.ExecuteQueryResponse.entitiesCreated', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entitiesDeleted', full_name='calixa.domain.warehouse.ExecuteQueryResponse.entitiesDeleted', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1156,
  serialized_end=1253,
)


_VERIFYCREDENTIALSREQUEST = _descriptor.Descriptor(
  name='VerifyCredentialsRequest',
  full_name='calixa.domain.warehouse.VerifyCredentialsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='credentials', full_name='calixa.domain.warehouse.VerifyCredentialsRequest.credentials', index=0,
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
  serialized_start=1255,
  serialized_end=1340,
)


_VERIFYCREDENTIALSRESPONSE = _descriptor.Descriptor(
  name='VerifyCredentialsResponse',
  full_name='calixa.domain.warehouse.VerifyCredentialsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1342,
  serialized_end=1369,
)

_CREDENTIALS.fields_by_name['bigquery'].message_type = _BIGQUERYCREDENTIALS
_CREDENTIALS.fields_by_name['snowflake'].message_type = _SNOWFLAKECREDENTIALS
_CREDENTIALS.fields_by_name['redshift'].message_type = _REDSHIFTCREDENTIALS
_CREDENTIALS.oneofs_by_name['credentials'].fields.append(
  _CREDENTIALS.fields_by_name['bigquery'])
_CREDENTIALS.fields_by_name['bigquery'].containing_oneof = _CREDENTIALS.oneofs_by_name['credentials']
_CREDENTIALS.oneofs_by_name['credentials'].fields.append(
  _CREDENTIALS.fields_by_name['snowflake'])
_CREDENTIALS.fields_by_name['snowflake'].containing_oneof = _CREDENTIALS.oneofs_by_name['credentials']
_CREDENTIALS.oneofs_by_name['credentials'].fields.append(
  _CREDENTIALS.fields_by_name['redshift'])
_CREDENTIALS.fields_by_name['redshift'].containing_oneof = _CREDENTIALS.oneofs_by_name['credentials']
_FIELDMAPPER.fields_by_name['field_type'].enum_type = _FIELDTYPE
_QUERYCONTEXT.fields_by_name['field_mappers'].message_type = _FIELDMAPPER
_QUERYCONTEXT.fields_by_name['output_entity_type'].enum_type = common__pb2._ENTITYTYPE
_QUERYCONTEXT.fields_by_name['source'].enum_type = integration__source__pb2._INTEGRATIONSOURCE
_QUERYCONTEXT.fields_by_name['last_run_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXECUTEQUERYREQUEST.fields_by_name['credentials'].message_type = _CREDENTIALS
_EXECUTEQUERYREQUEST.fields_by_name['query_context'].message_type = _QUERYCONTEXT
_VERIFYCREDENTIALSREQUEST.fields_by_name['credentials'].message_type = _CREDENTIALS
DESCRIPTOR.message_types_by_name['BigQueryCredentials'] = _BIGQUERYCREDENTIALS
DESCRIPTOR.message_types_by_name['SnowflakeCredentials'] = _SNOWFLAKECREDENTIALS
DESCRIPTOR.message_types_by_name['RedshiftCredentials'] = _REDSHIFTCREDENTIALS
DESCRIPTOR.message_types_by_name['Credentials'] = _CREDENTIALS
DESCRIPTOR.message_types_by_name['FieldMapper'] = _FIELDMAPPER
DESCRIPTOR.message_types_by_name['QueryContext'] = _QUERYCONTEXT
DESCRIPTOR.message_types_by_name['ExecuteQueryRequest'] = _EXECUTEQUERYREQUEST
DESCRIPTOR.message_types_by_name['ExecuteQueryResponse'] = _EXECUTEQUERYRESPONSE
DESCRIPTOR.message_types_by_name['VerifyCredentialsRequest'] = _VERIFYCREDENTIALSREQUEST
DESCRIPTOR.message_types_by_name['VerifyCredentialsResponse'] = _VERIFYCREDENTIALSRESPONSE
DESCRIPTOR.enum_types_by_name['FieldType'] = _FIELDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BigQueryCredentials = _reflection.GeneratedProtocolMessageType('BigQueryCredentials', (_message.Message,), {
  'DESCRIPTOR' : _BIGQUERYCREDENTIALS,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.BigQueryCredentials)
  })
_sym_db.RegisterMessage(BigQueryCredentials)

SnowflakeCredentials = _reflection.GeneratedProtocolMessageType('SnowflakeCredentials', (_message.Message,), {
  'DESCRIPTOR' : _SNOWFLAKECREDENTIALS,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.SnowflakeCredentials)
  })
_sym_db.RegisterMessage(SnowflakeCredentials)

RedshiftCredentials = _reflection.GeneratedProtocolMessageType('RedshiftCredentials', (_message.Message,), {
  'DESCRIPTOR' : _REDSHIFTCREDENTIALS,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.RedshiftCredentials)
  })
_sym_db.RegisterMessage(RedshiftCredentials)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

FieldMapper = _reflection.GeneratedProtocolMessageType('FieldMapper', (_message.Message,), {
  'DESCRIPTOR' : _FIELDMAPPER,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.FieldMapper)
  })
_sym_db.RegisterMessage(FieldMapper)

QueryContext = _reflection.GeneratedProtocolMessageType('QueryContext', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCONTEXT,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.QueryContext)
  })
_sym_db.RegisterMessage(QueryContext)

ExecuteQueryRequest = _reflection.GeneratedProtocolMessageType('ExecuteQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEQUERYREQUEST,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.ExecuteQueryRequest)
  })
_sym_db.RegisterMessage(ExecuteQueryRequest)

ExecuteQueryResponse = _reflection.GeneratedProtocolMessageType('ExecuteQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXECUTEQUERYRESPONSE,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.ExecuteQueryResponse)
  })
_sym_db.RegisterMessage(ExecuteQueryResponse)

VerifyCredentialsRequest = _reflection.GeneratedProtocolMessageType('VerifyCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYCREDENTIALSREQUEST,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.VerifyCredentialsRequest)
  })
_sym_db.RegisterMessage(VerifyCredentialsRequest)

VerifyCredentialsResponse = _reflection.GeneratedProtocolMessageType('VerifyCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYCREDENTIALSRESPONSE,
  '__module__' : 'datawarehouse_pb2'
  # @@protoc_insertion_point(class_scope:calixa.domain.warehouse.VerifyCredentialsResponse)
  })
_sym_db.RegisterMessage(VerifyCredentialsResponse)


DESCRIPTOR._options = None

_DATAWAREHOUSESERVICE = _descriptor.ServiceDescriptor(
  name='DataWarehouseService',
  full_name='calixa.domain.warehouse.DataWarehouseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1569,
  serialized_end=1809,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteQuery',
    full_name='calixa.domain.warehouse.DataWarehouseService.ExecuteQuery',
    index=0,
    containing_service=None,
    input_type=_EXECUTEQUERYREQUEST,
    output_type=entity__pb2._ENTITY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyCredentials',
    full_name='calixa.domain.warehouse.DataWarehouseService.VerifyCredentials',
    index=1,
    containing_service=None,
    input_type=_VERIFYCREDENTIALSREQUEST,
    output_type=_VERIFYCREDENTIALSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAWAREHOUSESERVICE)

DESCRIPTOR.services_by_name['DataWarehouseService'] = _DATAWAREHOUSESERVICE

# @@protoc_insertion_point(module_scope)
