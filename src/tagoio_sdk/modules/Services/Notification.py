from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Account.Notification_Type import NotificationCreate


class Notification(TagoIOModule):
    def send(self, notification: NotificationCreate) -> str:
        """
        Send Notification

        You can add ref_id from a bucket or dashboard, if it is valid it will show up a button Go To
        Dashboard Any account with share of the dashboard/bucket will receive too.

        :param NotificationCreate notification: Notification Object
        """
        result = self.doRequest(
            {
                "path": "/analysis/services/notification/send",
                "method": "POST",
                "body": notification,
            }
        )

        return result
