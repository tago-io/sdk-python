from typing import Any
from typing import Dict

from requests_mock.mocker import Mocker
from src.tagoio_sdk.modules.Resources.IntegrationNetwork import Networks


def mockListNetwork() -> Dict[str, Any]:
    """Mock to return the list of NetworkInfo."""
    return {
        "status": True,
        "result": [
            {"id": "60af66df0ae39d0012b0bbe9", "name": "AWS IoT"},
            {"id": "5d48632019b67f001c874a6b", "name": "BeWhere"},
        ],
    }


def mockNetworkInfo() -> Dict[str, Any]:
    """Mock to return the object NetworkInfo."""
    return {
        "status": True,
        "result": {
            "id": "5ede22a7427104001c248b08",
            "name": "LoRaWAN Activity",
            "profile": "5bbcb03b667d7a002e56664b",
            "middleware_endpoint": "https://lorawan.tago.io",
        },
    }


def mockNetworkCreate() -> Dict[str, Any]:
    """Mock to return network create response."""
    return {
        "status": True,
        "result": {"network": "network-id-123"},
    }


def mockNetworkEdit() -> Dict[str, Any]:
    """Mock to return network edit response."""
    return {
        "status": True,
        "result": "Successfully Updated",
    }


def mockNetworkDelete() -> Dict[str, Any]:
    """Mock to return network delete response."""
    return {
        "status": True,
        "result": "Successfully Removed",
    }


def mockNetworkTokenList() -> Dict[str, Any]:
    """Mock to return list of network tokens."""
    return {
        "status": True,
        "result": [
            {
                "token": "token-123",
                "name": "Default Token",
                "permission": "full",
                "created_at": "2025-01-09T10:00:00.000Z",
            },
            {
                "token": "token-456",
                "name": "Read-Only Token",
                "permission": "read",
                "created_at": "2025-01-08T15:30:00.000Z",
            },
        ],
    }


def mockNetworkTokenCreate() -> Dict[str, Any]:
    """Mock to return token create response."""
    return {
        "status": True,
        "result": {
            "token": "new-token-value",
            "expire_date": None,
        },
    }


def mockNetworkTokenDelete() -> Dict[str, Any]:
    """Mock to return token delete response."""
    return {
        "status": True,
        "result": "Successfully Removed",
    }


def testNetworksMethodListNetworks(requests_mock: Mocker):
    """Test listNetwork method with pagination."""
    requests_mock.get("https://api.tago.io/integration/network", json=mockListNetwork())

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).listNetwork(queryObj={"amount": 100})

    assert response == mockListNetwork()["result"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testNetworksMethodInfo(requests_mock: Mocker):
    """Test info method to retrieve network details."""
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}", json=mockNetworkInfo()
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).info(networkID=networkID)

    assert response == mockNetworkInfo()["result"]
    assert isinstance(response, dict)


def testNetworksMethodCreate(requests_mock: Mocker):
    """Test create method to create a new network."""
    requests_mock.post("https://api.tago.io/integration/network", json=mockNetworkCreate())

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).create(
        {
            "name": "My Custom Network",
            "description": "Custom integration network",
            "middleware_endpoint": "https://my-middleware.com/endpoint",
            "public": False,
        }
    )

    assert response == mockNetworkCreate()["result"]
    assert isinstance(response, dict)
    assert "network" in response


def testNetworksMethodEdit(requests_mock: Mocker):
    """Test edit method to update network properties."""
    networkID = "network-id-123"
    requests_mock.put(
        f"https://api.tago.io/integration/network/{networkID}", json=mockNetworkEdit()
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).edit(
        networkID,
        {
            "name": "Updated Network Name",
            "description": "Updated description",
            "public": True,
        },
    )

    assert response == mockNetworkEdit()["result"]
    assert response == "Successfully Updated"


def testNetworksMethodDelete(requests_mock: Mocker):
    """Test delete method to remove a network."""
    networkID = "network-id-123"
    requests_mock.delete(
        f"https://api.tago.io/integration/network/{networkID}", json=mockNetworkDelete()
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).delete(networkID)

    assert response == mockNetworkDelete()["result"]
    assert response == "Successfully Removed"


def testNetworksMethodTokenList(requests_mock: Mocker):
    """Test tokenList method to retrieve network tokens."""
    networkID = "network-id-123"
    requests_mock.get(
        f"https://api.tago.io/integration/network/token/{networkID}",
        json=mockNetworkTokenList(),
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).tokenList(
        networkID,
        {
            "page": 1,
            "amount": 20,
            "fields": ["name", "token", "permission"],
            "orderBy": ["created_at", "desc"],
        },
    )

    # dateParserList converts created_at strings to datetime objects
    assert isinstance(response, list)
    assert len(response) == 2
    assert response[0]["token"] == "token-123"
    assert response[0]["name"] == "Default Token"
    assert response[0]["permission"] == "full"


def testNetworksMethodTokenCreate(requests_mock: Mocker):
    """Test tokenCreate method to generate a new token."""
    requests_mock.post(
        "https://api.tago.io/integration/network/token", json=mockNetworkTokenCreate()
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).tokenCreate(
        "network-id-123",
        {
            "name": "Production Token",
            "permission": "write",
            "expire_time": "never",
        },
    )

    assert response == mockNetworkTokenCreate()["result"]
    assert isinstance(response, dict)
    assert "token" in response


def testNetworksMethodTokenDelete(requests_mock: Mocker):
    """Test tokenDelete method to remove a token."""
    token = "token-to-delete"
    requests_mock.delete(
        f"https://api.tago.io/integration/network/token/{token}",
        json=mockNetworkTokenDelete(),
    )

    tokenFake = {"token": "fake_token"}
    response = Networks(params=tokenFake).tokenDelete(token)

    assert response == mockNetworkTokenDelete()["result"]
    assert response == "Successfully Removed"
