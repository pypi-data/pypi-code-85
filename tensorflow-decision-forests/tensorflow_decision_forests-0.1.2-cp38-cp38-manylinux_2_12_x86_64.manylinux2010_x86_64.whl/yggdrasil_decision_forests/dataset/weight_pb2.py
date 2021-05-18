# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yggdrasil_decision_forests/dataset/weight.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='yggdrasil_decision_forests/dataset/weight.proto',
  package='yggdrasil_decision_forests.dataset.proto',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n/yggdrasil_decision_forests/dataset/weight.proto\x12(yggdrasil_decision_forests.dataset.proto\"\xa5\x03\n\x10WeightDefinition\x12\x11\n\tattribute\x18\x01 \x01(\t\x12_\n\tnumerical\x18\x02 \x01(\x0b\x32J.yggdrasil_decision_forests.dataset.proto.WeightDefinition.NumericalWeightH\x00\x12\x63\n\x0b\x63\x61tegorical\x18\x03 \x01(\x0b\x32L.yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeightH\x00\x1a\x11\n\x0fNumericalWeight\x1a\x9c\x01\n\x11\x43\x61tegoricalWeight\x12`\n\x05items\x18\x01 \x03(\x0b\x32Q.yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.Item\x1a%\n\x04Item\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0e\n\x06weight\x18\x03 \x01(\x02\x42\x06\n\x04type\"\xdd\x02\n\x16LinkedWeightDefinition\x12\x15\n\rattribute_idx\x18\x01 \x01(\x05\x12\x65\n\tnumerical\x18\x02 \x01(\x0b\x32P.yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.NumericalWeightH\x00\x12i\n\x0b\x63\x61tegorical\x18\x03 \x01(\x0b\x32R.yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.CategoricalWeightH\x00\x1a\x11\n\x0fNumericalWeight\x1a?\n\x11\x43\x61tegoricalWeight\x12*\n\x1e\x63\x61tegorical_value_idx_2_weight\x18\x01 \x03(\x02\x42\x02\x10\x01\x42\x06\n\x04type')
)




_WEIGHTDEFINITION_NUMERICALWEIGHT = _descriptor.Descriptor(
  name='NumericalWeight',
  full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.NumericalWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=331,
  serialized_end=348,
)

_WEIGHTDEFINITION_CATEGORICALWEIGHT_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.Item.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.Item.weight', index=1,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=470,
  serialized_end=507,
)

_WEIGHTDEFINITION_CATEGORICALWEIGHT = _descriptor.Descriptor(
  name='CategoricalWeight',
  full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTDEFINITION_CATEGORICALWEIGHT_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=507,
)

_WEIGHTDEFINITION = _descriptor.Descriptor(
  name='WeightDefinition',
  full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.attribute', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numerical', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.numerical', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categorical', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.categorical', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_WEIGHTDEFINITION_NUMERICALWEIGHT, _WEIGHTDEFINITION_CATEGORICALWEIGHT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='yggdrasil_decision_forests.dataset.proto.WeightDefinition.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=94,
  serialized_end=515,
)


_LINKEDWEIGHTDEFINITION_NUMERICALWEIGHT = _descriptor.Descriptor(
  name='NumericalWeight',
  full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.NumericalWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=331,
  serialized_end=348,
)

_LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT = _descriptor.Descriptor(
  name='CategoricalWeight',
  full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.CategoricalWeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categorical_value_idx_2_weight', full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.CategoricalWeight.categorical_value_idx_2_weight', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=796,
  serialized_end=859,
)

_LINKEDWEIGHTDEFINITION = _descriptor.Descriptor(
  name='LinkedWeightDefinition',
  full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute_idx', full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.attribute_idx', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numerical', full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.numerical', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categorical', full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.categorical', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LINKEDWEIGHTDEFINITION_NUMERICALWEIGHT, _LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=518,
  serialized_end=867,
)

_WEIGHTDEFINITION_NUMERICALWEIGHT.containing_type = _WEIGHTDEFINITION
_WEIGHTDEFINITION_CATEGORICALWEIGHT_ITEM.containing_type = _WEIGHTDEFINITION_CATEGORICALWEIGHT
_WEIGHTDEFINITION_CATEGORICALWEIGHT.fields_by_name['items'].message_type = _WEIGHTDEFINITION_CATEGORICALWEIGHT_ITEM
_WEIGHTDEFINITION_CATEGORICALWEIGHT.containing_type = _WEIGHTDEFINITION
_WEIGHTDEFINITION.fields_by_name['numerical'].message_type = _WEIGHTDEFINITION_NUMERICALWEIGHT
_WEIGHTDEFINITION.fields_by_name['categorical'].message_type = _WEIGHTDEFINITION_CATEGORICALWEIGHT
_WEIGHTDEFINITION.oneofs_by_name['type'].fields.append(
  _WEIGHTDEFINITION.fields_by_name['numerical'])
