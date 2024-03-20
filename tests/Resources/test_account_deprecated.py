from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Account import Account
from tagoio_sdk.modules.Resources.Account_Types import AccountInfo


def mockAccountInfo() -> list[AccountInfo]:
    return {
        "status": True,
        "result": {
            "active": True,
            "blocked": False,
            "created_at": "2023-02-21T15:17:35.759Z",
            "email": "email@test.com",
            "id": "test_id",
            "language": "en",
            "last_login": "2023-03-07T01:43:45.950Z",
            "name": "Tester Test",
            "newsletter": False,
            "options": {
                "quickstart": {
                    "finished_tasks": [
                        "actions",
                        "devices",
                        "dashboards",
                        "deploy",
                        "access",
                        "explore",
                    ],
                    "finished_percentage": 86,
                },
                "last_whats_new": "2022-06-16T15:00:00.001Z",
                "decimal_separator": ".",
                "user_view_welcome": True,
                "thousand_separator": ",",
            },
            "phone": None,
            "plan": "free",
            "send_invoice": False,
            "stripe_id": "test_stripe_id",
            "timezone": "America/Sao_Paulo",
            "type": "user",
            "updated_at": "2023-03-24T17:43:47.916Z",
            "otp": {},
            "survey": {
                "PLAN_TO_USE_TAGOIO": True,
                "SECTORS_INDUSTRY_IN": True,
                "WHICH_TYPE_BUSINESS": True,
            },
            "company": "tago.io",
            "country": "Brazil",
        },
    }


def testAccountMethodInfo(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get("https://api.tago.io/account", json=mockAccountInfo())

    tokenFake = {"token": "fake_token"}
    response = Account(params=tokenFake).info()

    assert response["email"] == mockAccountInfo()["result"]["email"]
    assert isinstance(response, dict)
