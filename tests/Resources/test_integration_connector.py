import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.IntegrationConnector import Connectors

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockListConnectors() -> dict:
    return {
        "status": True,
        "result": [
            {
                "id": "connector_id_1",
                "name": "Connector 1",
                "public": True,
                "created_at": "2023-01-01T00:00:00.000Z",
                "updated_at": "2023-01-01T00:00:00.000Z",
            },
            {
                "id": "connector_id_2",
                "name": "Connector 2",
                "public": False,
                "created_at": "2023-01-02T00:00:00.000Z",
                "updated_at": "2023-01-02T00:00:00.000Z",
            },
        ],
    }


def mockConnectorInfo() -> dict:
    return {
        "status": True,
        "result": {
            "id": "connector_id_1",
            "name": "Connector 1",
            "public": True,
            "description": "Test connector description",
            "logo_url": "https://example.com/logo.png",
            "networks": ["network_id_1", "network_id_2"],
            "created_at": "2023-01-01T00:00:00.000Z",
            "updated_at": "2023-01-01T00:00:00.000Z",
            "enabled": True,
            "type": "custom",
            "install_text": "Installation instructions",
            "install_end_text": "Installation complete",
            "device_annotation": "Device annotation",
        },
    }


def mockCreateConnector() -> dict:
    return {"status": True, "result": {"connector": "new_connector_id"}}


def testConnectorsMethodList(requests_mock: Mocker) -> None:
    """Test list method of Connectors class."""
    mock_response = mockListConnectors()
    requests_mock.get("https://api.tago.io/integration/connector/", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.integration.connectors.list()

    # Check if result has expected structure
    assert len(result) == 2
    assert result[0]["id"] == "connector_id_1"
    assert result[1]["id"] == "connector_id_2"

    # Test with query parameters
    query = {
        "page": 2,
        "fields": ["id", "name", "public"],
        "amount": 15,
        "orderBy": ["name", "desc"],
        "filter": {"name": "Test"},
    }

    requests_mock.get("https://api.tago.io/integration/connector/", json=mock_response)
    resources.integration.connectors.list(query)

    # We're just checking if the call works with parameters


def testConnectorsMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Connectors class."""
    mock_response = mockConnectorInfo()
    requests_mock.get("https://api.tago.io/integration/connector/connector_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.integration.connectors.info("connector_id_1")

    # Check if result has expected structure
    assert result["id"] == "connector_id_1"
    assert result["name"] == "Connector 1"
    assert result["description"] == "Test connector description"
    assert len(result["networks"]) == 2


def testConnectorsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Connectors class."""
    mock_response = mockCreateConnector()
    requests_mock.post("https://api.tago.io/integration/connector/", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    connector_data = {"name": "New Connector", "type": "custom", "networks": ["network_id_1"], "enabled": True}

    result = resources.integration.connectors.create(connector_data)

    # Check if result has expected structure
    assert result["connector"] == "new_connector_id"


def testConnectorsMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Connectors class."""
    mock_response = {"status": True, "result": "Connector Successfully Updated"}
    requests_mock.put("https://api.tago.io/integration/connector/connector_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    edit_data = {"name": "Updated Connector Name", "description": "Updated description"}

    result = resources.integration.connectors.edit("connector_id_1", edit_data)

    # Check if result has expected structure
    assert result == "Connector Successfully Updated"


def testConnectorsMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Connectors class."""
    mock_response = {"status": True, "result": "Connector Successfully Deleted"}
    requests_mock.delete("https://api.tago.io/integration/connector/connector_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.integration.connectors.delete("connector_id_1")

    # Check if result has expected structure
    assert result == "Connector Successfully Deleted"
