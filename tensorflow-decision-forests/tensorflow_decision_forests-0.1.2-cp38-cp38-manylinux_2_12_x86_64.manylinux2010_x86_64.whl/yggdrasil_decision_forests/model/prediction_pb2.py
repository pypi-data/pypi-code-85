# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yggdrasil_decision_forests/model/prediction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yggdrasil_decision_forests.utils import distribution_pb2 as yggdrasil__decision__forests_dot_utils_dot_distribution__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yggdrasil_decision_forests/model/prediction.proto',
  package='yggdrasil_decision_forests.model.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n1yggdrasil_decision_forests/model/prediction.proto\x12&yggdrasil_decision_forests.model.proto\x1a\x33yggdrasil_decision_forests/utils/distribution.proto\"\xee\x04\n\nPrediction\x12[\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32\x41.yggdrasil_decision_forests.model.proto.Prediction.ClassificationH\x00\x12S\n\nregression\x18\x02 \x01(\x0b\x32=.yggdrasil_decision_forests.model.proto.Prediction.RegressionH\x00\x12M\n\x07ranking\x18\x05 \x01(\x0b\x32:.yggdrasil_decision_forests.model.proto.Prediction.RankingH\x00\x12\x11\n\x06weight\x18\x03 \x01(\x02:\x01\x31\x12\x13\n\x0b\x65xample_key\x18\x04 \x01(\t\x1a\x8d\x01\n\x0e\x43lassification\x12\r\n\x05value\x18\x01 \x01(\x05\x12V\n\x0c\x64istribution\x18\x02 \x01(\x0b\x32@.yggdrasil_decision_forests.utils.proto.IntegerDistributionFloat\x12\x14\n\x0cground_truth\x18\x03 \x01(\x05\x1a\x31\n\nRegression\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x14\n\x0cground_truth\x18\x02 \x01(\x02\x1al\n\x07Ranking\x12\x11\n\trelevance\x18\x01 \x01(\x02\x12\x1e\n\x16ground_truth_relevance\x18\x02 \x01(\x02\x12\x1c\n\x10\x64\x65precated_group\x18\x03 \x01(\x05\x42\x02\x18\x01\x12\x10\n\x08group_id\x18\x04 \x01(\x04\x42\x06\n\x04type')
  ,
  dependencies=[yggdrasil__decision__forests_dot_utils_dot_distribution__pb2.DESCRIPTOR,])




_PREDICTION_CLASSIFICATION = _descriptor.Descriptor(
  name='Classification',
  full_name='yggdrasil_decision_forests.model.proto.Prediction.Classification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='yggdrasil_decision_forests.model.proto.Prediction.Classification.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribution', full_name='yggdrasil_decision_forests.model.proto.Prediction.Classification.distribution', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ground_truth', full_name='yggdrasil_decision_forests.model.proto.Prediction.Classification.ground_truth', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=600,
)

_PREDICTION_REGRESSION = _descriptor.Descriptor(
  name='Regression',
  full_name='yggdrasil_decision_forests.model.proto.Prediction.Regression',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='yggdrasil_decision_forests.model.proto.Prediction.Regression.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ground_truth', full_name='yggdrasil_decision_forests.model.proto.Prediction.Regression.ground_truth', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=651,
)

_PREDICTION_RANKING = _descriptor.Descriptor(
  name='Ranking',
  full_name='yggdrasil_decision_forests.model.proto.Prediction.Ranking',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relevance', full_name='yggdrasil_decision_forests.model.proto.Prediction.Ranking.relevance', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ground_truth_relevance', full_name='yggdrasil_decision_forests.model.proto.Prediction.Ranking.ground_truth_relevance', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deprecated_group', full_name='yggdrasil_decision_forests.model.proto.Prediction.Ranking.deprecated_group', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='yggdrasil_decision_forests.model.proto.Prediction.Ranking.group_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=653,
  serialized_end=761,
)

_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='yggdrasil_decision_forests.model.proto.Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='yggdrasil_decision_forests.model.proto.Prediction.classification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regression', full_name='yggdrasil_decision_forests.model.proto.Prediction.regression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranking', full_name='yggdrasil_decision_forests.model.proto.Prediction.ranking', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='yggdrasil_decision_forests.model.proto.Prediction.weight', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_key', full_name='yggdrasil_decision_forests.model.proto.Prediction.example_key', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTION_CLASSIFICATION, _PREDICTION_REGRESSION, _PREDICTION_RANKING, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='yggdrasil_decision_forests.model.proto.Prediction.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=147,
  serialized_end=769,
)

_PREDICTION_CLASSIFICATION.fields_by_name['distribution'].message_type = yggdrasil__decision__forests_dot_utils_dot_distribution__pb2._INTEGERDISTRIBUTIONFLOAT
_PREDICTION_CLASSIFICATION.containing_type = _PREDICTION
_PREDICTION_REGRESSION.containing_type = _PREDICTION
_PREDICTION_RANKING.containing_type = _PREDICTION
_PREDICTION.fields_by_name['classification'].message_type = _PREDICTION_CLASSIFICATION
_PREDICTION.fields_by_name['regression'].message_type = _PREDICTION_REGRESSION
_PREDICTION.fields_by_name['ranking'].message_type = _PREDICTION_RANKING
_PREDICTION.oneofs_by_name['type'].fields.append(
  _PREDICTION.fields_by_name['classification'])
_PREDICTION.fields_by_name['classification'].containing_oneof = _PREDICTION.oneofs_by_name['type']
_PREDICTION.oneofs_by_name['type'].fields.append(
  _PREDICTION.fields_by_name['regression'])
_PREDICTION.fields_by_name['regression'].containing_oneof = _PREDICTION.oneofs_by_name['type']
_PREDICTION.oneofs_by_name['type'].fields.append(
  _PREDICTION.fields_by_name['ranking'])
_PREDICTION.fields_by_name['ranking'].containing_oneof = _PREDICTION.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), {

  'Classification' : _reflection.GeneratedProtocolMessageType('Classification', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_CLASSIFICATION,
    '__module__' : 'yggdrasil_decision_forests.model.prediction_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.model.proto.Prediction.Classification)
    })
  ,

  'Regression' : _reflection.GeneratedProtocolMessageType('Regression', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_REGRESSION,
    '__module__' : 'yggdrasil_decision_forests.model.prediction_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.model.proto.Prediction.Regression)
    })
  ,

  'Ranking' : _reflection.GeneratedProtocolMessageType('Ranking', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTION_RANKING,
    '__module__' : 'yggdrasil_decision_forests.model.prediction_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.model.proto.Prediction.Ranking)
    })
  ,
  'DESCRIPTOR' : _PREDICTION,
  '__module__' : 'yggdrasil_decision_forests.model.prediction_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.model.proto.Prediction)
  })
_sym_db.RegisterMessage(Prediction)
_sym_db.RegisterMessage(Prediction.Classification)
_sym_db.RegisterMessage(Prediction.Regression)
_sym_db.RegisterMessage(Prediction.Ranking)


_PREDICTION_RANKING.fields_by_name['deprecated_group']._options = None
# @@protoc_insertion_point(module_scope)
