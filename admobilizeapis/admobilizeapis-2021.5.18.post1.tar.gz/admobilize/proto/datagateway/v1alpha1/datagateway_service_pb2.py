# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admobilize/datagateway/v1alpha1/datagateway_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from admobilize.proto.common import entity_pb2 as admobilize_dot_common_dot_entity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admobilize/datagateway/v1alpha1/datagateway_service.proto',
  package='admobilize.datagateway.v1alpha1',
  syntax='proto3',
  serialized_options=b'\n#com.admobilize.datagateway.v1alpha1B\020DataGatewayProtoP\001ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/datagateway/v1alpha1\242\002\005ADMDG\252\002\037AdMobilize.DataGateway.V1Alpha1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9admobilize/datagateway/v1alpha1/datagateway_service.proto\x12\x1f\x61\x64mobilize.datagateway.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1e\x61\x64mobilize/common/entity.proto\"\xc6\x01\n\x03Job\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12;\n\x06status\x18\x02 \x01(\x0e\x32+.admobilize.datagateway.v1alpha1.Job.Status\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\x12\x16\n\x0estatus_message\x18\x04 \x01(\t\x12\x11\n\tself_link\x18\x05 \x01(\t\"7\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x08\n\x04\x44ONE\x10\x03\x12\t\n\x05\x45RROR\x10\x04\"\xdf\x01\n\x10\x43reateJobRequest\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x12\n\nproduct_id\x18\x04 \x01(\t\x12\x10\n\x08timezone\x18\x07 \x01(\t\x12\x12\n\nspeed_unit\x18\x08 \x01(\t\x12\x12\n\ndevice_ids\x18\x05 \x03(\t\x12\x0b\n\x03\x63ms\x18\x06 \x01(\t\"G\n\rGetJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12*\n\x06\x66ields\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"I\n\x14GetJobResultRequests\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"2\n\x14\x45xportResultsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\"j\n\x15GetDatapointsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x12\n\ndatapoints\x18\x04 \x01(\t\"K\n\x15\x45xportResultsResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x14\n\x0cjob_complete\x18\x02 \x01(\x08\x12\x0c\n\x04urls\x18\x03 \x03(\t2\xe0\x04\n\x12\x44\x61taGatewayService\x12|\n\tCreateJob\x12\x31.admobilize.datagateway.v1alpha1.CreateJobRequest\x1a$.admobilize.datagateway.v1alpha1.Job\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/v1alpha1/jobs\x12}\n\x06GetJob\x12..admobilize.datagateway.v1alpha1.GetJobRequest\x1a$.admobilize.datagateway.v1alpha1.Job\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1alpha1/{id=jobs/*}\x12\xa5\x01\n\rGetJobResults\x12\x35.admobilize.datagateway.v1alpha1.GetJobResultRequests\x1a\x36.admobilize.datagateway.v1alpha1.GetDatapointsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1alpha1/{id=jobs/*}/results\x12\xa4\x01\n\rExportResults\x12\x35.admobilize.datagateway.v1alpha1.ExportResultsRequest\x1a\x36.admobilize.datagateway.v1alpha1.ExportResultsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1alpha1/{id=jobs/*}/exportB\xa8\x01\n#com.admobilize.datagateway.v1alpha1B\x10\x44\x61taGatewayProtoP\x01ZCbitbucket.org/admobilize/admobilizeapis-go/pkg/datagateway/v1alpha1\xa2\x02\x05\x41\x44MDG\xaa\x02\x1f\x41\x64Mobilize.DataGateway.V1Alpha1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,admobilize_dot_common_dot_entity__pb2.DESCRIPTOR,])



_JOB_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='admobilize.datagateway.v1alpha1.Job.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=396,
  serialized_end=451,
)
_sym_db.RegisterEnumDescriptor(_JOB_STATUS)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='admobilize.datagateway.v1alpha1.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='admobilize.datagateway.v1alpha1.Job.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='admobilize.datagateway.v1alpha1.Job.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='admobilize.datagateway.v1alpha1.Job.detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='admobilize.datagateway.v1alpha1.Job.status_message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_link', full_name='admobilize.datagateway.v1alpha1.Job.self_link', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _JOB_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=451,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='admobilize.datagateway.v1alpha1.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.start_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.project_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.product_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.timezone', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed_unit', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.speed_unit', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_ids', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.device_ids', index=6,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cms', full_name='admobilize.datagateway.v1alpha1.CreateJobRequest.cms', index=7,
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
  serialized_start=454,
  serialized_end=677,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='admobilize.datagateway.v1alpha1.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.datagateway.v1alpha1.GetJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fields', full_name='admobilize.datagateway.v1alpha1.GetJobRequest.fields', index=1,
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
  serialized_start=679,
  serialized_end=750,
)


_GETJOBRESULTREQUESTS = _descriptor.Descriptor(
  name='GetJobResultRequests',
  full_name='admobilize.datagateway.v1alpha1.GetJobResultRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.datagateway.v1alpha1.GetJobResultRequests.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='admobilize.datagateway.v1alpha1.GetJobResultRequests.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='admobilize.datagateway.v1alpha1.GetJobResultRequests.page_token', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=825,
)


