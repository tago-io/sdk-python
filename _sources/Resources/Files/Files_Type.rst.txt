**Files Type**
===============


.. _FileQuery:

FileQuery
---------

    **Attributes:**

        | path: str
        | Path to search for files

        | paginationToken: str
        | Token for paginated results

        | quantity: int
        | Number of files to return


.. _FileInfo:

FileInfo
--------

    **Attributes:**

        | filename: str
        | Name of the file

        | size: int
        | Size of the file in bytes

        | last_modified: Optional[datetime]
        | Date and time when the file was last modified


.. _FileListInfo:

FileListInfo
------------

    **Attributes:**

        | files: List[:ref:`FileInfo`]
        | List of file information

        | folders: List[str]
        | List of folder names


.. _Base64File:

Base64File
----------

    **Attributes:**

        | filename: str
        | Name of file

        | file: str
        | String of Base64

        | public: bool
        | Make file public
        | default: False


.. _CopyFiles:

CopyFiles
---------

    **Attributes:**

        | from: str
        | Source path of the file to be copied

        | to: str
        | Destination path for the copied file


.. _MoveFiles:

MoveFiles
---------

    **Attributes:**

        | from: str
        | Source path of the file to be moved

        | to: str
        | Destination path for the moved file


.. _FilesPermission:

FilesPermission
---------------

    **Attributes:**

        | file: str
        | Path to the file

        | public: bool
        | Whether the file should be publicly accessible


.. _UploadOptions:

UploadOptions
-------------

    **Attributes:**

        | maxTriesForEachChunk: int
        | The maximum amount of tries to upload each chunk to TagoIO. After this many unsuccessful tries of a single chunk, the upload is aborted

        | timeoutForEachFailedChunk: int
        | Timeout before trying to upload the same chunk if the request failed

        | contentType: str
        | The file's content type. This is optional

        | isPublic: bool
        | If the file can be accessed by anybody with a link or not

        | dashboard: str
        | Dashboard ID. Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.

        | widget: str
        | Widget ID. Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.

        | fieldId: str
        | ID of the field from the widget where the file is selected. Uploading files from a widget requires `dashboard`, `widget`, and `fieldId` to be provided.

        | onCancelToken: Callable[[Callable[[], Any]], Any]
        | Will provide a cancel token for you to cancel the request

        | chunkSize: int
        | The byte size of each chunk sent to TagoIO. This will influence how many requests this function will perform

        | onProgress: Callable[[float], Any]
        | Will provide the upload percentage for this file
