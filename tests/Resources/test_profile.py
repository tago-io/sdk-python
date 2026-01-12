import os

from requests_mock.mocker import Mocker

from tagoio_sdk.common.Common_Type import TokenDataList
from tagoio_sdk.modules.Resources.Profile_Type import ProfileInfo
from tagoio_sdk.modules.Resources.Profile_Type import ProfileSummary
from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockProfileInfo() -> ProfileInfo:
    return {
        "status": True,
        "result": {
            "info": {
                "id": "profile_id",
                "account": "account_profile_id",
                "name": "tago.io",
                "logo_url": None,
                "banner_url": None,
                "created_at": "2023-02-21T15:17:35.880Z",
                "updated_at": "2023-02-21T15:17:35.880Z",
            },
            "allocation": {
                "input": 1000000,
                "output": 3000000,
                "analysis": 3000,
                "data_records": 800000,
                "sms": 10,
                "email": 100,
                "run_users": 10,
                "push_notification": 100,
                "file_storage": 200,
            },
            "account_plan": "free",
            "addons": {"custom_dns": False, "mobile": False},
        },
    }


def mockListProfileInfo() -> list[ProfileInfo]:
    return {
        "status": True,
        "result": [
            {"id": "profile_id", "name": "tago.io", "logo_url": None},
            {
                "account": "account_profile_id",
                "profile": "profile_profile_id",
                "id": "profile_id",
                "name": "DeltaTrak Test",
                "logo_url": None,
                "from_share": True,
            },
        ],
    }


def mockProfileSummary() -> ProfileSummary:
    return {
        "status": True,
        "result": {
            "amount": {
                "device": 3,
                "bucket": 3,
                "dashboard": 3,
                "analysis": 4,
                "action": 1,
                "am": 0,
                "run_users": 0,
                "dictionary": 0,
                "connectors": 0,
                "networks": 0,
                "tcore": 0,
                "tcore_cluster": 0,
            },
            "limit": {
                "analysis": 3000,
                "data_records": 800000,
                "email": 100,
                "input": 1000000,
                "output": 3000000,
                "sms": 10,
                "run_users": 10,
                "push_notification": 100,
                "file_storage": 200,
                "tcore": 1,
            },
            "limit_used": {
                "input": 23379,
                "output": 5161,
                "analysis": 2.17,
                "sms": 10,
                "email": 14,
                "data_records": 0,
                "run_users": 0,
                "push_notification": 0,
                "file_storage": 0.58,
                "tcore": 0,
                "tcore_cluster": 0,
            },
            "tago_run": "profile_id.tago.run",
            "addons": {"custom_dns": False, "mobile": False},
        },
    }


def mockTokenDataList() -> list[TokenDataList]:
    return {
        "status": True,
        "result": [
            {
                "name": "Token Name",
                "permission": "full",
                "token": "token_profile_id",
                "expire_time": "2023-06-07T01:43:45.951Z",
                "created_at": "2023-03-07T01:43:45.952Z",
            },
            {
                "name": "Token Name",
                "permission": "full",
                "token": "token_profile_id",
                "expire_time": None,
                "created_at": "2023-02-24T18:09:33.731Z",
            },
        ],
    }


