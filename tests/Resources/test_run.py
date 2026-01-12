import os

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockRunInfo() -> dict:
    return {
        "status": True,
        "result": {
            "profile": "profile_id_123",
            "active": True,
            "name": "My Run Environment",
            "sub_title": "IoT Application",
            "url": "myapp.run.tago.io",
            "email_domain": None,
            "signup_method": "default",
            "favicon": None,
            "logo": "https://example.com/logo.png",
            "signup_logo": None,
            "signup_logo_options": {},
            "sidebar_buttons": [],
            "signup_fields": [],
            "email_templates": {},
            "feature_devicewifisetup": {},
            "feature_geolocation": {},
            "theme": {},
            "integration": {},
            "sso_saml_active": False,
            "security": {},
        },
    }


def mockRunEdit() -> dict:
    return {"status": True, "result": "TagoIO Run Successfully Updated"}


def mockUserList() -> dict:
    return {
        "status": True,
        "result": [
            {
                "id": "user_id_1",
                "name": "John Doe",
                "email": "john@example.com",
                "timezone": "America/New_York",
                "created_at": "2023-02-21T15:17:35.759Z",
                "updated_at": "2023-02-21T15:17:35.759Z",
                "last_login": "2023-02-21T15:17:35.759Z",
            },
            {
                "id": "user_id_2",
                "name": "Jane Smith",
                "email": "jane@example.com",
                "timezone": "America/Los_Angeles",
                "created_at": "2023-02-21T16:17:35.759Z",
                "updated_at": "2023-02-21T16:17:35.759Z",
                "last_login": "2023-02-21T16:17:35.759Z",
            },
        ],
    }


def mockUserInfo() -> dict:
    return {
        "status": True,
        "result": {
            "id": "user_id_1",
            "name": "John Doe",
            "email": "john@example.com",
            "timezone": "America/New_York",
            "company": "ACME Corp",
            "phone": "+1234567890",
            "language": "en-US",
            "profile": "profile_id_123",
            "active": True,
            "newsletter": False,
            "last_login": "2023-02-21T15:17:35.759Z",
            "created_at": "2023-02-21T15:17:35.759Z",
            "updated_at": "2023-02-21T15:17:35.759Z",
            "options": {},
            "tags": [{"key": "role", "value": "admin"}],
        },
    }


def mockUserCreate() -> dict:
    return {"status": True, "result": {"user": "user_id_new"}}


def mockUserEdit() -> dict:
    return {"status": True, "result": "TagoIO Run User Successfully Updated"}


def mockUserDelete() -> dict:
    return {"status": True, "result": "Successfully Removed"}


def mockLoginAsUser() -> dict:
    return {
        "status": True,
        "result": {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...",
            "expire_date": "2024-02-21T15:17:35.759Z",
        },
    }


def mockEmailTest() -> dict:
    return {"status": True, "result": "E-mail sent to example@email.com"}


def mockNotificationList() -> dict:
    return {
        "status": True,
        "result": [
            {
                "id": "notification_id_1",
                "title": "System Update",
                "message": "New features available",
            },
            {
                "id": "notification_id_2",
                "title": "Maintenance",
                "message": "Scheduled maintenance tonight",
            },
        ],
    }


def mockNotificationCreate() -> dict:
    return {"status": True, "result": {"id": "notification_id_new"}}


def mockNotificationEdit() -> dict:
    return {"status": True, "result": "TagoIO Notification User Successfully Updated"}


def mockNotificationDelete() -> dict:
    return {"status": True, "result": "Successfully Removed"}


def mockSSOSAMLInfo() -> dict:
    return {
        "status": True,
        "result": {
            "sp": {
                "entity_id": "https://example.com",
                "acs_url": "https://example.com/acs",
                "metadata": "<xml>...</xml>",
            },
            "idp": {"issuer": "https://idp.example.com"},
            "mapping": {"email": "email", "firstName": "firstName"},
        },
    }


