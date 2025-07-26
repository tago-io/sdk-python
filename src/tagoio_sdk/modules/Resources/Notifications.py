from typing import List
from typing import Optional
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Notification_Type import NotificationCreate
from tagoio_sdk.modules.Resources.Notification_Type import NotificationInfo
from tagoio_sdk.modules.Resources.Notification_Type import NotificationQuery
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Notifications(TagoIOModule):
    def list(self, queryObj: Optional[NotificationQuery] = None) -> List[NotificationInfo]:
        """
        @description:
            Retrieves all notifications from the application with optional filtering.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Access notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.notifications.list({"filter": {"read": False}, "amount": 10})
            print(result)  # [{'id': 'notification-id-123', 'title': 'System Update', 'message': 'Features', ...}]
            ```
        """
        result = self.doRequest(
            {
                "path": "/notification/",
                "method": "GET",
                "params": queryObj or {},
            }
        )

        result = dateParserList(result, ["created_at"])

        return result

    def markAsRead(self, notificationIDS: Union[GenericID, List[GenericID]]) -> str:
        """
        @description:
            Marks one or multiple notifications as read.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Edit notification** in Access Management.
            ```python
            resources = Resources()
            # Mark single notification
            resources.notifications.markAsRead("notification-id-123")

            # Mark multiple notifications
            resources.notifications.markAsRead(["id-1", "id-2"])
            ```
        """
        if not isinstance(notificationIDS, list):
            notificationIDS = [notificationIDS]

        result = self.doRequest(
            {
                "path": "/notification/read",
                "method": "PUT",
                "body": {
                    "notification_ids": notificationIDS,
                    "read": True,
                },
            }
        )

        return result

    def markAsUnread(self, notificationIDS: Union[GenericID, List[GenericID]]) -> str:
        """
        @description:
            Marks one or multiple notifications as unread.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Edit notification** in Access Management.
            ```python
            resources = Resources()
            # Mark single notification
            resources.notifications.markAsUnread("notification-id-123")

            # Mark multiple notifications
            resources.notifications.markAsUnread(["id-1", "id-2"])
            ```
        """
        if not isinstance(notificationIDS, list):
            notificationIDS = [notificationIDS]

        result = self.doRequest(
            {
                "path": "/notification/read",
                "method": "PUT",
                "body": {
                    "notification_ids": notificationIDS,
                    "read": False,
                },
            }
        )

        return result

    def markAllAsRead(self) -> str:
        """
        @description:
            Marks all notifications in the application as read.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Edit notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.notifications.markAllAsRead()
            print(result)  # All TagoIO Notification Run Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": "/notification/markallread",
                "method": "PUT",
            }
        )

        return result

    def notificationButton(self, notificationID: GenericID, buttonID: str) -> str:
        """
        @description:
            Records when a notification button is pressed by the user.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Edit notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.notifications.notificationButton("notification-123", "button-456")
            print(result)
            ```
        """
        result = self.doRequest(
            {
                "path": f"/notification/{notificationID}/{buttonID}",
                "method": "PUT",
            }
        )

        return result

    def create(self, notificationData: NotificationCreate) -> dict:
        """
        @description:
            Creates a new notification in the system.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Create notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.notifications.create({"title": "System Update", "message": "New features available"})
            print(result["id"])  # notification-id-123
            ```
        """
        result = self.doRequest(
            {
                "path": "/notification",
                "method": "POST",
                "body": {**notificationData},
            }
        )

        return result

    def remove(self, notificationID: GenericID) -> str:
        """
        @description:
            Permanently deletes a notification from the system.

        @see:
            https://help.tago.io/portal/en/kb/articles/11-notification Notification

        @example:
            If receive an error "Authorization Denied", check policy **Profile** / **Delete notification** in Access Management.
            ```python
            resources = Resources()
            result = resources.notifications.remove("notification-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/notification/{notificationID}",
                "method": "DELETE",
            }
        )

        return result

    def registerDevice(self, deviceToken: GenericToken, platform: str) -> str:
        """
        @description:
            Registers a mobile device for push notifications.
        @note:
            **This is used internally for mobile applications**
        """
        result = self.doRequest(
            {
                "path": "/notification/push/register",
                "method": "POST",
                "body": {
                    "device_token": deviceToken,
                    "platform": platform,
                },
            }
        )

        return result

    def unRegisterDevice(self, deviceToken: GenericToken) -> str:
        """
        @description:
            Removes a mobile device from push notification service.
        @note:
            **This is used internally for mobile applications**
        """
        result = self.doRequest(
            {
                "path": "/notification/push/unregister",
                "method": "POST",
                "body": {
                    "device_token": deviceToken,
                },
            }
        )

        return result
