import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Analysis_Types import AnalysisCreateInfo, AnalysisInfo, ScriptFile, AnalysisListItem

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
        ]
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
        }
    }


def mockCreateAnalysis() -> dict:
    return {
        "status": True,
        "result": {
            "id": "analysis_id",
            "token": "analysis_token"
        }
    }


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
    requests_mock.put("https://api.tago.io/analysis/analysis_id", json={"status": True, "result": "success"})

    resources = Resources()
    response = resources.analysis.edit("analysis_id", analysis_data)

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodDelete(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.delete("https://api.tago.io/analysis/analysis_id", json={"status": True, "result": "success"})

    resources = Resources()
    response = resources.analysis.delete("analysis_id")

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodInfo(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get("https://api.tago.io/analysis/analysis_id", json=mockAnalysisInfo())

    resources = Resources()
    response = resources.analysis.info("analysis_id")

    assert response["id"] == mockAnalysisInfo()["result"]["id"]
    assert isinstance(response, dict)


def testAnalysesMethodRun(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.post("https://api.tago.io/analysis/analysis_id/run", json={"status": True, "result": {"token": "run_token"}})

    resources = Resources()
    response = resources.analysis.run("analysis_id")

    assert response == {"token": "run_token"}
    assert isinstance(response, dict)


def testAnalysesMethodTokenGenerate(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get("https://api.tago.io/analysis/analysis_id/token", json={"status": True, "result": {"token": "new_token"}})

    resources = Resources()
    response = resources.analysis.tokenGenerate("analysis_id")

    assert response == {"token": "new_token"}
    assert isinstance(response, dict)


def testAnalysesMethodUploadScript(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    script_file = ScriptFile(name="script.js", language="node", content="console.log('Hello, World!');")
    requests_mock.post("https://api.tago.io/analysis/analysis_id/upload", json={"status": True, "result": "success"})

    resources = Resources()
    response = resources.analysis.uploadScript("analysis_id", script_file)

    assert response == "success"
    assert isinstance(response, str)


def testAnalysesMethodDownloadScript(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    requests_mock.get("https://api.tago.io/analysis/analysis_id/download", json={"status": True, "result": {"url": "https://download.url"}})

    resources = Resources()
    response = resources.analysis.downloadScript("analysis_id")

    assert response == {"url": "https://download.url"}
    assert isinstance(response, dict)
