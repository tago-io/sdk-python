import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Secrets_Type import SecretsInfo

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockSecretsList() -> list[SecretsInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "secret_id_1",
                "key": "API_KEY",
                "value_length": 32,
                "tags": [{"key": "type", "value": "api"}],
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
            },
            {
                "id": "secret_id_2",
                "key": "DB_PASSWORD",
                "value_length": 16,
                "tags": [{"key": "type", "value": "database"}],
                "created_at": "2023-02-22T10:30:45.123Z",
                "updated_at": "2023-02-22T10:30:45.123Z",
            },
        ],
    }


def mockSecretInfo() -> SecretsInfo:
    return {
        "status": True,
        "result": {
            "id": "secret_id_1",
            "key": "API_KEY",
            "value_length": 32,
            "tags": [{"key": "type", "value": "api"}],
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
        },
    }


def mockCreateSecret() -> dict:
    return {
        "status": True,
        "result": {"id": "new_secret_id"},
    }


def testSecretsMethodList(requests_mock: Mocker) -> None:
    """Test list method of Secrets class."""
    mock_response = mockSecretsList()
    requests_mock.get("https://api.tago.io/secrets", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["id", "key", "tags"],
        "amount": 20,
        "orderBy": ["key", "asc"],
    }

    result = resources.secrets.list(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["id"] == "secret_id_1"
    assert result[0]["key"] == "API_KEY"
    assert result[1]["id"] == "secret_id_2"
    assert result[1]["key"] == "DB_PASSWORD"
    assert result[0]["tags"][0]["key"] == "type"
    assert result[0]["tags"][0]["value"] == "api"


def testSecretsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Secrets class."""
    mock_response = mockCreateSecret()
    requests_mock.post("https://api.tago.io/secrets", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    secret_data = {
        "key": "NEW_API_KEY",
        "value": "secret_value_123",
        "tags": [{"key": "type", "value": "api"}],
    }

    result = resources.secrets.create(secret_data)

    # Check if result has expected structure
    assert result["id"] == "new_secret_id"


def testSecretsMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Secrets class."""
    mock_response = mockSecretInfo()
    requests_mock.get("https://api.tago.io/secrets/secret_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.secrets.info("secret_id_1")

    # Check if result has expected properties
    assert result["id"] == "secret_id_1"
    assert result["key"] == "API_KEY"
    assert result["value_length"] == 32
    assert len(result["tags"]) == 1
    assert result["tags"][0]["key"] == "type"
    assert result["tags"][0]["value"] == "api"


def testSecretsMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Secrets class."""
    mock_response = {
        "status": True,
        "result": "Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/secrets/secret_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    secret_data = {
        "value": "new_secret_value",
        "tags": [{"key": "environment", "value": "production"}],
    }

    result = resources.secrets.edit("secret_id_1", secret_data)

    # Check if result has expected message
    assert result == "Successfully Updated"


def testSecretsMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Secrets class."""
    mock_response = {
        "status": True,
        "result": "Successfully Removed",
    }

    requests_mock.delete("https://api.tago.io/secrets/secret_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.secrets.delete("secret_id_1")

    # Check if result has expected message
    assert result == "Successfully Removed"