def mockSSOSAMLEdit() -> dict:
    return {"status": True, "result": "TagoIO Run SAML SSO Successfully Updated"}


def mockCustomDomainCreate() -> dict:
    return {"status": True, "result": "Custom domain created successfully"}


def mockCustomDomainInfo() -> dict:
    return {
        "status": True,
        "result": {
            "active": True,
            "domain": "mycompany.com",
            "subdomain": "app",
            "email": "app.mycompany.com",
            "dns_ssl": {"status": True, "type": "TXT", "key": "key1", "value": "value1"},
            "dns_page": {"status": True, "type": "CNAME", "key": "key2", "value": "value2"},
            "dns_email_1": {"status": True, "type": "MX", "key": "key3", "value": "value3"},
            "dns_email_2": {"status": True, "type": "TXT", "key": "key4", "value": "value4"},
            "dns_email_3": {"status": True, "type": "TXT", "key": "key5", "value": "value5"},
            "created_at": "2023-02-21T15:17:35.759Z",
        },
    }


def mockCustomDomainDelete() -> dict:
    return {"status": True, "result": "Custom domain deleted successfully"}


def mockCustomDomainRegenerate() -> dict:
    return {"status": True, "result": "Custom domain regenerated successfully"}


def testRunMethodInfo(requests_mock: Mocker) -> None:
    """Test info method of Run class."""
    mock_response = mockRunInfo()
    requests_mock.get("https://api.tago.io/run", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.info()

    assert result["name"] == "My Run Environment"
    assert result["active"] is True


def testRunMethodEdit(requests_mock: Mocker) -> None:
    """Test edit method of Run class."""
    mock_response = mockRunEdit()
    requests_mock.put("https://api.tago.io/run", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.edit({"name": "Updated Name"})

    assert result == "TagoIO Run Successfully Updated"


def testRunMethodListUsers(requests_mock: Mocker) -> None:
    """Test listUsers method of Run class."""
    mock_response = mockUserList()
    requests_mock.get("https://api.tago.io/run/users", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.listUsers({"page": 1, "amount": 20})

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == "user_id_1"
    assert result[1]["id"] == "user_id_2"


def testRunMethodUserInfo(requests_mock: Mocker) -> None:
    """Test userInfo method of Run class."""
    mock_response = mockUserInfo()
    requests_mock.get("https://api.tago.io/run/users/user_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.userInfo("user_id_1")

    assert result["id"] == "user_id_1"
    assert result["name"] == "John Doe"
    assert result["email"] == "john@example.com"


def testRunMethodUserCreate(requests_mock: Mocker) -> None:
    """Test userCreate method of Run class."""
    mock_response = mockUserCreate()
    requests_mock.post("https://api.tago.io/run/users", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.userCreate(
        {
            "name": "New User",
            "email": "newuser@example.com",
            "password": "secure123",
            "timezone": "America/New_York",
        }
    )

    assert result["user"] == "user_id_new"


def testRunMethodUserEdit(requests_mock: Mocker) -> None:
    """Test userEdit method of Run class."""
    mock_response = mockUserEdit()
    requests_mock.put("https://api.tago.io/run/users/user_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.userEdit("user_id_1", {"name": "Updated Name"})

    assert result == "TagoIO Run User Successfully Updated"


def testRunMethodUserDelete(requests_mock: Mocker) -> None:
    """Test userDelete method of Run class."""
    mock_response = mockUserDelete()
    requests_mock.delete("https://api.tago.io/run/users/user_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.userDelete("user_id_1")

    assert result == "Successfully Removed"


def testRunMethodLoginAsUser(requests_mock: Mocker) -> None:
    """Test loginAsUser method of Run class."""
    mock_response = mockLoginAsUser()
    requests_mock.get("https://api.tago.io/run/users/user_id_1/login", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.loginAsUser("user_id_1")

    assert "token" in result
    assert result["token"].startswith("eyJ")


def testRunMethodEmailTest(requests_mock: Mocker) -> None:
    """Test emailTest method of Run class."""
    mock_response = mockEmailTest()
    requests_mock.post("https://api.tago.io/run/email_test", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.emailTest({"subject": "Test", "body": "Test message"})

    assert result == "E-mail sent to example@email.com"


def testRunMethodNotificationList(requests_mock: Mocker) -> None:
    """Test notificationList method of Run class."""
    mock_response = mockNotificationList()
    requests_mock.get("https://api.tago.io/run/notification/user_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.notificationList("user_id_1")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["id"] == "notification_id_1"


def testRunMethodNotificationCreate(requests_mock: Mocker) -> None:
    """Test notificationCreate method of Run class."""
    mock_response = mockNotificationCreate()
    requests_mock.post("https://api.tago.io/run/notification/", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.notificationCreate("user_id_1", {"title": "Alert", "message": "Important message"})

    assert result["id"] == "notification_id_new"


def testRunMethodNotificationEdit(requests_mock: Mocker) -> None:
    """Test notificationEdit method of Run class."""
    mock_response = mockNotificationEdit()
    requests_mock.put("https://api.tago.io/run/notification/notification_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.notificationEdit("notification_id_1", {"title": "Updated Title"})

    assert result == "TagoIO Notification User Successfully Updated"


def testRunMethodNotificationDelete(requests_mock: Mocker) -> None:
    """Test notificationDelete method of Run class."""
    mock_response = mockNotificationDelete()
    requests_mock.delete("https://api.tago.io/run/notification/notification_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.notificationDelete("notification_id_1")

    assert result == "Successfully Removed"


def testRunMethodSSOSAMLInfo(requests_mock: Mocker) -> None:
    """Test ssoSAMLInfo method of Run class."""
    mock_response = mockSSOSAMLInfo()
    requests_mock.get("https://api.tago.io/run/sso/saml", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.ssoSAMLInfo()

    assert "sp" in result
    assert "idp" in result


def testRunMethodSSOSAMLEdit(requests_mock: Mocker) -> None:
    """Test ssoSAMLEdit method of Run class."""
    mock_response = mockSSOSAMLEdit()
    requests_mock.put("https://api.tago.io/run/sso/saml", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.ssoSAMLEdit({"active": True, "idp_metadata": "<xml>...</xml>"})

    assert result == "TagoIO Run SAML SSO Successfully Updated"


def testRunMethodCreateCustomDomain(requests_mock: Mocker) -> None:
    """Test createCustomDomain method of Run class."""
    mock_response = mockCustomDomainCreate()
    requests_mock.post("https://api.tago.io/run/customdomain/profile_id_123", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.createCustomDomain("profile_id_123", {"domain": "mycompany.com", "subdomain": "app"})

    assert result == "Custom domain created successfully"


def testRunMethodGetCustomDomain(requests_mock: Mocker) -> None:
    """Test getCustomDomain method of Run class."""
    mock_response = mockCustomDomainInfo()
    requests_mock.get("https://api.tago.io/run/customdomain/profile_id_123", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.getCustomDomain("profile_id_123")

    assert result["domain"] == "mycompany.com"
    assert result["active"] is True


def testRunMethodDeleteCustomDomain(requests_mock: Mocker) -> None:
    """Test deleteCustomDomain method of Run class."""
    mock_response = mockCustomDomainDelete()
    requests_mock.delete("https://api.tago.io/run/customdomain/profile_id_123", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.deleteCustomDomain("profile_id_123")

    assert result == "Custom domain deleted successfully"


def testRunMethodRegenerateCustomDomain(requests_mock: Mocker) -> None:
    """Test regenerateCustomDomain method of Run class."""
    mock_response = mockCustomDomainRegenerate()
    requests_mock.put("https://api.tago.io/run/customdomain/regenerate/profile_id_123", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.run.regenerateCustomDomain("profile_id_123")

    assert result == "Custom domain regenerated successfully"
