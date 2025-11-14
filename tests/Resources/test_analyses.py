import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisCreateInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisInfo
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisListItem
from tagoio_sdk.modules.Resources.Analysis_Types import ScriptFile
from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockAnalysisList() -> list[AnalysisListItem]:
    return {
        "status": True,
        "result": [
            {
                "id": "analysis_id",
                "name": "Analysis Name",
                "created_at": "2023-03-07T01:43:45.952Z",
                "updated_at": "2023-03-07T01:43:45.952Z",
                "last_run": "2023-03-07T01:43:45.952Z",
            }
        ],
    }


def mockAnalysisInfo() -> AnalysisInfo:
    return {
        "status": True,
        "result": {
            "id": "analysis_id",
            "name": "Analysis Name",
            "created_at": "2023-03-07T01:43:45.952Z",
            "updated_at": "2023-03-07T01:43:45.952Z",
            "last_run": "2023-03-07T01:43:45.952Z",
        },
    }


def mockCreateAnalysis() -> dict:
    return {"status": True, "result": {"id": "analysis_id", "token": "analysis_token"}}


def testAnalysesMethodList(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get("https://api.tago.io/analysis/", json=mockAnalysisList())

    resources = Resources()
    response = resources.analysis.list()

    assert response[0]["name"] == mockAnalysisList()["result"][0]["name"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testAnalysesMethodCreate(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    analysis_data = AnalysisCreateInfo(name="New Analysis")
    requests_mock.post("https://api.tago.io/analysis", json=mockCreateAnalysis())

    resources = Resources()
    response = resources.analysis.create(analysis_data)

    assert response == mockCreateAnalysis()["result"]
    assert isinstance(response, dict)


def testAnalysesMethodEdit(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    analysis_data = AnalysisInfo(name="Updated Analysis")
    requests_mock.put(
        "https://api.tago.io/analysis/analysis_id",
        json={"status": True, "result": "success"},
    )

    resources = Resources()
    response = resources.analysis.edit("analysis_id", analysis_data)

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodDelete(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.delete(
        "https://api.tago.io/analysis/analysis_id",
        json={"status": True, "result": "success"},
    )

    resources = Resources()
    response = resources.analysis.delete("analysis_id")

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodInfo(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get(
        "https://api.tago.io/analysis/analysis_id", json=mockAnalysisInfo()
    )

    resources = Resources()
    response = resources.analysis.info("analysis_id")

    assert response["id"] == mockAnalysisInfo()["result"]["id"]
    assert isinstance(response, dict)


def testAnalysesMethodRun(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.post(
        "https://api.tago.io/analysis/analysis_id/run",
        json={"status": True, "result": {"token": "run_token"}},
    )

    resources = Resources()
    response = resources.analysis.run("analysis_id")

    assert response == {"token": "run_token"}
    assert isinstance(response, dict)


def testAnalysesMethodTokenGenerate(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get(
        "https://api.tago.io/analysis/analysis_id/token",
        json={"status": True, "result": {"token": "new_token"}},
    )

    resources = Resources()
    response = resources.analysis.tokenGenerate("analysis_id")

    assert response == {"token": "new_token"}
    assert isinstance(response, dict)


def testAnalysesMethodUploadScript(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    script_file = ScriptFile(
        name="script.js", language="node", content="console.log('Hello, World!');"
    )
    requests_mock.post(
        "https://api.tago.io/analysis/analysis_id/upload",
        json={"status": True, "result": "success"},
    )

    resources = Resources()
    response = resources.analysis.uploadScript("analysis_id", script_file)

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodDownloadScript(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get(
        "https://api.tago.io/analysis/analysis_id/download",
        json={"status": True, "result": {"url": "https://download.url"}},
    )

    resources = Resources()
    response = resources.analysis.downloadScript("analysis_id")

    assert response == {"url": "https://download.url"}
    assert isinstance(response, dict)


def testAnalysesMethodListSnippets(requests_mock: Mocker) -> None:
    """
    Test listSnippets method to retrieve all available snippets for a runtime.
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    mock_snippets_response = {
        "runtime": "python-rt2025",
        "schema_version": 1,
        "generated_at": "2025-01-13T12:00:00Z",
        "snippets": [
            {
                "id": "console-example",
                "title": "Console Example",
                "description": "Basic console logging example",
                "language": "python",
                "tags": ["basics", "logging"],
                "filename": "console.py",
                "file_path": "python-rt2025/console.py",
            },
            {
                "id": "data-processing",
                "title": "Data Processing",
                "description": "Process device data",
                "language": "python",
                "tags": ["data", "processing"],
                "filename": "process-data.py",
                "file_path": "python-rt2025/process-data.py",
            },
        ],
    }

    requests_mock.get(
        "https://snippets.tago.io/python-rt2025.json", json=mock_snippets_response
    )

    resources = Resources()
    response = resources.analysis.listSnippets("python-rt2025")

    assert response["runtime"] == "python-rt2025"
    assert response["schema_version"] == 1
    assert len(response["snippets"]) == 2
    assert response["snippets"][0]["id"] == "console-example"
    assert response["snippets"][0]["title"] == "Console Example"
    assert isinstance(response, dict)
    assert isinstance(response["snippets"], list)


def testAnalysesMethodGetSnippetFile(requests_mock: Mocker) -> None:
    """
    Test getSnippetFile method to retrieve raw snippet file content.
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    mock_file_content = """# Console Example
from tagoio_sdk import Analysis

def my_analysis(context):
    context.log("Hello from Python snippet!")

Analysis(my_analysis)
"""

    requests_mock.get(
        "https://snippets.tago.io/python-rt2025/console.py", text=mock_file_content
    )

    resources = Resources()
    response = resources.analysis.getSnippetFile("python-rt2025", "console.py")

    assert "Console Example" in response
    assert "context.log" in response
    assert isinstance(response, str)


def testAnalysesMethodListSnippetsError(requests_mock: Mocker) -> None:
    """
    Test listSnippets method error handling when request fails.
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get("https://snippets.tago.io/invalid-runtime.json", status_code=404)

    resources = Resources()

    try:
        resources.analysis.listSnippets("invalid-runtime")
        raise AssertionError("Expected RuntimeError to be raised")
    except RuntimeError as e:
        assert "Failed to fetch snippets" in str(e)


def testAnalysesMethodGetSnippetFileError(requests_mock: Mocker) -> None:
    """
    Test getSnippetFile method error handling when file not found.
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get(
        "https://snippets.tago.io/python-rt2025/nonexistent.py", status_code=404
    )

    resources = Resources()

    try:
        resources.analysis.getSnippetFile("python-rt2025", "nonexistent.py")
        raise AssertionError("Expected RuntimeError to be raised")
    except RuntimeError as e:
        assert "Failed to fetch snippet file" in str(e)