_WEIGHTDEFINITION.fields_by_name['numerical'].containing_oneof = _WEIGHTDEFINITION.oneofs_by_name['type']
_WEIGHTDEFINITION.oneofs_by_name['type'].fields.append(
  _WEIGHTDEFINITION.fields_by_name['categorical'])
_WEIGHTDEFINITION.fields_by_name['categorical'].containing_oneof = _WEIGHTDEFINITION.oneofs_by_name['type']
_LINKEDWEIGHTDEFINITION_NUMERICALWEIGHT.containing_type = _LINKEDWEIGHTDEFINITION
_LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT.containing_type = _LINKEDWEIGHTDEFINITION
_LINKEDWEIGHTDEFINITION.fields_by_name['numerical'].message_type = _LINKEDWEIGHTDEFINITION_NUMERICALWEIGHT
_LINKEDWEIGHTDEFINITION.fields_by_name['categorical'].message_type = _LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT
_LINKEDWEIGHTDEFINITION.oneofs_by_name['type'].fields.append(
  _LINKEDWEIGHTDEFINITION.fields_by_name['numerical'])
_LINKEDWEIGHTDEFINITION.fields_by_name['numerical'].containing_oneof = _LINKEDWEIGHTDEFINITION.oneofs_by_name['type']
_LINKEDWEIGHTDEFINITION.oneofs_by_name['type'].fields.append(
  _LINKEDWEIGHTDEFINITION.fields_by_name['categorical'])
_LINKEDWEIGHTDEFINITION.fields_by_name['categorical'].containing_oneof = _LINKEDWEIGHTDEFINITION.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['WeightDefinition'] = _WEIGHTDEFINITION
DESCRIPTOR.message_types_by_name['LinkedWeightDefinition'] = _LINKEDWEIGHTDEFINITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeightDefinition = _reflection.GeneratedProtocolMessageType('WeightDefinition', (_message.Message,), {

  'NumericalWeight' : _reflection.GeneratedProtocolMessageType('NumericalWeight', (_message.Message,), {
    'DESCRIPTOR' : _WEIGHTDEFINITION_NUMERICALWEIGHT,
    '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.WeightDefinition.NumericalWeight)
    })
  ,

  'CategoricalWeight' : _reflection.GeneratedProtocolMessageType('CategoricalWeight', (_message.Message,), {

    'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
      'DESCRIPTOR' : _WEIGHTDEFINITION_CATEGORICALWEIGHT_ITEM,
      '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
      # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight.Item)
      })
    ,
    'DESCRIPTOR' : _WEIGHTDEFINITION_CATEGORICALWEIGHT,
    '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.WeightDefinition.CategoricalWeight)
    })
  ,
  'DESCRIPTOR' : _WEIGHTDEFINITION,
  '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.WeightDefinition)
  })
_sym_db.RegisterMessage(WeightDefinition)
_sym_db.RegisterMessage(WeightDefinition.NumericalWeight)
_sym_db.RegisterMessage(WeightDefinition.CategoricalWeight)
_sym_db.RegisterMessage(WeightDefinition.CategoricalWeight.Item)

LinkedWeightDefinition = _reflection.GeneratedProtocolMessageType('LinkedWeightDefinition', (_message.Message,), {

  'NumericalWeight' : _reflection.GeneratedProtocolMessageType('NumericalWeight', (_message.Message,), {
    'DESCRIPTOR' : _LINKEDWEIGHTDEFINITION_NUMERICALWEIGHT,
    '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.NumericalWeight)
    })
  ,

  'CategoricalWeight' : _reflection.GeneratedProtocolMessageType('CategoricalWeight', (_message.Message,), {
    'DESCRIPTOR' : _LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT,
    '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
    # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition.CategoricalWeight)
    })
  ,
  'DESCRIPTOR' : _LINKEDWEIGHTDEFINITION,
  '__module__' : 'yggdrasil_decision_forests.dataset.weight_pb2'
  # @@protoc_insertion_point(class_scope:yggdrasil_decision_forests.dataset.proto.LinkedWeightDefinition)
  })
_sym_db.RegisterMessage(LinkedWeightDefinition)
_sym_db.RegisterMessage(LinkedWeightDefinition.NumericalWeight)
_sym_db.RegisterMessage(LinkedWeightDefinition.CategoricalWeight)


_LINKEDWEIGHTDEFINITION_CATEGORICALWEIGHT.fields_by_name['categorical_value_idx_2_weight']._options = None
# @@protoc_insertion_point(module_scope)