def testProfileMethodInfo(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get("https://api.tago.io/profile/profile_id", json=mockProfileInfo())

    resources = Resources()
    response = resources.profile.info(profileID="profile_id")

    assert response["allocation"] == mockProfileInfo()["result"]["allocation"]
    assert isinstance(response, dict)


def testProfileMethodList(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get("https://api.tago.io/profile", json=mockListProfileInfo())

    resources = Resources()
    response = resources.profile.list()

    assert response == mockListProfileInfo()["result"]
    assert isinstance(response, list)
    assert isinstance(response[1], dict)


def testProfileMethodSummary(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get(
        "https://api.tago.io/profile/profile_id/summary", json=mockProfileSummary()
    )

    resources = Resources()
    response = resources.profile.summary(profileID="profile_id")

    assert response == mockProfileSummary()["result"]
    assert isinstance(response, dict)


def testProfileMethodTokenList(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get(
        "https://api.tago.io/profile/profile_id/token", json=mockTokenDataList()
    )

    resources = Resources()
    response = resources.profile.tokenList(profileID="profile_id")

    assert response[1]["token"] == mockTokenDataList()["result"][1]["token"]
    assert isinstance(response, list)
    assert isinstance(response[1], dict)


def mockProfileCreate() -> dict:
    return {"status": True, "result": {"id": "new-profile-id-123"}}


def mockProfileEdit() -> dict:
    return {"status": True, "result": "Successfully Updated"}


def mockProfileDelete() -> dict:
    return {"status": True, "result": "Successfully Removed"}


def mockUsageStatisticList() -> dict:
    return {
        "status": True,
        "result": [
            {
                "time": "2024-09-02T00:01:29.749Z",
                "analysis": 0.07,
                "data_records": 67254,
                "input": 1500,
                "output": 250,
            },
            {
                "time": "2024-09-03T00:01:29.749Z",
                "analysis": 0.12,
                "data_records": 85123,
                "input": 2100,
                "output": 340,
            },
        ],
    }


def mockAuditLog() -> dict:
    return {
        "status": True,
        "result": {
            "events": [
                {
                    "resourceName": "device",
                    "message": "Device created",
                    "resourceID": "device-id-123",
                    "who": "account-id-456",
                    "date": "2024-12-01T10:00:00.000Z",
                }
            ],
            "statistics": {
                "recordsMatched": 1,
                "recordsScanned": 100,
                "bytesScanned": 5000,
            },
            "status": "Complete",
            "queryId": "query-id-789",
        },
    }


def mockAddonInfo() -> dict:
    return {
        "status": True,
        "result": {"id": "addon-id-123", "name": "Custom DNS", "logo_url": None},
    }


def mockServiceEdit() -> dict:
    return {"status": True, "result": "Profile resource allocation Successfully Updated"}


def mockTransferToken() -> dict:
    return {"status": True, "result": "Token Successfully Transferred"}


def mockTokenCreate() -> dict:
    return {
        "status": True,
        "result": {
            "token": "new-token-value",
            "name": "API Access",
            "permission": "full",
            "expire_date": "2025-12-31T23:59:59.000Z",
        },
    }


def mockTokenDelete() -> dict:
    return {"status": True, "result": "Token Successfully Removed"}


def mockTeamList() -> dict:
    return {
        "status": True,
        "result": [
            {
                "id": "account-id-123",
                "active": False,
                "name": "John Doe",
                "email": "john@example.com",
                "created_at": "2024-01-01T10:00:00.000Z",
            },
            {
                "id": "account-id-456",
                "active": True,
                "name": "Jane Smith",
                "email": "jane@example.com",
                "created_at": "2024-02-01T10:00:00.000Z",
            },
        ],
    }


def mockAddTeamMember() -> dict:
    return {"status": True, "result": "User invited"}


def mockDeleteTeamMember() -> dict:
    return {"status": True, "result": "Account Successfully Removed"}


def testProfileMethodCreate(requests_mock: Mocker) -> None:
    """Test profile creation"""
    requests_mock.post("https://api.tago.io/profile/", json=mockProfileCreate())

    resources = Resources()
    response = resources.profile.create(
        {"name": "New Profile"}, allocate_free_resources=True
    )

    assert response["id"] == mockProfileCreate()["result"]["id"]
    assert isinstance(response, dict)


def testProfileMethodEdit(requests_mock: Mocker) -> None:
    """Test profile editing"""
    requests_mock.put(
        "https://api.tago.io/profile/profile-id-123", json=mockProfileEdit()
    )

    resources = Resources()
    response = resources.profile.edit("profile-id-123", {"name": "Updated Name"})

    assert response == mockProfileEdit()["result"]
    assert isinstance(response, str)


def testProfileMethodDelete(requests_mock: Mocker) -> None:
    """Test profile deletion"""
    requests_mock.delete(
        "https://api.tago.io/profile/profile-id-123", json=mockProfileDelete()
    )

    resources = Resources()
    response = resources.profile.delete(
        "profile-id-123", {"password": "test-password"}
    )

    assert response == mockProfileDelete()["result"]
    assert isinstance(response, str)


def testProfileMethodUsageStatisticList(requests_mock: Mocker) -> None:
    """Test usage statistics listing"""
    requests_mock.get(
        "https://api.tago.io/profile/profile-id-123/statistics",
        json=mockUsageStatisticList(),
    )

    resources = Resources()
    response = resources.profile.usageStatisticList("profile-id-123")

    assert len(response) == 2
    assert response[0]["analysis"] == 0.07
    assert isinstance(response, list)


def testProfileMethodAuditLog(requests_mock: Mocker) -> None:
    """Test audit log creation"""
    requests_mock.get(
        "https://api.tago.io/profile/profile-id-123/auditlog", json=mockAuditLog()
    )

    resources = Resources()
    response = resources.profile.auditLog("profile-id-123")

    assert response["queryId"] == mockAuditLog()["result"]["queryId"]
    assert response["status"] == "Complete"
    assert isinstance(response, dict)


def testProfileMethodAuditLogQuery(requests_mock: Mocker) -> None:
    """Test audit log query"""
    requests_mock.get(
        "https://api.tago.io/profile/profile-id-123/auditlog/query-id-789",
        json=mockAuditLog(),
    )

    resources = Resources()
    response = resources.profile.auditLogQuery("profile-id-123", "query-id-789")

    assert response["queryId"] == mockAuditLog()["result"]["queryId"]
    assert isinstance(response, dict)


def testProfileMethodServiceEdit(requests_mock: Mocker) -> None:
    """Test service editing"""
    requests_mock.post(
        "https://api.tago.io/profile/profile-id-123/services", json=mockServiceEdit()
    )

    resources = Resources()
    response = resources.profile.serviceEdit(
        "profile-id-123", {"input": 350000, "output": 342153}
    )

    assert response == mockServiceEdit()["result"]
    assert isinstance(response, str)


def testProfileMethodTransferToken(requests_mock: Mocker) -> None:
    """Test token transfer"""
    requests_mock.put(
        "https://api.tago.io/profile/switch/target-profile-123",
        json=mockTransferToken(),
    )

    resources = Resources()
    response = resources.profile.transferTokenToAnotherProfile("target-profile-123")

    assert response == mockTransferToken()["result"]
    assert isinstance(response, str)


def testProfileMethodTokenCreate(requests_mock: Mocker) -> None:
    """Test token creation"""
    requests_mock.post(
        "https://api.tago.io/profile/profile-id-123/token", json=mockTokenCreate()
    )

    resources = Resources()
    response = resources.profile.tokenCreate(
        "profile-id-123",
        {"name": "API Access", "permission": "full", "email": "test@example.com"},
    )

    assert response["token"] == mockTokenCreate()["result"]["token"]
    assert isinstance(response, dict)


def testProfileMethodTokenDelete(requests_mock: Mocker) -> None:
    """Test token deletion"""
    requests_mock.delete(
        "https://api.tago.io/profile/profile-id-123/token/token-xyz",
        json=mockTokenDelete(),
    )

    resources = Resources()
    response = resources.profile.tokenDelete("profile-id-123", "token-xyz")

    assert response == mockTokenDelete()["result"]
    assert isinstance(response, str)


def testProfileMethodAddTeamMember(requests_mock: Mocker) -> None:
    """Test adding team member"""
    requests_mock.post(
        "https://api.tago.io/profile/profile-id-123/team", json=mockAddTeamMember()
    )

    resources = Resources()
    response = resources.profile.addTeamMember("profile-id-123", "user@example.com")

    assert response == mockAddTeamMember()["result"]
    assert isinstance(response, str)


def testProfileMethodTeamList(requests_mock: Mocker) -> None:
    """Test team member listing"""
    requests_mock.get(
        "https://api.tago.io/profile/profile-id-123/team", json=mockTeamList()
    )

    resources = Resources()
    response = resources.profile.teamList("profile-id-123")

    assert len(response) == 2
    assert response[0]["name"] == "John Doe"
    assert isinstance(response, list)


def testProfileMethodDeleteTeamMember(requests_mock: Mocker) -> None:
    """Test team member deletion"""
    requests_mock.delete(
        "https://api.tago.io/profile/profile-id-123/team/account-id-456",
        json=mockDeleteTeamMember(),
    )

    resources = Resources()
    response = resources.profile.deleteTeamMember("profile-id-123", "account-id-456")

    assert response == mockDeleteTeamMember()["result"]
    assert isinstance(response, str)
