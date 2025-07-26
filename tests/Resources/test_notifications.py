import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Notification_Type import NotificationInfo

os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockNotificationList() -> list[NotificationInfo]:
    return {
        "status": True,
        "result": [
            {
                "id": "notification_id_1",
                "title": "System Update",
                "message": "New features available",
                "read": False,
                "created_at": "2023-06-15T10:00:00.000Z",
            },
            {
                "id": "notification_id_2",
                "title": "Maintenance",
                "message": "Scheduled maintenance",
                "read": True,
                "created_at": "2023-06-14T14:30:00.000Z",
            },
        ],
    }


def mockCreateNotification() -> dict:
    return {
        "status": True,
        "result": {"id": "new_notification_id"},
    }


def testNotificationsMethodList(requests_mock: Mocker) -> None:
    """Test list method of Notifications class."""
    mock_response = mockNotificationList()
    requests_mock.get("https://api.tago.io/notification/", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.list()

    # Check if result has expected structure
    assert len(result) == 2
    assert result[0]["id"] == "notification_id_1"
    assert result[1]["id"] == "notification_id_2"

    # Test with query parameters
    query = {"read": False, "amount": 10}

    requests_mock.get("https://api.tago.io/notification/", json=mock_response)
    result = resources.notifications.list(query)

    assert len(result) == 2


def testNotificationsMethodMarkAsRead(requests_mock: Mocker) -> None:
    """Test markAsRead method of Notifications class."""
    mock_response = {"status": True, "result": "TagoIO Notification Run Successfully Updated"}
    requests_mock.put("https://api.tago.io/notification/read", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    # Test with single notification ID
    result = resources.notifications.markAsRead("notification_id_1")
    assert result == "TagoIO Notification Run Successfully Updated"

    # Test with multiple notification IDs
    result = resources.notifications.markAsRead(["notification_id_1", "notification_id_2"])
    assert result == "TagoIO Notification Run Successfully Updated"


def testNotificationsMethodMarkAsUnread(requests_mock: Mocker) -> None:
    """Test markAsUnread method of Notifications class."""
    mock_response = {"status": True, "result": "TagoIO Notification Run Successfully Updated"}
    requests_mock.put("https://api.tago.io/notification/read", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    # Test with single notification ID
    result = resources.notifications.markAsUnread("notification_id_1")
    assert result == "TagoIO Notification Run Successfully Updated"

    # Test with multiple notification IDs
    result = resources.notifications.markAsUnread(["notification_id_1", "notification_id_2"])
    assert result == "TagoIO Notification Run Successfully Updated"


def testNotificationsMethodMarkAllAsRead(requests_mock: Mocker) -> None:
    """Test markAllAsRead method of Notifications class."""
    mock_response = {"status": True, "result": "All TagoIO Notification Run Successfully Updated"}
    requests_mock.put("https://api.tago.io/notification/markallread", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.markAllAsRead()

    assert result == "All TagoIO Notification Run Successfully Updated"


def testNotificationsMethodNotificationButton(requests_mock: Mocker) -> None:
    """Test notificationButton method of Notifications class."""
    mock_response = {"status": True, "result": "Button action processed"}
    requests_mock.put("https://api.tago.io/notification/notification_id_1/button_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.notificationButton("notification_id_1", "button_id_1")

    assert result == "Button action processed"


def testNotificationsMethodCreate(requests_mock: Mocker) -> None:
    """Test create method of Notifications class."""
    mock_response = mockCreateNotification()
    requests_mock.post("https://api.tago.io/notification", json=mock_response)

    resources = Resources({"token": "your_token_value"})

    notification_data = {
        "title": "New Notification",
        "message": "This is a test notification",
        "read": False,
    }

    result = resources.notifications.create(notification_data)

    # Check if result has expected structure
    assert result["id"] == "new_notification_id"


def testNotificationsMethodRemove(requests_mock: Mocker) -> None:
    """Test remove method of Notifications class."""
    mock_response = {"status": True, "result": "Successfully Removed"}
    requests_mock.delete("https://api.tago.io/notification/notification_id_1", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.remove("notification_id_1")

    assert result == "Successfully Removed"


def testNotificationsMethodRegisterDevice(requests_mock: Mocker) -> None:
    """Test registerDevice method of Notifications class."""
    mock_response = {"status": True, "result": "Device successfully registered"}
    requests_mock.post("https://api.tago.io/notification/push/register", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.registerDevice("device_token_123", "android")

    assert result == "Device successfully registered"


def testNotificationsMethodUnRegisterDevice(requests_mock: Mocker) -> None:
    """Test unRegisterDevice method of Notifications class."""
    mock_response = {"status": True, "result": "Device successfully unregistered"}
    requests_mock.post("https://api.tago.io/notification/push/unregister", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.notifications.unRegisterDevice("device_token_123")

    assert result == "Device successfully unregistered"