_EXPORTRESULTSREQUEST = _descriptor.Descriptor(
  name='ExportResultsRequest',
  full_name='admobilize.datagateway.v1alpha1.ExportResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='admobilize.datagateway.v1alpha1.ExportResultsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='admobilize.datagateway.v1alpha1.ExportResultsRequest.format', index=1,
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
  serialized_start=827,
  serialized_end=877,
)


_GETDATAPOINTSRESPONSE = _descriptor.Descriptor(
  name='GetDatapointsResponse',
  full_name='admobilize.datagateway.v1alpha1.GetDatapointsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='admobilize.datagateway.v1alpha1.GetDatapointsResponse.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_complete', full_name='admobilize.datagateway.v1alpha1.GetDatapointsResponse.job_complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='admobilize.datagateway.v1alpha1.GetDatapointsResponse.next_page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datapoints', full_name='admobilize.datagateway.v1alpha1.GetDatapointsResponse.datapoints', index=3,
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
  serialized_start=879,
  serialized_end=985,
)


_EXPORTRESULTSRESPONSE = _descriptor.Descriptor(
  name='ExportResultsResponse',
  full_name='admobilize.datagateway.v1alpha1.ExportResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='admobilize.datagateway.v1alpha1.ExportResultsResponse.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_complete', full_name='admobilize.datagateway.v1alpha1.ExportResultsResponse.job_complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='urls', full_name='admobilize.datagateway.v1alpha1.ExportResultsResponse.urls', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=987,
  serialized_end=1062,
)

_JOB.fields_by_name['status'].enum_type = _JOB_STATUS
_JOB_STATUS.containing_type = _JOB
_CREATEJOBREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CREATEJOBREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETJOBREQUEST.fields_by_name['fields'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobResultRequests'] = _GETJOBRESULTREQUESTS
DESCRIPTOR.message_types_by_name['ExportResultsRequest'] = _EXPORTRESULTSREQUEST
DESCRIPTOR.message_types_by_name['GetDatapointsResponse'] = _GETDATAPOINTSRESPONSE
DESCRIPTOR.message_types_by_name['ExportResultsResponse'] = _EXPORTRESULTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.Job)
  })
_sym_db.RegisterMessage(Job)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

GetJobResultRequests = _reflection.GeneratedProtocolMessageType('GetJobResultRequests', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBRESULTREQUESTS,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetJobResultRequests)
  })
_sym_db.RegisterMessage(GetJobResultRequests)

ExportResultsRequest = _reflection.GeneratedProtocolMessageType('ExportResultsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSREQUEST,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.ExportResultsRequest)
  })
_sym_db.RegisterMessage(ExportResultsRequest)

GetDatapointsResponse = _reflection.GeneratedProtocolMessageType('GetDatapointsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATAPOINTSRESPONSE,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.GetDatapointsResponse)
  })
_sym_db.RegisterMessage(GetDatapointsResponse)

ExportResultsResponse = _reflection.GeneratedProtocolMessageType('ExportResultsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTRESULTSRESPONSE,
  '__module__' : 'admobilize.datagateway.v1alpha1.datagateway_service_pb2'
  # @@protoc_insertion_point(class_scope:admobilize.datagateway.v1alpha1.ExportResultsResponse)
  })
_sym_db.RegisterMessage(ExportResultsResponse)


DESCRIPTOR._options = None

_DATAGATEWAYSERVICE = _descriptor.ServiceDescriptor(
  name='DataGatewayService',
  full_name='admobilize.datagateway.v1alpha1.DataGatewayService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1065,
  serialized_end=1673,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='admobilize.datagateway.v1alpha1.DataGatewayService.CreateJob',
    index=0,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=_JOB,
    serialized_options=b'\202\323\344\223\002\020\"\016/v1alpha1/jobs',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='admobilize.datagateway.v1alpha1.DataGatewayService.GetJob',
    index=1,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_JOB,
    serialized_options=b'\202\323\344\223\002\027\022\025/v1alpha1/{id=jobs/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetJobResults',
    full_name='admobilize.datagateway.v1alpha1.DataGatewayService.GetJobResults',
    index=2,
    containing_service=None,
    input_type=_GETJOBRESULTREQUESTS,
    output_type=_GETDATAPOINTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\022\035/v1alpha1/{id=jobs/*}/results',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExportResults',
    full_name='admobilize.datagateway.v1alpha1.DataGatewayService.ExportResults',
    index=3,
    containing_service=None,
    input_type=_EXPORTRESULTSREQUEST,
    output_type=_EXPORTRESULTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\036\022\034/v1alpha1/{id=jobs/*}/export',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATAGATEWAYSERVICE)

DESCRIPTOR.services_by_name['DataGatewayService'] = _DATAGATEWAYSERVICE

# @@protoc_insertion_point(module_scope)
