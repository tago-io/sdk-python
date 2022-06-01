from typing import TypedDict

from tagoio_sdk.common.tagoio_module import TagoIOModule


class SMSData(TypedDict):
    to: str
    """
    Number to send SMS, Example: +5599999999999
    """
    message: str
    """
    Message to be send
    """


class SMS(TagoIOModule):
    def send(self, sms: SMSData) -> str:
        """
        Send SMS to phone number

        :param SMSData sms: SMS Object
        """
        result = self.doRequest(
            {
                "path": "/analysis/services/sms/send",
                "method": "POST",
                "body": sms,
            }
        )
        return result
