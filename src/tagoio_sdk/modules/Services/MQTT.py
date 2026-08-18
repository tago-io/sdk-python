import warnings

from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule


class options(TypedDict):
    retain: Optional[bool]
    qos: Optional[Union[int, float]]


class MQTTData(TypedDict):
    topic: str
    message: str
    bucket: GenericID
    options: Optional[options]


class MQTT(TagoIOModule):
    def publish(self, mqtt: MQTTData) -> str:
        """Publish an MQTT message.

        .. deprecated::
            Migrate to TagoTIP: https://docs.tago.io/docs/tagotip/transports/mqtt
        """
        warnings.warn(
            "services.mqtt.publish() is deprecated. "
            "Migrate to TagoTIP: https://docs.tago.io/docs/tagotip/transports/mqtt",
            DeprecationWarning,
            stacklevel=2,
        )
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
