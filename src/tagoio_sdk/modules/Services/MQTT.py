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
            Legacy MQTT is deprecated. Use the new MQTT connector or HTTP API instead.
            See: https://docs.tago.io/docs/tagoio/integrations/networks/mqtt/
        """
        warnings.warn(
            "services.mqtt.publish() is deprecated and will be removed in a future major version. "
            "Migrate to the new MQTT connector or use the HTTP API. "
            "See: https://docs.tago.io/docs/tagoio/integrations/networks/mqtt/",
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
