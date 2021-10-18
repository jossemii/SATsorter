# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import onnx_pb2 as onnx__pb2
import celaut_pb2 as celaut__pb2
import solvers_dataset_pb2 as solvers__dataset__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tapi.proto\x12\x03\x61pi\x1a\nonnx.proto\x1a\x0c\x63\x65laut.proto\x1a\x15solvers_dataset.proto\"L\n\x0eInterpretation\x12\x10\n\x08variable\x18\x01 \x03(\x05\x12\x18\n\x0bsatisfiable\x18\x02 \x01(\x08H\x00\x88\x01\x01\x42\x0e\n\x0c_satisfiable\"\x19\n\x06\x43lause\x12\x0f\n\x07literal\x18\x01 \x03(\x05\"\"\n\x03\x43nf\x12\x1b\n\x06\x63lause\x18\x01 \x03(\x0b\x32\x0b.api.Clause\"\x07\n\x05\x45mpty\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"W\n\x0fServiceWithMeta\x12\"\n\x04meta\x18\x01 \x01(\x0b\x32\x14.celaut.Any.Metadata\x12 \n\x07service\x18\x02 \x01(\x0b\x32\x0f.celaut.Service\"\xa5\x03\n\x06Tensor\x12-\n\rspecification\x18\x01 \x01(\x0b\x32\x16.celaut.Service.Tensor\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x36\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1f.api.Tensor.NonEscalarDimensionH\x00\x1a\xfe\x01\n\x13NonEscalarDimension\x12?\n\x0bnon_escalar\x18\x01 \x03(\x0b\x32*.api.Tensor.NonEscalarDimension.NonEscalar\x1a\xa5\x01\n\nNonEscalar\x12*\n\x07\x65lement\x18\x01 \x01(\x0b\x32\x19.dataset.SolverWithConfig\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x36\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1f.api.Tensor.NonEscalarDimensionH\x00\x42\x07\n\x05modelB\x07\n\x05model2-\n\x06Random\x12#\n\tRandomCnf\x12\n.api.Empty\x1a\x08.api.Cnf\"\x00\x32\x8a\x03\n\x06Solver\x12&\n\nStartTrain\x12\n.api.Empty\x1a\n.api.Empty\"\x00\x12%\n\tStopTrain\x12\n.api.Empty\x1a\n.api.Empty\"\x00\x12&\n\tGetTensor\x12\n.api.Empty\x1a\x0b.api.Tensor\"\x00\x12\x32\n\x0cUploadSolver\x12\x14.api.ServiceWithMeta\x1a\n.api.Empty\"\x00\x12\'\n\nStreamLogs\x12\n.api.Empty\x1a\t.api.File\"\x00\x30\x01\x12(\n\x05Solve\x12\x08.api.Cnf\x1a\x13.api.Interpretation\"\x00\x12&\n\tAddTensor\x12\x0b.api.Tensor\x1a\n.api.Empty\"\x00\x12,\n\nGetDataSet\x12\n.api.Empty\x1a\x10.dataset.DataSet\"\x00\x12,\n\nAddDataSet\x12\x10.dataset.DataSet\x1a\n.api.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[onnx__pb2.DESCRIPTOR,celaut__pb2.DESCRIPTOR,solvers__dataset__pb2.DESCRIPTOR,])




_INTERPRETATION = _descriptor.Descriptor(
  name='Interpretation',
  full_name='api.Interpretation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='api.Interpretation.variable', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='satisfiable', full_name='api.Interpretation.satisfiable', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
      name='_satisfiable', full_name='api.Interpretation._satisfiable',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=67,
  serialized_end=143,
)


_CLAUSE = _descriptor.Descriptor(
  name='Clause',
  full_name='api.Clause',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='literal', full_name='api.Clause.literal', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=145,
  serialized_end=170,
)


_CNF = _descriptor.Descriptor(
  name='Cnf',
  full_name='api.Cnf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clause', full_name='api.Cnf.clause', index=0,
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
  serialized_start=172,
  serialized_end=206,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='api.Empty',
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
  serialized_start=208,
  serialized_end=215,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='api.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='api.File.file', index=0,
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
  serialized_start=217,
  serialized_end=237,
)


