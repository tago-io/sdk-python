import os
from typing import Dict
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Files_Types import FileListInfo

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockFileList() -> FileListInfo:
    return {
        "status": True,
        "result": {
            "total": 200,
            "usage": 0.05,
            "files": [
                {"filename": "document.pdf", "size": 7812, "last_modified": "2023-02-21T15:17:35.759Z"},
                {"filename": "image.jpg", "size": 12345, "last_modified": "2023-02-22T10:30:20.123Z"},
            ],
            "folders": ["folder1", "folder2"],
        },
    }


def mockUploadBase64() -> Dict[str, str]:
    return {"status": True, "result": "Files successfully uploaded"}


def mockCheckPermission() -> Dict[str, bool]:
    return {"status": True, "result": {"public": True}}


def mockFileURLSigned() -> Dict[str, str]:
    return {"status": True, "result": "https://storage.tago.io/file/signed/path/file.txt?token=abc123"}


def mockFileMD5() -> Dict[str, str]:
    return {"status": True, "result": "d41d8cd98f00b204e9800998ecf8427e"}


def mockMultipartStart() -> Dict[str, str]:
    return {"status": True, "result": "upload_id_123456"}


def mockMultipartUpload() -> Dict[str, str]:
    return {"status": True, "result": {"ETag": "part_etag_123"}}


def mockMultipartComplete() -> Dict[str, str]:
    return {"status": True, "result": {"file": "https://api.tago.io/file/path/to/uploaded_file.txt"}}


def testFilesMethodList(requests_mock: Mocker) -> None:
    """Test list method of Files class."""
    mock_response = mockFileList()
    requests_mock.get("https://api.tago.io/files", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {"path": "/my/folder", "quantity": 100}

    result = resources.files.list(query)

    # Check if result has expected properties
    assert "total" in result
    assert "usage" in result
    assert "files" in result
    assert "folders" in result

    # Check specific values
    assert result["total"] == 200
    assert result["usage"] == 0.05
    assert len(result["files"]) == 2
    assert len(result["folders"]) == 2
    assert result["files"][0]["filename"] == "document.pdf"
    assert result["files"][0]["size"] == 7812


def testFilesMethodUploadBase64(requests_mock: Mocker) -> None:
    """Test uploadBase64 method of Files class."""
    mock_response = mockUploadBase64()
    requests_mock.post("https://api.tago.io/files", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    files_to_upload = [{"filename": "/my-files/document.pdf", "file": "base64EncodedContent", "public": True}]

    result = resources.files.uploadBase64(files_to_upload)

    # Check if result has expected message
    assert result == "Files successfully uploaded"


def testFilesMethodMove(requests_mock: Mocker) -> None:
    """Test move method of Files class."""
    mock_response = {"status": True, "result": "Successfully Updated"}

    requests_mock.put("https://api.tago.io/files", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    files_to_move = [{"_from": "/old/path/file.txt", "to": "/new/path/renamed.txt"}]

    result = resources.files.move(files_to_move)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testFilesMethodCopy(requests_mock: Mocker) -> None:
    """Test copy method of Files class."""
    mock_response = {"status": True, "result": "Successfully Copied"}

    requests_mock.put("https://api.tago.io/files/copy", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    files_to_copy = [{"_from": "/source/file.txt", "to": "/destination/copy.txt"}]

    result = resources.files.copy(files_to_copy)

    # Check if result has expected message
    assert result == "Successfully Copied"


def testFilesMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Files class."""
    mock_response = {"status": True, "result": "Successfully Removed"}

    requests_mock.delete("https://api.tago.io/files", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    files_to_delete = ["/path/to/file.txt", "/folder/to/delete"]

    result = resources.files.delete(files_to_delete)

    # Check if result has expected message
    assert result == "Successfully Removed"


def testFilesMethodCheckPermission(requests_mock: Mocker) -> None:
    """Test checkPermission method of Files class."""
    mock_response = mockCheckPermission()
    requests_mock.get("https://api.tago.io/files/permission", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.files.checkPermission("/path/to/file.txt")

    # Check if result has expected properties
    assert "public" in result
    assert result["public"] is True


def testFilesMethodChangePermission(requests_mock: Mocker) -> None:
    """Test changePermission method of Files class."""
    mock_response = {"status": True, "result": "Successfully Updated"}

    requests_mock.put("https://api.tago.io/files/permission", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    files_visibility = [{"file": "/path/to/file.txt", "public": True}]

    result = resources.files.changePermission(files_visibility)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testFilesMethodGetFileURLSigned(requests_mock: Mocker) -> None:
    """Test getFileURLSigned method of Files class."""
    mock_response = mockFileURLSigned()
    file_path = "/path/to/file.txt"

    # Mock the URL with a path that would be extracted by _getPathFromUrl
    requests_mock.get(f"https://api.tago.io/file{file_path}", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    # The class would extract this path from the URL
    mock_url = f"https://api.tago.io/file{file_path}"
    result = resources.files.getFileURLSigned(mock_url)

    # Check if result returns expected URL
    assert result == "https://storage.tago.io/file/signed/path/file.txt?token=abc123"


def testFilesMethodGetFileMD5(requests_mock: Mocker) -> None:
    """Test getFileMD5 method of Files class."""
    mock_response = mockFileMD5()
    file_path = "/path/to/file.txt"

    # Mock the URL with a path that would be extracted by _getPathFromUrl
    requests_mock.get(f"https://api.tago.io/file{file_path}", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    # The class would extract this path from the URL
    mock_url = f"https://api.tago.io/file{file_path}"
    result = resources.files.getFileMD5(mock_url)

    # Check if result returns expected MD5 hash
    assert result == "d41d8cd98f00b204e9800998ecf8427e"


def testFilesMethodUploadFile(requests_mock: Mocker) -> None:
    """Test uploadFile method of Files class."""
    # Mock the three API calls made during an upload
    requests_mock.post(
        "https://api.tago.io/files",
        [
            {"json": {"status": True, "result": "upload_id_123456"}, "status_code": 200},
            {"json": {"status": True, "result": {"ETag": "part_etag_123"}}, "status_code": 200},
            {
                "json": {"status": True, "result": {"file": "https://api.tago.io/file/path/to/uploaded_file.txt"}},
                "status_code": 200,
            },
        ],
    )

    resources = Resources({"token": "your_token_value"})

    # Create a small file for testing
    file_data = b"This is a test file content"
    filename = "/uploads/test_file.txt"

    # Mock onProgress callback
    progress_values = []

    def on_progress(progress):
        progress_values.append(progress)

    # Upload the file
    result = resources.files.uploadFile(file_data, filename, {"onProgress": on_progress})

    # Check if result has expected properties
    assert "file" in result
    assert result["file"] == "https://api.tago.io/file/path/to/uploaded_file.txt"

    # Check that progress was reported
    assert len(progress_values) > 0
    assert progress_values[-1] == 100.0
