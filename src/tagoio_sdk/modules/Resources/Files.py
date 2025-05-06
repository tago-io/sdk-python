import time
from typing import Dict, List, Optional, Any

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Utils.dateParser import dateParserList
from tagoio_sdk.modules.Resources.Files_Types import (
    Base64File,
    CopyFiles,
    FileListInfo,
    FileQuery,
    FilesPermission,
    MoveFiles,
    UploadOptions,
)


class Files(TagoIOModule):
    """Manage files in TagoIO."""

    def list(self, queryObj: Optional[FileQuery] = None) -> FileListInfo:
        """
        @description:
            Lists all files in the application with pagination support.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.files.list({
              "path": "/my/folder",
              "quantity": 100
            })
            print(result)  # { 'total': 200, 'usage': 0.05, 'files': [{ 'size': 7812, ...}], 'folders': ['my-folder'] }
            ```
        """
        queryObj = queryObj or {}

        result = self.doRequest(
            {
                "path": "/files",
                "method": "GET",
                "params": {
                    "path": queryObj.get("path", "/"),
                    "pagination_token": queryObj.get("paginationToken"),
                    "qty": queryObj.get("quantity", 300),
                },
            }
        )

        if "files" in result:
            result["files"] = dateParserList(result["files"], ["last_modified"])

        return result

    def uploadBase64(self, fileList: List[Base64File]) -> str:
        """
        @description:
            Uploads base64 encoded files to TagoIO storage.

        @see:
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Upload** in Access Management.
            ```python
            resources = Resources()
            result = resources.files.uploadBase64([{
              "filename": "/my-files/document.pdf",
              "file": "base64EncodedContent",
              "public": True,
            }])
            print(result)
            ```
        """
        result = self.doRequest(
            {
                "path": "/files",
                "method": "POST",
                "body": fileList,
            }
        )

        return result

    def move(self, fileList: List[MoveFiles]) -> str:
        """
        @description:
            Moves or renames files in TagoIO storage.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.files.move([{
              "from": "/old/path/file.txt",
              "to": "/new/path/renamed.txt"
            }])
            print(result)  # Successfully Updated
            ```
        """
        # Convert from->to dictionaries to match Python structure where "from" is a keyword
        mapped_files = []
        for file_item in fileList:
            if hasattr(file_item, "from") and hasattr(file_item, "to"):
                mapped_files.append({"from": getattr(file_item, "from"), "to": file_item.to})
            elif "_from" in file_item:
                mapped_files.append({"from": file_item["_from"], "to": file_item["to"]})
            else:
                # Try to extract from __annotations__ if using that pattern
                mapped_files.append(file_item)

        result = self.doRequest(
            {
                "path": "/files",
                "method": "PUT",
                "body": mapped_files,
            }
        )

        return result

    def copy(self, fileList: List[CopyFiles]) -> str:
        """
        @description:
            Copies files in TagoIO files.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            ```python
            resources = Resources()
            result = resources.files.copy([{
              "from": "/source/file.txt",
              "to": "/destination/copy.txt"
            }])
            print(result)
            ```
        """
        # Convert from->to dictionaries to match Python structure
        mapped_files = []
        for file_item in fileList:
            if hasattr(file_item, "from") and hasattr(file_item, "to"):
                mapped_files.append({"from": getattr(file_item, "from"), "to": file_item.to})
            elif "_from" in file_item:
                mapped_files.append({"from": file_item["_from"], "to": file_item["to"]})
            else:
                # Try to extract from __annotations__ if using that pattern
                mapped_files.append(file_item)

        result = self.doRequest(
            {
                "path": "/files/copy",
                "method": "PUT",
                "body": mapped_files,
            }
        )

        return result

    def delete(self, files: List[str]) -> str:
        """
        @description:
            Deletes files or folders from TagoIO storage.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Upload** in Access Management.
            ```python
            resources = Resources()
            result = resources.files.delete([
              "/path/to/file.txt",
              "/folder/to/delete"
            ])
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": "/files",
                "method": "DELETE",
                "body": files,
            }
        )

        return result

    def checkPermission(self, file: str) -> Dict[str, bool]:
        """
        @description:
            Checks if a file is public or private.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Access** in Access Management.
            ```python
            resources = Resources()
            permission = resources.files.checkPermission("/path/to/file.txt")
            print(permission["public"])  # True or False
            ```
        """
        result = self.doRequest(
            {
                "path": "/files/permission",
                "method": "GET",
                "params": {
                    "file": file,
                },
            }
        )

        return result

    def changePermission(self, filesVisibility: List[FilesPermission]) -> str:
        """
        @description:
            Changes visibility settings for multiple files.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.files.changePermission([{
              "file": "/path/to/file.txt",
              "public": True
            }])
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": "/files/permission",
                "method": "PUT",
                "body": filesVisibility,
            }
        )

        return result

    def _getPathFromUrl(self, url: str) -> str:
        tago_url = url.find(".tago.io/file/")

        if tago_url == -1:
            raise ValueError(f"{url} is not a TagoIO files url")

        return url[tago_url + 8 :]

    def getFileURLSigned(self, url: str) -> str:
        """
        @description:
            Gets a signed URL with temporary authentication token.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Access** in Access Management.
            ```python
            resources = Resources()
            signed_url = resources.files.getFileURLSigned("https://api.tago.io/file/...")
            print(signed_url)
            ```
        """
        path = self._getPathFromUrl(url)

        result = self.doRequest(
            {
                "path": path,
                "method": "GET",
                "params": {
                    "noRedirect": True,
                },
            }
        )

        return result

    def getFileMD5(self, url: str) -> str:
        """
        @description:
            Gets the MD5 hash of a file with authentication for private files.
            This hash can be used to verify file integrity.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Access** in Access Management
            ```python
            resources = Resources()
            md5_hash = resources.files.getFileMD5("https://storage.tago.io/file/path/document.pdf")
            print(md5_hash)  # e.g. "d41d8cd98f00b204e9800998ecf8427e"
            ```
        """
        path = self._getPathFromUrl(url)

        result = self.doRequest(
            {
                "path": path,
                "method": "GET",
                "params": {
                    "md5": True,
                    "noRedirect": True,
                },
            }
        )

        return result

    def _createMultipartUpload(self, filename: str, options: Optional[UploadOptions] = None) -> Dict[str, Any]:
        options = options or {}
        dashboard = options.get("dashboard")
        widget = options.get("widget")
        field_id = options.get("fieldId")
        is_public = options.get("isPublic")
        content_type = options.get("contentType")

        path = f"/data/files/{dashboard}/{widget}" if dashboard and widget and field_id else "/files"

        result = self.doRequest(
            {
                "path": path,
                "method": "POST",
                "body": {
                    "multipart_action": "start",
                    "filename": filename,
                    "public": is_public,
                    "contentType": content_type,
                    **({"field_id": field_id} if field_id else {}),
                },
            }
        )

        return result

    def _uploadPart(
        self, filename: str, upload_id: str, part_number: int, blob: bytes, options: Optional[UploadOptions] = None
    ) -> Dict[str, Any]:
        options = options or {}
        field_id = options.get("fieldId")
        dashboard = options.get("dashboard")
        widget = options.get("widget")

        path = f"/data/files/{dashboard}/{widget}" if dashboard and widget else "/files"

        # Prepare the multipart form data
        form_data = {
            "filename": filename,
            "upload_id": upload_id,
            "part": str(part_number),
            "file": (filename, io.BytesIO(blob), "application/octet-stream"),
            "multipart_action": "upload",
        }

        if field_id:
            form_data["field_id"] = field_id

        import io

        files = {"file": (filename, io.BytesIO(blob), "application/octet-stream")}

        headers = {"Content-Type": "multipart/form-data"}

        result = self.doRequest(
            {
                "path": path,
                "method": "POST",
                "body": form_data,
                "files": files,
                "maxContentLength": float("infinity"),
                "headers": headers,
            }
        )

        return {
            "ETag": result["ETag"],
            "PartNumber": part_number,
        }

    def _addToQueue(
        self,
        filename: str,
        upload_id: GenericID,
        part_number: int,
        blob: bytes,
        options: Optional[UploadOptions],
    ) -> Dict[str, Any]:
        options = options or {}
        max_tries = options.get("maxTriesForEachChunk", 5)
        timeout = options.get("timeoutForEachFailedChunk", 2000)

        tries = 0

        while tries < max_tries:
            try:
                result = self._uploadPart(filename, upload_id, part_number, blob, options)
                return result
            except Exception as ex:
                if is_limit_error(ex):
                    raise ValueError(str(ex))

                time.sleep(timeout / 1000)  # Convert ms to seconds

                tries += 1
                if tries >= max_tries:
                    raise ValueError(f"Could not upload part number {part_number}: {str(ex)}")

        # This should never be reached due to the exception above
        return {}

    def _completeMultipartUpload(
        self, filename: str, upload_id: str, parts: List[Dict[str, Any]], options: Optional[UploadOptions] = None
    ) -> Dict[str, str]:
        options = options or {}
        field_id = options.get("fieldId")
        dashboard = options.get("dashboard")
        widget = options.get("widget")

        path = f"/data/files/{dashboard}/{widget}" if dashboard and widget else "/files"

        # Sort parts by part number
        parts_ordered = sorted(parts, key=lambda x: x["PartNumber"])

        headers = {"Content-Type": "multipart/form-data"}

        body = {
            "multipart_action": "end",
            "upload_id": upload_id,
            "filename": filename,
            "parts": parts_ordered,
            "headers": headers,
        }

        if field_id:
            body["field_id"] = field_id

        result = self.doRequest(
            {
                "path": path,
                "method": "POST",
                "body": body,
            }
        )

        return result

    def uploadFile(self, file: bytes, filename: str, options: Optional[UploadOptions] = None) -> Dict[str, str]:
        """
        @description:
            Uploads a single file to TagoIO using multipart upload.
            The file is divided into chunks and uploaded in parallel for better performance.

        @see:
            https://help.tago.io/portal/en/kb/articles/127-files Files
            https://help.tago.io/portal/en/kb/articles/140-uploading-files Uploading Files

        @example:
            If receive an error "Authorization Denied", check policy **File** / **Upload** in Access Management.
            ```python
            resources = Resources()
            with open('myfile.txt', 'rb') as f:
                file_data = f.read()
            result = resources.files.uploadFile(file_data, "/uploads/myfile.txt", {
              "chunkSize": 5 * 1024 * 1024,  # 5MB chunks
              "onProgress": lambda progress: print(f"Upload progress: {progress}%")
            })
            print(result["file"])  # https://api.tago.io/file/.../uploads/myfile.txt
            ```
        """
        options = options or {}
        MB = 2**20

        # Setup cancellation if provided
        cancelled = False
        if options.get("onCancelToken"):
            options["onCancelToken"](lambda: setattr(locals(), "cancelled", True))

        self._is_canceled(cancelled)

        # Start the multipart upload
        upload_id = self._createMultipartUpload(filename, options)

        # Calculate chunk sizes
        bytes_per_chunk = options.get("chunkSize", 7 * MB)
        file_size = len(file)
        chunk_amount = (file_size // bytes_per_chunk) + 1
        parts_per_time = 3

        # Check minimum chunk size for multipart uploads
        if chunk_amount > 1 and bytes_per_chunk < 5 * MB:
            raise ValueError("Chunk sizes cannot be lower than 5mb if the upload will have multiple parts")

        # Initialize tracking variables
        offset_start = 0
        offset_end = bytes_per_chunk
        part_number = 1
        error = None
        parts = []
        promises = []

        import threading

        self._is_canceled(cancelled)

        # Function to process chunks and update progress
        def process_chunk(offset_start, offset_end, part_number):
            try:
                sliced = file[offset_start:offset_end]
                part_data = self._addToQueue(filename, upload_id, part_number, sliced, options)
                parts.append(part_data)

                # Update progress if callback provided
                if options.get("onProgress"):
                    percentage = (len(parts) * 100) / chunk_amount
                    limited_percentage = min(percentage, 100)
                    rounded_percentage = round(limited_percentage, 2)
                    options["onProgress"](rounded_percentage)

                return part_data
            except Exception as e:
                nonlocal error
                error = e
                return None

        # Upload each chunk
        while offset_start < file_size:
            # Check if we're at the maximum parallel uploads
            while len(promises) >= parts_per_time:
                self._is_canceled(cancelled)

                if error:
                    raise error

                time.sleep(1)

                # Check if any threads have completed
                promises = [p for p in promises if p.is_alive()]

            # Start a new upload thread
            thread = threading.Thread(target=process_chunk, args=(offset_start, offset_end, part_number))
            thread.start()
            promises.append(thread)

            self._is_canceled(cancelled)

            time.sleep(0.5)

            # Move to the next chunk
            offset_start = offset_end
            offset_end = offset_start + bytes_per_chunk
            part_number += 1

        # Wait for all uploads to complete
        while promises:
            self._is_canceled(cancelled)

            if error:
                raise error

            time.sleep(1)

            # Update the list of active threads
            promises = [p for p in promises if p.is_alive()]

        self._is_canceled(cancelled)

        # Complete the multipart upload with retries
        for i in range(3):
            try:
                return self._completeMultipartUpload(filename, upload_id, parts, options)
            except Exception as ex:
                if is_limit_error(ex):
                    raise ValueError(str(ex))

                time.sleep(1)
                if i == 2:  # Last attempt failed
                    raise ex

        # This should never be reached due to the exception above
        return {}

    def _is_canceled(self, cancelled: bool):
        if cancelled:
            raise ValueError("Cancelled request")


def is_limit_error(error: Exception) -> bool:
    if not hasattr(error, "message") and not isinstance(error, Exception):
        return False

    message = str(error)

    # TODO: Use status code instead of string error message when available.
    return message.startswith("You have exceeded the maximum limit")
