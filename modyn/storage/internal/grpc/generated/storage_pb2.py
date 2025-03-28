# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\rstorage.proto\x12\rmodyn.storage".\n\nGetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x03"<\n\x0bGetResponse\x12\x0f\n\x07samples\x18\x01 \x03(\x0c\x12\x0c\n\x04keys\x18\x02 \x03(\x03\x12\x0e\n\x06labels\x18\x03 \x03(\x03"\x1c\n\x1aGetCurrentTimestampRequest"?\n\x16GetNewDataSinceRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03"K\n\x17GetNewDataSinceResponse\x12\x0c\n\x04keys\x18\x01 \x03(\x03\x12\x12\n\ntimestamps\x18\x02 \x03(\x03\x12\x0e\n\x06labels\x18\x03 \x03(\x03"^\n\x18GetDataInIntervalRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x02 \x01(\x03\x12\x15\n\rend_timestamp\x18\x03 \x01(\x03"M\n\x19GetDataInIntervalResponse\x12\x0c\n\x04keys\x18\x01 \x03(\x03\x12\x12\n\ntimestamps\x18\x02 \x03(\x03\x12\x0e\n\x06labels\x18\x03 \x03(\x03"\xb7\x01\n\x17GetDataPerWorkerRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x11\n\tworker_id\x18\x02 \x01(\x05\x12\x15\n\rtotal_workers\x18\x03 \x01(\x05\x12\x1c\n\x0fstart_timestamp\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12\x1a\n\rend_timestamp\x18\x05 \x01(\x03H\x01\x88\x01\x01\x42\x12\n\x10_start_timestampB\x10\n\x0e_end_timestamp"(\n\x18GetDataPerWorkerResponse\x12\x0c\n\x04keys\x18\x01 \x03(\x03"\x8b\x01\n\x15GetDatasetSizeRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x1c\n\x0fstart_timestamp\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x1a\n\rend_timestamp\x18\x03 \x01(\x03H\x01\x88\x01\x01\x42\x12\n\x10_start_timestampB\x10\n\x0e_end_timestamp";\n\x16GetDatasetSizeResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08num_keys\x18\x02 \x01(\x03"-\n\x17\x44\x61tasetAvailableRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t"-\n\x18\x44\x61tasetAvailableResponse\x12\x11\n\tavailable\x18\x01 \x01(\x08"\xff\x01\n\x19RegisterNewDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x1f\n\x17\x66ilesystem_wrapper_type\x18\x02 \x01(\t\x12\x19\n\x11\x66ile_wrapper_type\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x11\n\tbase_path\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x06 \x01(\t\x12\x1b\n\x13\x66ile_wrapper_config\x18\x07 \x01(\t\x12\x1d\n\x15ignore_last_timestamp\x18\x08 \x01(\x08\x12\x1d\n\x15\x66ile_watcher_interval\x18\t \x01(\x03"-\n\x1aRegisterNewDatasetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"0\n\x1bGetCurrentTimestampResponse\x12\x11\n\ttimestamp\x18\x01 \x01(\x03"(\n\x15\x44\x65leteDatasetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08"5\n\x11\x44\x65leteDataRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\x03"%\n\x12\x44\x65leteDataResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe2\x07\n\x07Storage\x12@\n\x03Get\x12\x19.modyn.storage.GetRequest\x1a\x1a.modyn.storage.GetResponse"\x00\x30\x01\x12\x64\n\x0fGetNewDataSince\x12%.modyn.storage.GetNewDataSinceRequest\x1a&.modyn.storage.GetNewDataSinceResponse"\x00\x30\x01\x12j\n\x11GetDataInInterval\x12\'.modyn.storage.GetDataInIntervalRequest\x1a(.modyn.storage.GetDataInIntervalResponse"\x00\x30\x01\x12g\n\x10GetDataPerWorker\x12&.modyn.storage.GetDataPerWorkerRequest\x1a\'.modyn.storage.GetDataPerWorkerResponse"\x00\x30\x01\x12_\n\x0eGetDatasetSize\x12$.modyn.storage.GetDatasetSizeRequest\x1a%.modyn.storage.GetDatasetSizeResponse"\x00\x12\x66\n\x11\x43heckAvailability\x12&.modyn.storage.DatasetAvailableRequest\x1a\'.modyn.storage.DatasetAvailableResponse"\x00\x12k\n\x12RegisterNewDataset\x12(.modyn.storage.RegisterNewDatasetRequest\x1a).modyn.storage.RegisterNewDatasetResponse"\x00\x12n\n\x13GetCurrentTimestamp\x12).modyn.storage.GetCurrentTimestampRequest\x1a*.modyn.storage.GetCurrentTimestampResponse"\x00\x12_\n\rDeleteDataset\x12&.modyn.storage.DatasetAvailableRequest\x1a$.modyn.storage.DeleteDatasetResponse"\x00\x12S\n\nDeleteData\x12 .modyn.storage.DeleteDataRequest\x1a!.modyn.storage.DeleteDataResponse"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "storage_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_GETREQUEST"]._serialized_start = 32
    _globals["_GETREQUEST"]._serialized_end = 78
    _globals["_GETRESPONSE"]._serialized_start = 80
    _globals["_GETRESPONSE"]._serialized_end = 140
    _globals["_GETCURRENTTIMESTAMPREQUEST"]._serialized_start = 142
    _globals["_GETCURRENTTIMESTAMPREQUEST"]._serialized_end = 170
    _globals["_GETNEWDATASINCEREQUEST"]._serialized_start = 172
    _globals["_GETNEWDATASINCEREQUEST"]._serialized_end = 235
    _globals["_GETNEWDATASINCERESPONSE"]._serialized_start = 237
    _globals["_GETNEWDATASINCERESPONSE"]._serialized_end = 312
    _globals["_GETDATAININTERVALREQUEST"]._serialized_start = 314
    _globals["_GETDATAININTERVALREQUEST"]._serialized_end = 408
    _globals["_GETDATAININTERVALRESPONSE"]._serialized_start = 410
    _globals["_GETDATAININTERVALRESPONSE"]._serialized_end = 487
    _globals["_GETDATAPERWORKERREQUEST"]._serialized_start = 490
    _globals["_GETDATAPERWORKERREQUEST"]._serialized_end = 673
    _globals["_GETDATAPERWORKERRESPONSE"]._serialized_start = 675
    _globals["_GETDATAPERWORKERRESPONSE"]._serialized_end = 715
    _globals["_GETDATASETSIZEREQUEST"]._serialized_start = 718
    _globals["_GETDATASETSIZEREQUEST"]._serialized_end = 857
    _globals["_GETDATASETSIZERESPONSE"]._serialized_start = 859
    _globals["_GETDATASETSIZERESPONSE"]._serialized_end = 918
    _globals["_DATASETAVAILABLEREQUEST"]._serialized_start = 920
    _globals["_DATASETAVAILABLEREQUEST"]._serialized_end = 965
    _globals["_DATASETAVAILABLERESPONSE"]._serialized_start = 967
    _globals["_DATASETAVAILABLERESPONSE"]._serialized_end = 1012
    _globals["_REGISTERNEWDATASETREQUEST"]._serialized_start = 1015
    _globals["_REGISTERNEWDATASETREQUEST"]._serialized_end = 1270
    _globals["_REGISTERNEWDATASETRESPONSE"]._serialized_start = 1272
    _globals["_REGISTERNEWDATASETRESPONSE"]._serialized_end = 1317
    _globals["_GETCURRENTTIMESTAMPRESPONSE"]._serialized_start = 1319
    _globals["_GETCURRENTTIMESTAMPRESPONSE"]._serialized_end = 1367
    _globals["_DELETEDATASETRESPONSE"]._serialized_start = 1369
    _globals["_DELETEDATASETRESPONSE"]._serialized_end = 1409
    _globals["_DELETEDATAREQUEST"]._serialized_start = 1411
    _globals["_DELETEDATAREQUEST"]._serialized_end = 1464
    _globals["_DELETEDATARESPONSE"]._serialized_start = 1466
    _globals["_DELETEDATARESPONSE"]._serialized_end = 1503
    _globals["_STORAGE"]._serialized_start = 1506
    _globals["_STORAGE"]._serialized_end = 2500
# @@protoc_insertion_point(module_scope)
