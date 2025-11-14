import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Account import Account
from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockAccountInfo() -> dict:
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
            "otp": {"authenticator": False, "sms": False, "email": True},
            "company": "tago.io",
        },
    }


def mockLoginResponse() -> dict:
    return {
        "status": True,
        "result": {
            "type": "user",
            "id": "612ea05e3cc078001371895110",
            "email": "example@mail.com",
            "company": "companyname",
            "name": "Your Name",
            "profiles": [
                {
                    "id": "612ea05e3cc078001371895111",
                    "name": "profilename",
                }
            ],
        },
    }


def mockTokenCreateResponse() -> dict:
    return {
        "status": True,
        "result": {"token": "new-generated-token-123"},
    }


def testAccountMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Account class."""
    mock_response = mockAccountInfo()
    requests_mock.get("https://api.tago.io/account", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    response = resources.account.info()

    assert response["email"] == "email@test.com"
    assert response["name"] == "Tester Test"
    assert response["id"] == "test_id"
    assert isinstance(response, dict)


def testAccountMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Account class."""
    mock_response = {
        "status": True,
        "result": "Account Successfully Updated",
    }

    requests_mock.put("https://api.tago.io/account", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    account_data = {
        "name": "Updated Account Name",
        "timezone": "America/New_York",
        "company": "My Company",
    }

    result = resources.account.edit(account_data)

    assert result == "Account Successfully Updated"


def testAccountMethodDelete(requests_mock: Mocker) -> None:
    """Test delete method of Account class."""
    mock_response = {
        "status": True,
        "result": "Account Successfully Deleted",
    }

    requests_mock.delete("https://api.tago.io/account", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.account.delete()

    assert result == "Account Successfully Deleted"


def testAccountMethodPasswordChange(requests_mock: Mocker) -> None:
    """Test passwordChange method of Account class."""
    mock_response = {
        "status": True,
        "result": "Password changed successfully",
    }

    requests_mock.post("https://api.tago.io/account/passwordreset", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.account.passwordChange("new-secure-password")

    assert result == "Password changed successfully"


def testAccountMethodEnableOTP(requests_mock: Mocker) -> None:
    """Test enableOTP method of Account class."""
    mock_response = {
        "status": True,
        "result": "OTP enabled, confirmation required",
    }

    requests_mock.post("https://api.tago.io/account/otp/email/enable", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.account.enableOTP({"email": "user@example.com", "password": "password"}, "email")

    assert result == "OTP enabled, confirmation required"


def testAccountMethodDisableOTP(requests_mock: Mocker) -> None:
    """Test disableOTP method of Account class."""
    mock_response = {
        "status": True,
        "result": "OTP disabled successfully",
    }

    requests_mock.post("https://api.tago.io/account/otp/authenticator/disable", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.account.disableOTP({"email": "user@example.com", "password": "password"}, "authenticator")

    assert result == "OTP disabled successfully"


def testAccountMethodConfirmOTP(requests_mock: Mocker) -> None:
    """Test confirmOTP method of Account class."""
    mock_response = {
        "status": True,
        "result": "OTP confirmed successfully",
    }

    requests_mock.post("https://api.tago.io/account/otp/email/confirm", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    result = resources.account.confirmOTP("123456", "email")

    assert result == "OTP confirmed successfully"


def testAccountStaticMethodTokenCreate(requests_mock: Mocker) -> None:
    """Test tokenCreate static method of Account class."""
    mock_response = mockTokenCreateResponse()
    requests_mock.post("https://api.tago.io/account/profile/token", json=mock_response)

    token_params = {
        "profile_id": "profile-id-123",
        "email": "user@example.com",
        "password": "your-password",
        "pin_code": "123456",
        "otp_type": "email",
        "name": "My API Token",
    }

    result = Account.tokenCreate(token_params)

    assert result["token"] == "new-generated-token-123"


def testAccountStaticMethodLogin(requests_mock: Mocker) -> None:
    """Test login static method of Account class."""
    mock_response = mockLoginResponse()
    requests_mock.post("https://api.tago.io/account/login", json=mock_response)

    credentials = {
        "email": "user@example.com",
        "password": "your-password",
        "otp_type": "email",
        "pin_code": "123456",
    }

    result = Account.login(credentials)

    assert result["email"] == "example@mail.com"
    assert result["type"] == "user"
    assert len(result["profiles"]) == 1
    assert result["profiles"][0]["name"] == "profilename"


def testAccountStaticMethodPasswordRecover(requests_mock: Mocker) -> None:
    """Test passwordRecover static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Email sent successfully",
    }

    requests_mock.get("https://api.tago.io/account/passwordreset/user@example.com", json=mock_response)

    result = Account.passwordRecover("user@example.com")

    assert result == "Email sent successfully"


def testAccountStaticMethodCreate(requests_mock: Mocker) -> None:
    """Test create static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Account created successfully",
    }

    requests_mock.post("https://api.tago.io/account", json=mock_response)

    create_params = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "secure-password",
        "cpassword": "secure-password",
        "timezone": "America/New_York",
        "company": "My Company",
        "newsletter": False,
    }

    result = Account.create(create_params)

    assert result == "Account created successfully"


def testAccountStaticMethodResendConfirmation(requests_mock: Mocker) -> None:
    """Test resendConfirmation static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Confirmation email sent",
    }

    requests_mock.get("https://api.tago.io/account/resend_confirmation/user@example.com", json=mock_response)

    result = Account.resendConfirmation("user@example.com")

    assert result == "Confirmation email sent"


def testAccountStaticMethodConfirmAccount(requests_mock: Mocker) -> None:
    """Test confirmAccount static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Account confirmed successfully",
    }

    requests_mock.get("https://api.tago.io/account/confirm/confirmation-token-123", json=mock_response)

    result = Account.confirmAccount("confirmation-token-123")

    assert result == "Account confirmed successfully"


def testAccountStaticMethodRequestLoginPINCode(requests_mock: Mocker) -> None:
    """Test requestLoginPINCode static method of Account class."""
    mock_response = {
        "status": True,
        "result": "PIN code sent",
    }

    requests_mock.post("https://api.tago.io/account/login/otp", json=mock_response)

    credentials = {"email": "user@example.com", "password": "your-password"}

    result = Account.requestLoginPINCode(credentials, "email")

    assert result == "PIN code sent"


def testAccountStaticMethodAcceptTeamInvitation(requests_mock: Mocker) -> None:
    """Test acceptTeamInvitation static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Invitation accepted",
    }

    requests_mock.get("https://api.tago.io/profile/team/accept/invitation-token-123", json=mock_response)

    result = Account.acceptTeamInvitation("invitation-token-123")

    assert result == "Invitation accepted"


def testAccountStaticMethodDeclineTeamInvitation(requests_mock: Mocker) -> None:
    """Test declineTeamInvitation static method of Account class."""
    mock_response = {
        "status": True,
        "result": "Invitation declined",
    }

    requests_mock.get("https://api.tago.io/profile/team/decline/invitation-token-123", json=mock_response)

    result = Account.declineTeamInvitation("invitation-token-123")

    assert result == "Invitation declined"
