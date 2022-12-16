import book_pb2 as _book_pb2
import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["book"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    def __init__(self, book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["response_status"]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    response_status: _status_pb2.ResponseStatus
    def __init__(self, response_status: _Optional[_Union[_status_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "response_status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    response_status: _status_pb2.ResponseStatus
    def __init__(self, response_status: _Optional[_Union[_status_pb2.ResponseStatus, _Mapping]] = ..., book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...
