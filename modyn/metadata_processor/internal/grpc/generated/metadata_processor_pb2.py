# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata_processor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18metadata_processor.proto\x12\x12metadata_processor\"F\n\x17RegisterPipelineRequest\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\x05\x12\x16\n\x0eprocessor_type\x18\x02 \x01(\t\"\x12\n\x10PipelineResponse\"\xc4\x01\n\x17TrainingMetadataRequest\x12\x13\n\x0bpipeline_id\x18\x01 \x01(\x05\x12\x12\n\ntrigger_id\x18\x02 \x01(\x05\x12@\n\x10trigger_metadata\x18\x03 \x01(\x0b\x32&.metadata_processor.PerTriggerMetadata\x12>\n\x0fsample_metadata\x18\x04 \x03(\x0b\x32%.metadata_processor.PerSampleMetadata\"\"\n\x12PerTriggerMetadata\x12\x0c\n\x04loss\x18\x01 \x01(\x02\"4\n\x11PerSampleMetadata\x12\x11\n\tsample_id\x18\x01 \x01(\t\x12\x0c\n\x04loss\x18\x02 \x01(\x02\"\x1a\n\x18TrainingMetadataResponse2\xf7\x01\n\x11MetadataProcessor\x12h\n\x11register_pipeline\x12+.metadata_processor.RegisterPipelineRequest\x1a$.metadata_processor.PipelineResponse\"\x00\x12x\n\x19process_training_metadata\x12+.metadata_processor.TrainingMetadataRequest\x1a,.metadata_processor.TrainingMetadataResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'metadata_processor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _REGISTERPIPELINEREQUEST._serialized_start = 48
    _REGISTERPIPELINEREQUEST._serialized_end = 118
    _PIPELINERESPONSE._serialized_start = 120
    _PIPELINERESPONSE._serialized_end = 138
    _TRAININGMETADATAREQUEST._serialized_start = 141
    _TRAININGMETADATAREQUEST._serialized_end = 337
    _PERTRIGGERMETADATA._serialized_start = 339
    _PERTRIGGERMETADATA._serialized_end = 373
    _PERSAMPLEMETADATA._serialized_start = 375
    _PERSAMPLEMETADATA._serialized_end = 427
    _TRAININGMETADATARESPONSE._serialized_start = 429
    _TRAININGMETADATARESPONSE._serialized_end = 455
    _METADATAPROCESSOR._serialized_start = 458
    _METADATAPROCESSOR._serialized_end = 705
# @@protoc_insertion_point(module_scope)
