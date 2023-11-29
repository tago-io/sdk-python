import os
from requests_mock.mocker import Mocker

from tagoio_sdk.common.Common_Type import TokenDataList
from tagoio_sdk.modules.Resources.Profile_Type import ProfileInfo, ProfileSummary
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
