import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Actions_Types import ActionInfo

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockActionList() -> list[ActionInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "action_id_1",
                "name": "Action 1",
                "active": True,
                "type": "condition",
                "action": {"script": ["analysis_id_1"], "type": "script"},
                "tags": [{"key": "type", "value": "notification"}],
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
                "last_triggered": "2023-02-21T15:17:35.759Z",
            },
            {
                "id": "action_id_2",
                "name": "Action 2",
                "active": True,
                "type": "condition",
                "action": {"script": ["analysis_id_2"], "type": "script"},
                "tags": [{"key": "type", "value": "alert"}],
                "created_at": "2023-02-21T16:17:35.759Z",
                "updated_at": "2023-02-21T16:17:35.759Z",
                "last_triggered": "2023-02-21T16:17:35.759Z",
            },
        ],
    }


def mockActionInfo() -> ActionInfo:
    return {
        "status": True,
        "result": {
            "id": "action_id_1",
            "name": "Action 1",
            "active": True,
            "type": "condition",
            "action": {"script": ["analysis_id_1"], "type": "script"},
            "tags": [{"key": "type", "value": "notification"}],
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
            "last_triggered": "2023-02-21T15:17:35.759Z",
        },
    }


def mockCreateAction() -> dict:
    return {
        "status": True,
        "result": {"action": "action_id_new"},
    }


def testActionsMethodList(requests_mock: Mocker) -> None:
    """Test list method of Actions class."""
    mock_response = mockActionList()
    requests_mock.get("https://api.tago.io/action", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["id", "name", "tags"],
        "amount": 20,
        "orderBy": ["name", "asc"],
    }

    result = resources.actions.list(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "action_id_1"
    assert result[1]["id"] == "action_id_2"


def testActionsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Actions class."""
    mock_response = mockCreateAction()
    requests_mock.post("https://api.tago.io/action", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    action_data = {
        "name": "New Action",
        "active": True,
        "type": "condition",
        "action": {"script": ["analysis_id_3"], "type": "script"},
        "tags": [{"key": "type", "value": "notification"}],
    }

    result = resources.actions.create(action_data)

    # Check if result has expected structure
    assert result["action"] == "action_id_new"


def testActionsMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Actions class."""
    mock_response = {
        "status": True,
        "result": "Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/action/action_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    action_data = {
        "name": "Updated Action",
        "active": False,
        "tags": [{"key": "type", "value": "alert"}],
    }

    result = resources.actions.edit("action_id_1", action_data)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testActionsMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Actions class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/action/action_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.actions.delete("action_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testActionsMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Actions class."""
    mock_response = mockActionInfo()
    requests_mock.get("https://api.tago.io/action/action_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.actions.info("action_id_1")

    # Check if result has expected properties
    assert result["id"] == "action_id_1"
    assert result["name"] == "Action 1"
    assert result["active"] == True
    assert result["type"] == "condition"
    assert result["action"]["type"] == "script"
    assert "analysis_id_1" in result["action"]["script"]
    assert len(result["tags"]) == 1
    assert result["tags"][0]["key"] == "type"
    assert result["tags"][0]["value"] == "notification"