_SERVICEWITHMETA = _descriptor.Descriptor(
  name='ServiceWithMeta',
  full_name='api.ServiceWithMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='api.ServiceWithMeta.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='api.ServiceWithMeta.service', index=1,
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
  serialized_start=239,
  serialized_end=326,
)


_TENSOR_NONESCALARDIMENSION_NONESCALAR = _descriptor.Descriptor(
  name='NonEscalar',
  full_name='api.Tensor.NonEscalarDimension.NonEscalar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='element', full_name='api.Tensor.NonEscalarDimension.NonEscalar.element', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='escalar', full_name='api.Tensor.NonEscalarDimension.NonEscalar.escalar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='api.Tensor.NonEscalarDimension.NonEscalar.non_escalar', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='model', full_name='api.Tensor.NonEscalarDimension.NonEscalar.model',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=576,
  serialized_end=741,
)

_TENSOR_NONESCALARDIMENSION = _descriptor.Descriptor(
  name='NonEscalarDimension',
  full_name='api.Tensor.NonEscalarDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='api.Tensor.NonEscalarDimension.non_escalar', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSOR_NONESCALARDIMENSION_NONESCALAR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=741,
)

_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='api.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='specification', full_name='api.Tensor.specification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='escalar', full_name='api.Tensor.escalar', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_escalar', full_name='api.Tensor.non_escalar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TENSOR_NONESCALARDIMENSION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='model', full_name='api.Tensor.model',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=329,
  serialized_end=750,
)

_INTERPRETATION.oneofs_by_name['_satisfiable'].fields.append(
  _INTERPRETATION.fields_by_name['satisfiable'])
_INTERPRETATION.fields_by_name['satisfiable'].containing_oneof = _INTERPRETATION.oneofs_by_name['_satisfiable']
_CNF.fields_by_name['clause'].message_type = _CLAUSE
_SERVICEWITHMETA.fields_by_name['meta'].message_type = celaut__pb2._ANY_METADATA
_SERVICEWITHMETA.fields_by_name['service'].message_type = celaut__pb2._SERVICE
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['element'].message_type = solvers__dataset__pb2._SOLVERWITHCONFIG
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'].message_type = onnx__pb2._MODELPROTO
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION
_TENSOR_NONESCALARDIMENSION_NONESCALAR.containing_type = _TENSOR_NONESCALARDIMENSION
_TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model'].fields.append(
  _TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'])
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['escalar'].containing_oneof = _TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model']
_TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model'].fields.append(
  _TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'])
_TENSOR_NONESCALARDIMENSION_NONESCALAR.fields_by_name['non_escalar'].containing_oneof = _TENSOR_NONESCALARDIMENSION_NONESCALAR.oneofs_by_name['model']
_TENSOR_NONESCALARDIMENSION.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION_NONESCALAR
_TENSOR_NONESCALARDIMENSION.containing_type = _TENSOR
_TENSOR.fields_by_name['specification'].message_type = celaut__pb2._SERVICE_TENSOR
_TENSOR.fields_by_name['escalar'].message_type = onnx__pb2._MODELPROTO
_TENSOR.fields_by_name['non_escalar'].message_type = _TENSOR_NONESCALARDIMENSION
_TENSOR.oneofs_by_name['model'].fields.append(
  _TENSOR.fields_by_name['escalar'])
_TENSOR.fields_by_name['escalar'].containing_oneof = _TENSOR.oneofs_by_name['model']
_TENSOR.oneofs_by_name['model'].fields.append(
  _TENSOR.fields_by_name['non_escalar'])
