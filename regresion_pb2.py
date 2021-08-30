# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: regresion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import onnx_pb2 as onnx__pb2
import solvers_dataset_pb2 as solvers__dataset__pb2
import api_pb2 as api__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='regresion.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fregresion.proto\x1a\nonnx.proto\x1a\x15solvers_dataset.proto\x1a\tapi.proto2\xc0\x01\n\tRegresion\x12\'\n\nStreamLogs\x12\n.api.Empty\x1a\t.api.File\"\x00\x30\x01\x12.\n\tGetTensor\x12\n.api.Empty\x1a\x11.tensor_onnx.ONNX\"\x00\x30\x01\x12,\n\nGetDataSet\x12\n.api.Empty\x1a\x10.dataset.DataSet\"\x00\x12,\n\nAddDataSet\x12\x10.dataset.DataSet\x1a\n.api.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[onnx__pb2.DESCRIPTOR,solvers__dataset__pb2.DESCRIPTOR,api__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REGRESION = _descriptor.ServiceDescriptor(
  name='Regresion',
  full_name='Regresion',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=66,
  serialized_end=258,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamLogs',
    full_name='Regresion.StreamLogs',
    index=0,
    containing_service=None,
    input_type=api__pb2._EMPTY,
    output_type=api__pb2._FILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTensor',
    full_name='Regresion.GetTensor',
    index=1,
    containing_service=None,
    input_type=api__pb2._EMPTY,
    output_type=onnx__pb2._ONNX,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataSet',
    full_name='Regresion.GetDataSet',
    index=2,
    containing_service=None,
    input_type=api__pb2._EMPTY,
    output_type=solvers__dataset__pb2._DATASET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddDataSet',
    full_name='Regresion.AddDataSet',
    index=3,
    containing_service=None,
    input_type=solvers__dataset__pb2._DATASET,
    output_type=api__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGRESION)

DESCRIPTOR.services_by_name['Regresion'] = _REGRESION

# @@protoc_insertion_point(module_scope)
