# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import service.book_pb2 as book__pb2
import service.status_pb2 as status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17inventory_service.proto\x12\x1aservices.inventory_service\x1a\nbook.proto\x1a\x0cstatus.proto\"4\n\x11\x43reateBookRequest\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.models.book.Book\"I\n\x12\x43reateBookResponse\x12\x33\n\x0fresponse_status\x18\x01 \x01(\x0b\x32\x1a.google.rpc.ResponseStatus\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\"g\n\x0fGetBookResponse\x12\x33\n\x0fresponse_status\x18\x01 \x01(\x0b\x32\x1a.google.rpc.ResponseStatus\x12\x1f\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x11.models.book.Book2\xe7\x01\n\x10InventoryService\x12m\n\nCreateBook\x12-.services.inventory_service.CreateBookRequest\x1a..services.inventory_service.CreateBookResponse\"\x00\x12\x64\n\x07GetBook\x12*.services.inventory_service.GetBookRequest\x1a+.services.inventory_service.GetBookResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBOOKREQUEST._serialized_start=81
  _CREATEBOOKREQUEST._serialized_end=133
  _CREATEBOOKRESPONSE._serialized_start=135
  _CREATEBOOKRESPONSE._serialized_end=208
  _GETBOOKREQUEST._serialized_start=210
  _GETBOOKREQUEST._serialized_end=240
  _GETBOOKRESPONSE._serialized_start=242
  _GETBOOKRESPONSE._serialized_end=345
  _INVENTORYSERVICE._serialized_start=348
  _INVENTORYSERVICE._serialized_end=579
# @@protoc_insertion_point(module_scope)
