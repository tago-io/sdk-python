import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.common.Common_Type import TokenDataList, TokenData
from tagoio_sdk.modules.Resources.Service_Authorization_Types import TokenCreateResponse

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockTokenList() -> list[TokenDataList]:
    return {
        "status": True,
        "result": [
            {
                "token": "token_id_1",
                "name": "Service Token 1",
                "permission": "full",
                "verification_code": "abc123",
                "created_at": "2023-02-21T15:17:35.759Z",
                "last_authorization": "2023-02-22T10:30:45.123Z",
                "expire_time": "never",
            },
            {
                "token": "token_id_2",
                "name": "Service Token 2",
                "permission": "read",
                "verification_code": "def456",
                "created_at": "2023-03-15T08:22:17.432Z",
                "last_authorization": "2023-03-16T14:05:22.789Z",
                "expire_time": "2024-03-15T08:22:17.432Z",
            },
        ],
    }


def mockTokenCreate() -> dict:
    return {
        "status": True,
        "result": {
            "token": "new_token_id",
            "name": "New Service Token",
            "profile": "profile_id_123",
            "additional_parameters": "verification_code_789",
        },
    }


def testServiceAuthorizationMethodTokenList(requests_mock: Mocker) -> None:
    """Test tokenList method of ServiceAuthorization class."""
    mock_response = mockTokenList()
    requests_mock.get("https://api.tago.io/serviceauth", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    query = {
        "page": 1,
        "fields": ["name", "token", "permission"],
        "amount": 20,
        "orderBy": ["name", "asc"],
    }

    result = resources.serviceAuthorization.tokenList(query)

    # Check if the result is a list
    assert isinstance(result, list)
    # Check if the result has the expected items
    assert len(result) == 2
    # Check if items have expected properties
    assert result[0]["token"] == "token_id_1"
    assert result[0]["name"] == "Service Token 1"
    assert result[0]["permission"] == "full"
    assert result[1]["token"] == "token_id_2"
    assert result[1]["name"] == "Service Token 2"


def testServiceAuthorizationMethodTokenCreate(requests_mock: Mocker) -> None:
    """Test tokenCreate method of ServiceAuthorization class."""
    mock_response = mockTokenCreate()
    requests_mock.post("https://api.tago.io/serviceauth", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    token_data = {
        "name": "New Service Token",
        "verification_code": "verification_code_789",
        "permission": "full",
    }

    result = resources.serviceAuthorization.tokenCreate(token_data)

    # Check if result has expected structure
    assert result["token"] == "new_token_id"
    assert result["name"] == "New Service Token"
    assert result["profile"] == "profile_id_123"
    assert result["additional_parameters"] == "verification_code_789"


def testServiceAuthorizationMethodTokenDelete(requests_mock: Mocker) -> None:
    """Test tokenDelete method of ServiceAuthorization class."""
    mock_response = {"status": True, "result": "Token Successfully Removed"}
    requests_mock.delete("https://api.tago.io/serviceauth/token_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.serviceAuthorization.tokenDelete("token_id_1")

    # Check if result has expected message
    assert result == "Token Successfully Removed"


def testServiceAuthorizationMethodTokenEdit(requests_mock: Mocker) -> None:
    """Test tokenEdit method of ServiceAuthorization class."""
    mock_response = {"status": True, "result": "Authorization Code Successfully Updated"}
    requests_mock.put("https://api.tago.io/serviceauth/token_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.serviceAuthorization.tokenEdit("token_id_1", "new_verification_code")

    # Check if result has expected message
    assert result == "Authorization Code Successfully Updated"
