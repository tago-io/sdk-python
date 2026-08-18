from typing import TypedDict

from tagoio_sdk.common.tagoio_module import TagoIOModule


class TagoTiPCommand(TypedDict):
    serial: str
    """
    Serial of the target device
    """
    protocol: str
    """
    Protocol used to deliver the command
    """
    body: str
    """
    Command payload sent to the device
    """


class TagoTiP(TagoIOModule):
    def cmd(self, command: TagoTiPCommand) -> str:
        """
        Send a command to a device through TagoTiP.

        Requires a Service Authorization token in the module `token`.

        :param TagoTiPCommand command: Command object with serial, protocol and body

        Example:
            >>> from tagoio_sdk import TagoTiP
            >>> tagotip = TagoTiP({"token": "your-service-authorization-token"})
            >>> tagotip.cmd({
            ...     "serial": "mqtt1",
            ...     "protocol": "mqtt",
            ...     "body": "reboot-now",
            ... })
        """
        result = self.doRequest(
            {
                "path": "/tip/cmd",
                "method": "POST",
                "body": {
                    "serial": command["serial"],
                    "protocol": command["protocol"],
                    "body": command["body"],
                },
            }
        )
        return result