_TENSOR.fields_by_name['non_escalar'].containing_oneof = _TENSOR.oneofs_by_name['model']
DESCRIPTOR.message_types_by_name['Interpretation'] = _INTERPRETATION
DESCRIPTOR.message_types_by_name['Clause'] = _CLAUSE
DESCRIPTOR.message_types_by_name['Cnf'] = _CNF
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['ServiceWithMeta'] = _SERVICEWITHMETA
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Interpretation = _reflection.GeneratedProtocolMessageType('Interpretation', (_message.Message,), {
  'DESCRIPTOR' : _INTERPRETATION,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Interpretation)
  })
_sym_db.RegisterMessage(Interpretation)

Clause = _reflection.GeneratedProtocolMessageType('Clause', (_message.Message,), {
  'DESCRIPTOR' : _CLAUSE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Clause)
  })
_sym_db.RegisterMessage(Clause)

Cnf = _reflection.GeneratedProtocolMessageType('Cnf', (_message.Message,), {
  'DESCRIPTOR' : _CNF,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Cnf)
  })
_sym_db.RegisterMessage(Cnf)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Empty)
  })
_sym_db.RegisterMessage(Empty)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.File)
  })
_sym_db.RegisterMessage(File)

ServiceWithMeta = _reflection.GeneratedProtocolMessageType('ServiceWithMeta', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEWITHMETA,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.ServiceWithMeta)
  })
_sym_db.RegisterMessage(ServiceWithMeta)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {

  'NonEscalarDimension' : _reflection.GeneratedProtocolMessageType('NonEscalarDimension', (_message.Message,), {

    'NonEscalar' : _reflection.GeneratedProtocolMessageType('NonEscalar', (_message.Message,), {
      'DESCRIPTOR' : _TENSOR_NONESCALARDIMENSION_NONESCALAR,
      '__module__' : 'api_pb2'
      # @@protoc_insertion_point(class_scope:api.Tensor.NonEscalarDimension.NonEscalar)
      })
    ,
    'DESCRIPTOR' : _TENSOR_NONESCALARDIMENSION,
    '__module__' : 'api_pb2'
    # @@protoc_insertion_point(class_scope:api.Tensor.NonEscalarDimension)
    })
  ,
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'api_pb2'
  # @@protoc_insertion_point(class_scope:api.Tensor)
  })
_sym_db.RegisterMessage(Tensor)
_sym_db.RegisterMessage(Tensor.NonEscalarDimension)
_sym_db.RegisterMessage(Tensor.NonEscalarDimension.NonEscalar)



_RANDOM = _descriptor.ServiceDescriptor(
  name='Random',
  full_name='api.Random',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=752,
  serialized_end=797,
  methods=[
  _descriptor.MethodDescriptor(
    name='RandomCnf',
    full_name='api.Random.RandomCnf',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CNF,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RANDOM)

DESCRIPTOR.services_by_name['Random'] = _RANDOM


_SOLVER = _descriptor.ServiceDescriptor(
  name='Solver',
  full_name='api.Solver',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=800,
  serialized_end=1194,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartTrain',
    full_name='api.Solver.StartTrain',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopTrain',
    full_name='api.Solver.StopTrain',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTensor',
    full_name='api.Solver.GetTensor',
    index=2,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_TENSOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UploadSolver',
    full_name='api.Solver.UploadSolver',
    index=3,
    containing_service=None,
    input_type=_SERVICEWITHMETA,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLogs',
    full_name='api.Solver.StreamLogs',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_FILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Solve',
    full_name='api.Solver.Solve',
    index=5,
    containing_service=None,
    input_type=_CNF,
    output_type=_INTERPRETATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddTensor',
    full_name='api.Solver.AddTensor',
    index=6,
    containing_service=None,
    input_type=_TENSOR,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataSet',
    full_name='api.Solver.GetDataSet',
    index=7,
    containing_service=None,
    input_type=_EMPTY,
    output_type=solvers__dataset__pb2._DATASET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddDataSet',
    full_name='api.Solver.AddDataSet',
    index=8,
    containing_service=None,
    input_type=solvers__dataset__pb2._DATASET,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SOLVER)

DESCRIPTOR.services_by_name['Solver'] = _SOLVER

# @@protoc_insertion_point(module_scope)
