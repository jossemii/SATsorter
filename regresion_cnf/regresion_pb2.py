# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: regresion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import onnx_pb2 as onnx__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fregresion.proto\x1a\nonnx.proto\"\x07\n\x05\x45mpty\"\x14\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xcf\x02\n\x06Tensor\x12*\n\x07\x65scalar\x18\x01 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x32\n\x0bnon_escalar\x18\x02 \x01(\x0b\x32\x1b.Tensor.NonEscalarDimensionH\x00\x1a\xdb\x01\n\x13NonEscalarDimension\x12;\n\x0bnon_escalar\x18\x01 \x03(\x0b\x32&.Tensor.NonEscalarDimension.NonEscalar\x1a\x86\x01\n\nNonEscalar\x12\x0f\n\x07\x65lement\x18\x01 \x01(\t\x12*\n\x07\x65scalar\x18\x02 \x01(\x0b\x32\x17.tensor_onnx.ModelProtoH\x00\x12\x32\n\x0bnon_escalar\x18\x03 \x01(\x0b\x32\x1b.Tensor.NonEscalarDimensionH\x00\x42\x07\n\x05modelB\x07\n\x05model\"\x88\x01\n\x06\x42uffer\x12\x12\n\x05\x63hunk\x18\x01 \x01(\x0cH\x00\x88\x01\x01\x12\x16\n\tseparator\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x06signal\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x11\n\x04head\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\x08\n\x06_chunkB\x0c\n\n_separatorB\t\n\x07_signalB\x07\n\x05_head2Z\n\tRegresion\x12$\n\nStreamLogs\x12\x07.Buffer\x1a\x07.Buffer\"\x00(\x01\x30\x01\x12\'\n\rMakeRegresion\x12\x07.Buffer\x1a\x07.Buffer\"\x00(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'regresion_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=31
  _globals['_EMPTY']._serialized_end=38
  _globals['_FILE']._serialized_start=40
  _globals['_FILE']._serialized_end=60
  _globals['_TENSOR']._serialized_start=63
  _globals['_TENSOR']._serialized_end=398
  _globals['_TENSOR_NONESCALARDIMENSION']._serialized_start=170
  _globals['_TENSOR_NONESCALARDIMENSION']._serialized_end=389
  _globals['_TENSOR_NONESCALARDIMENSION_NONESCALAR']._serialized_start=255
  _globals['_TENSOR_NONESCALARDIMENSION_NONESCALAR']._serialized_end=389
  _globals['_BUFFER']._serialized_start=401
  _globals['_BUFFER']._serialized_end=537
  _globals['_REGRESION']._serialized_start=539
  _globals['_REGRESION']._serialized_end=629
# @@protoc_insertion_point(module_scope)
