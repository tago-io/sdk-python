from typing import TypedDict, Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule


class options(TypedDict):
    retain: bool
    qos: Union[int, float]


class MQTTData(TypedDict):
    topic: str
    message: str
    bucket: GenericID
    options: options


class MQTT(TagoIOModule):
    def publish(self, mqtt: MQTTData) -> str:
        result = self.doRequest(
            {
                "path": "/analysis/services/mqtt/publish",
                "method": "POST",
                "body": {
                    "topic": mqtt["topic"],
                    "message": mqtt["message"],
                    "bucket": mqtt["bucket"],
                    "options": mqtt["options"],
                },
            }
        )
        return result
