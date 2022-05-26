from datetime import datetime

from tagoio_sdk.common.tagoio_module import TagoIOModule


class ConsoleService(TagoIOModule):
    """
    Log message in analysis console

    :param message: Log message
    :param time: Date of message
    """

    def log(self, message: str, time: datetime) -> str:
        timestamp = datetime(time)
        result = self.doRequest(
            {
                "path": "/analysis/services/console/send",
                "method": "POST",
                "body": {"message": message, "timestamp": timestamp},
            }
        )
        return result
