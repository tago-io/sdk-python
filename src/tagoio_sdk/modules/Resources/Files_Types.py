from datetime import datetime
from typing import Any
from typing import Callable
from typing import List
from typing import Optional
from typing import TypedDict


class FileQuery(TypedDict, total=False):
    path: str
    paginationToken: str
    quantity: int


class FileInfo(TypedDict):
    filename: str
    size: int
    last_modified: Optional[datetime]


class FileListInfo(TypedDict):
    files: List[FileInfo]
    folders: List[str]


class Base64File(TypedDict, total=False):
    filename: str
    """Name of file"""
    file: str
    """String of Base64"""
    public: bool
    """
    Make file public
    default: False
    """


class CopyFiles(TypedDict):
    __annotations__ = {"from": str}
    """Using '__annotations__' to define this field because 'from' is a Python reserved keyword."""
    to: str


class MoveFiles(TypedDict):
    __annotations__ = {"from": str}
    """Using '__annotations__' to define this field because 'from' is a Python reserved keyword."""
    to: str


class FilesPermission(TypedDict):
    file: str
    public: bool


class UploadOptions(TypedDict, total=False):
    maxTriesForEachChunk: int
    """
    The maximum amount of tries to upload each chunk to TagoIO.

    After this many unsuccessful tries of a single chunk, the upload is aborted
    """
    timeoutForEachFailedChunk: int
    """timeout before trying to upload the same chunk if the request failed"""
    contentType: str
    """The file's content type. This is optional"""
    isPublic: bool
    """if the file can be accessed by anybody with a link or not"""
    dashboard: str
    """
    Dashboard ID.

    Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.
    """
    widget: str
    """
    Widget ID.

    Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.
    """
    fieldId: str
    """
    ID of the field from the widget where the file is selected.

    Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.
    """
    onCancelToken: Callable[[Callable[[], Any]], Any]
    """will provide a cancel token for you to cancel the request"""
    chunkSize: int
    """the byte size of each chunk sent to TagoIO. This will influence how many requests this function will perform"""
    onProgress: Callable[[float], Any]
    """will provide the upload percentage for this file"""
