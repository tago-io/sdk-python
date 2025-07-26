import time

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Files_Types import Base64File
from tagoio_sdk.modules.Resources.Files_Types import CopyFiles
from tagoio_sdk.modules.Resources.Files_Types import FileListInfo
from tagoio_sdk.modules.Resources.Files_Types import FileQuery
from tagoio_sdk.modules.Resources.Files_Types import FilesPermission
from tagoio_sdk.modules.Resources.Files_Types import MoveFiles
from tagoio_sdk.modules.Resources.Files_Types import UploadOptions
from tagoio_sdk.modules.Utils.dateParser import dateParserList
from tagoio_sdk.regions import getConnectionURI


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

    def _createMultipartUpload(self, filename: str, options: Optional[UploadOptions] = None) -> str:
        """Creates a multipart upload instance."""
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
        """Uploads a single part to TagoIO."""
        options = options or {}
        field_id = options.get("fieldId")
        dashboard = options.get("dashboard")
        widget = options.get("widget")

        path = f"/data/files/{dashboard}/{widget}" if dashboard and widget else "/files"

        import io

        import requests

        from requests_toolbelt.multipart.encoder import MultipartEncoder

        # Create multipart form data with proper content type
        form_data = {
            "filename": (None, filename),
            "upload_id": (None, upload_id),
            "part": (None, str(part_number)),
            "multipart_action": (None, "upload"),
            # Use actual filename here and correct content type
            "file": (filename, io.BytesIO(blob), "application/octet-stream"),
        }

        if field_id:
            form_data["field_id"] = (None, field_id)

        multipart = MultipartEncoder(fields=form_data)
        headers = {"Content-Type": multipart.content_type, "token": self.token}

        # Need to directly use requests here for proper multipart handling
        api_url = getConnectionURI(self.region)["api"]
        url = f"{api_url}{path}"

        response = requests.post(url=url, data=multipart, headers=headers)

        if response.status_code >= 200 and response.status_code < 300:
            result = response.json().get("result", {})
            return {"ETag": result.get("ETag"), "PartNumber": part_number}
        else:
            error_message = response.text
            try:
                error_data = response.json()
                if "message" in error_data:
                    error_message = error_data["message"]
            except Exception:
                pass
            raise ValueError(f"Error in part upload: {error_message}")

    def _addToQueue(
        self,
        filename: str,
        upload_id: str,
        part_number: int,
        blob: bytes,
        options: Optional[UploadOptions] = None,
    ) -> Dict[str, Any]:
        """
        Adds an upload to the queue.
        It will try to upload for 'opts.maxTriesForEachChunk' and fail
        if it couldn't upload after those many tries.
        """
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
                    raise ValueError(str(ex)) from ex

                time.sleep(timeout / 1000)  # Convert ms to seconds

                tries += 1
                if tries >= max_tries:
                    raise ValueError(f"Could not upload part number {part_number}: {str(ex)}") from ex

        # This should never be reached due to the exception above
        return {}

    def _completeMultipartUpload(
        self, filename: str, upload_id: str, parts: List[Dict[str, Any]], options: Optional[UploadOptions] = None
    ) -> Dict[str, str]:
        """Finishes a multipart upload instance."""
        options = options or {}
        field_id = options.get("fieldId")
        dashboard = options.get("dashboard")
        widget = options.get("widget")

        path = f"/data/files/{dashboard}/{widget}" if dashboard and widget else "/files"

        # Sort parts by part number
        parts_ordered = sorted(parts, key=lambda x: x["PartNumber"])

        result = self.doRequest(
            {
                "path": path,
                "method": "POST",
                "body": {
                    "multipart_action": "end",
                    "upload_id": upload_id,
                    "filename": filename,
                    "parts": parts_ordered,
                    **({"field_id": field_id} if field_id else {}),
                },
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
            options["onCancelToken"](lambda: globals().update(cancelled=True))

        self._is_canceled(cancelled)

        # Start the multipart upload
        upload_id = self._createMultipartUpload(filename, options)

        # Calculate chunk sizes
        bytes_per_chunk = options.get("chunkSize", 7 * MB)
        file_size = len(file)
        chunk_amount = (file_size // bytes_per_chunk) + (1 if file_size % bytes_per_chunk > 0 else 0)
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

        import queue
        import threading

        self._is_canceled(cancelled)

        # Queue to collect results from threads
        result_queue = queue.Queue()

        # Function to process chunks
        def process_chunk(start: int, end: int, p_num: int) -> None:
            try:
                sliced = file[start:end]
                part_data = self._addToQueue(filename, upload_id, p_num, sliced, options)
                result_queue.put(("success", part_data, p_num))
            except Exception as e:
                result_queue.put(("error", str(e), p_num))

        active_threads = set()

        # Upload each chunk
        while offset_start < file_size:
            # Check if we're at the maximum parallel uploads
            while len(active_threads) >= parts_per_time:
                self._is_canceled(cancelled)

                # Check for completed threads and process results
                still_active = set()
                for thread in active_threads:
                    if thread.is_alive():
                        still_active.add(thread)

                # Update active threads
                active_threads = still_active

                # Process any results
                while not result_queue.empty():
                    status, data, p_num = result_queue.get()
                    if status == "success":
                        parts.append(data)
                        if options.get("onProgress"):
                            percentage = (len(parts) * 100) / chunk_amount
                            limited_percentage = min(percentage, 100)
                            rounded_percentage = round(limited_percentage, 2)
                            options["onProgress"](rounded_percentage)
                    else:
                        error = ValueError(f"Error uploading part {p_num}: {data}")

                if error:
                    raise error

                time.sleep(0.2)

            # Start a new upload thread
            thread = threading.Thread(
                target=process_chunk, args=(offset_start, min(offset_end, file_size), part_number)
            )
            thread.start()
            active_threads.add(thread)

            self._is_canceled(cancelled)
            time.sleep(0.1)

            # Move to the next chunk
            offset_start = offset_end
            offset_end = offset_start + bytes_per_chunk
            part_number += 1

        # Wait for all uploads to complete
        while active_threads:
            self._is_canceled(cancelled)

            # Check for completed threads
            still_active = set()
            for thread in active_threads:
                if thread.is_alive():
                    still_active.add(thread)

            # Update active threads
            active_threads = still_active

            # Process any results
            while not result_queue.empty():
                status, data, p_num = result_queue.get()
                if status == "success":
                    parts.append(data)
                    if options.get("onProgress"):
                        percentage = (len(parts) * 100) / chunk_amount
                        limited_percentage = min(percentage, 100)
                        rounded_percentage = round(limited_percentage, 2)
                        options["onProgress"](rounded_percentage)
                else:
                    error = ValueError(f"Error uploading part {p_num}: {data}")

            if error:
                raise error

            time.sleep(0.2)

        # One final check for results
        while not result_queue.empty():
            status, data, p_num = result_queue.get()
            if status == "success":
                parts.append(data)
            else:
                raise ValueError(f"Error uploading part {p_num}: {data}")

        self._is_canceled(cancelled)

        if len(parts) != chunk_amount:
            raise ValueError(f"Expected {chunk_amount} parts but got {len(parts)}")

        # Complete the multipart upload with retries
        for i in range(3):
            try:
                return self._completeMultipartUpload(filename, upload_id, parts, options)
            except Exception as ex:
                if is_limit_error(ex):
                    raise ValueError(str(ex)) from ex
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
