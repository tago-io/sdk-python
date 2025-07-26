from datetime import datetime

from tagoio_sdk.common.tagoio_module import TagoIOModule


class ConsoleService(TagoIOModule):
    """
    Log message in analysis console

    :param message: Log message
    :param time: Date of message
    """

    def log(self, message: str, timestamp: datetime = None) -> str:
        if timestamp is None:
            timestamp = datetime.now()
        result = self.doRequest(
            {
                "path": "/analysis/services/console/send",
                "method": "POST",
                "body": {"message": message, "timestamp": timestamp},
            }
        )
        return result
