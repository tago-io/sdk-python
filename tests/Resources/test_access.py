import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Access_Types import AccessInfo

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockAccessList() -> list[AccessInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "access_id_1",
                "name": "Access Policy 1",
                "active": True,
                "permissions": [
                    {
                        "effect": "allow",
                        "action": ["access"],
                        "resource": ["access_management"],
                    }
                ],
                "targets": [],
                "tags": [{"key": "type", "value": "admin"}],
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
            },
            {
                "id": "access_id_2",
                "name": "Access Policy 2",
                "active": True,
                "permissions": [
                    {
                        "effect": "allow",
                        "action": ["edit"],
                        "resource": ["access_management"],
                    }
                ],
                "targets": [],
                "tags": [{"key": "type", "value": "user"}],
                "created_at": "2023-02-21T16:17:35.759Z",
                "updated_at": "2023-02-21T16:17:35.759Z",
            },
        ],
    }


def mockAccessInfo() -> AccessInfo:
    return {
        "status": True,
        "result": {
            "id": "access_id_1",
            "name": "Access Policy 1",
            "active": True,
            "permissions": [
                {
                    "effect": "allow",
                    "action": ["access"],
                    "resource": ["access_management"],
                }
            ],
            "targets": [],
            "tags": [{"key": "type", "value": "admin"}],
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
        },
    }


def mockCreateAccess() -> dict:
    return {
        "status": True,
        "result": {"am_id": "access_id_new"},
    }


def testAccessMethodList(requests_mock: Mocker) -> None:
    """Test list method of Access class."""
    mock_response = mockAccessList()
    requests_mock.get("https://api.tago.io/am", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["id", "name", "tags"],
        "amount": 20,
        "orderBy": ["name", "asc"],
    }

    result = resources.access.list(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "access_id_1"
    assert result[1]["id"] == "access_id_2"


def testAccessMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Access class."""
    mock_response = mockCreateAccess()
    requests_mock.post("https://api.tago.io/am", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    access_data = {
        "name": "New Access Policy",
        "active": True,
        "permissions": [
            {
                "effect": "allow",
                "action": ["access"],
                "resource": ["access_management"],
            }
        ],
        "targets": [],
        "tags": [{"key": "type", "value": "admin"}],
    }

    result = resources.access.create(access_data)

    # Check if result has expected structure
    assert result["am_id"] == "access_id_new"


def testAccessMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Access class."""
    mock_response = {
        "status": True,
        "result": "Access Management Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/am/access_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    access_data = {
        "name": "Updated Access Policy",
        "permissions": [
            {
                "effect": "allow",
                "action": ["edit"],
                "resource": ["access_management"],
            }
        ],
        "tags": [{"key": "type", "value": "user"}],
    }

    result = resources.access.edit("access_id_1", access_data)

    # Check if result has expected message
    assert result == "Access Management Successfully Updated"


def testAccessMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Access class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/am/access_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.access.delete("access_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"


def testAccessMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Access class."""
    mock_response = mockAccessInfo()
    requests_mock.get("https://api.tago.io/am/access_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.access.info("access_id_1")

    # Check if result has expected properties
    assert result["id"] == "access_id_1"
    assert result["name"] == "Access Policy 1"
    assert result["active"] == True
    assert len(result["permissions"]) == 1
    assert result["permissions"][0]["effect"] == "allow"
    assert "access" in result["permissions"][0]["action"]
    assert "access_management" in result["permissions"][0]["resource"]
