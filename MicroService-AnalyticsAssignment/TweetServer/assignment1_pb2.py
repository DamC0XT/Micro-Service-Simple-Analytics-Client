# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assignment1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='assignment1.proto',
  package='assignment1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11\x61ssignment1.proto\x12\x0b\x61ssignment1\"\x1b\n\x0bSizeRequest\x12\x0c\n\x04size\x18\x01 \x01(\t\"\x1d\n\nTweetReply\x12\x0f\n\x07message\x18\x01 \x01(\t2Q\n\x0bTweetSender\x12\x42\n\tSendTweet\x12\x18.assignment1.SizeRequest\x1a\x17.assignment1.TweetReply\"\x00\x30\x01\x62\x06proto3'
)




_SIZEREQUEST = _descriptor.Descriptor(
  name='SizeRequest',
  full_name='assignment1.SizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='assignment1.SizeRequest.size', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=61,
)


_TWEETREPLY = _descriptor.Descriptor(
  name='TweetReply',
  full_name='assignment1.TweetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='assignment1.TweetReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=92,
)

DESCRIPTOR.message_types_by_name['SizeRequest'] = _SIZEREQUEST
DESCRIPTOR.message_types_by_name['TweetReply'] = _TWEETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SizeRequest = _reflection.GeneratedProtocolMessageType('SizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIZEREQUEST,
  '__module__' : 'assignment1_pb2'
  # @@protoc_insertion_point(class_scope:assignment1.SizeRequest)
  })
_sym_db.RegisterMessage(SizeRequest)

TweetReply = _reflection.GeneratedProtocolMessageType('TweetReply', (_message.Message,), {
  'DESCRIPTOR' : _TWEETREPLY,
  '__module__' : 'assignment1_pb2'
  # @@protoc_insertion_point(class_scope:assignment1.TweetReply)
  })
_sym_db.RegisterMessage(TweetReply)



_TWEETSENDER = _descriptor.ServiceDescriptor(
  name='TweetSender',
  full_name='assignment1.TweetSender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=94,
  serialized_end=175,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendTweet',
    full_name='assignment1.TweetSender.SendTweet',
    index=0,
    containing_service=None,
    input_type=_SIZEREQUEST,
    output_type=_TWEETREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TWEETSENDER)

DESCRIPTOR.services_by_name['TweetSender'] = _TWEETSENDER

# @@protoc_insertion_point(module_scope)
