**Files**
==========

Manage files in TagoIO.

=======
list
=======

Lists all files in the application with pagination support.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`FileQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "path": "/",
                "paginationToken": None,
                "quantity": 300,
            }

    **Returns:**

        | :ref:`FileListInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.list({
          "path": "/my/folder",
          "quantity": 100
        })
        print(result)  # { 'total': 200, 'usage': 0.05, 'files': [{ 'size': 7812, ...}], 'folders': ['my-folder'] }


============
uploadBase64
============

Uploads base64 encoded files to TagoIO storage.

See: `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **fileList**: list[:ref:`Base64File`]
        | List of files to upload in base64 format

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.uploadBase64([{
          "filename": "/my-files/document.pdf",
          "file": "base64EncodedContent",
          "public": True,
        }])
        print(result)


=======
move
=======

Moves or renames files in TagoIO storage.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **fileList**: list[:ref:`MoveFiles`]
        | List of file paths to move/rename

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.move([{
          "from": "/old/path/file.txt",
          "to": "/new/path/renamed.txt"
        }])
        print(result)  # Successfully Updated


=======
copy
=======

Copies files in TagoIO files.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **fileList**: list[:ref:`CopyFiles`]
        | List of file paths to copy

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.copy([{
          "from": "/source/file.txt",
          "to": "/destination/copy.txt"
        }])
        print(result)


=======
delete
=======

Deletes files or folders from TagoIO storage.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **files**: list[str]
        | List of file paths to delete

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.delete([
          "/path/to/file.txt",
          "/folder/to/delete"
        ])
        print(result)  # Successfully Removed


===============
checkPermission
===============

Checks if a file is public or private.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **file**: str
        | File path to check permissions

    **Returns:**

        | Dict[str, bool]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        permission = resources.files.checkPermission("/path/to/file.txt")
        print(permission["public"])  # True or False


=================
changePermission
=================

Changes visibility settings for multiple files.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **filesVisibility**: list[:ref:`FilesPermission`]
        | List of file permission settings

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.files.changePermission([{
          "file": "/path/to/file.txt",
          "public": True
        }])
        print(result)  # Successfully Updated


================
getFileURLSigned
================

Gets a signed URL with temporary authentication token.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **url**: str
        | URL of the file to get signed URL

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        signed_url = resources.files.getFileURLSigned("https://api.tago.io/file/...")
        print(signed_url)


============
getFileMD5
============

Gets the MD5 hash of a file with authentication for private files.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **url**: str
        | URL of the file to get MD5 hash

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        md5_hash = resources.files.getFileMD5("https://storage.tago.io/file/path/document.pdf")
        print(md5_hash)  # e.g. "d41d8cd98f00b204e9800998ecf8427e"


============
uploadFile
============

Uploads a single file to TagoIO using multipart upload.

See: `Files <https://help.tago.io/portal/en/kb/articles/127-files>`_ | `Uploading Files <https://help.tago.io/portal/en/kb/articles/140-uploading-files>`_

    **Parameters:**

        | **file**: bytes
        | Binary file data to upload

        | **filename**: str
        | Path and filename for the file

        | *Optional* **options**: :ref:`UploadOptions`
        | Options for the file upload

    **Returns:**

        | Dict[str, str]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        with open('myfile.txt', 'rb') as f:
            file_data = f.read()
        result = resources.files.uploadFile(file_data, "/uploads/myfile.txt", {
          "chunkSize": 5 * 1024 * 1024,  # 5MB chunks
          "onProgress": lambda progress: print(f"Upload progress: {progress}%")
        })
        print(result["file"])  # https://api.tago.io/file/.../uploads/myfile.txt

.. toctree::


.. toctree::

    Files_Type
