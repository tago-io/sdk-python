import socketio

from tagoio_sdk import config
from tagoio_sdk.common.tagoio_module import GenericModuleParams
from tagoio_sdk.regions import getConnectionURI

socketOptions = config.tagoSDKconfig["socketOpts"]


class APISocket:
    def __init__(self, params: GenericModuleParams) -> None:
        url = getConnectionURI(params.get("region"))["realtime"]
        URLRealtime = "{}{}{}".format(url, "?token=", params.get("token"))
        self.realtimeURL = URLRealtime

        sio = socketio.AsyncClient(
            reconnection=socketOptions["reconnection"],
            reconnection_delay=socketOptions["reconnectionDelay"],
        )
        self.sio = sio

    async def connect(self) -> socketio.AsyncClient:
        await self.sio.connect(
            url=self.realtimeURL, transports=socketOptions["transports"]
        )
        await self.sio.wait()


channels = {
    "notification": "notification::data",
    "analysisConsole": "analysis::console",
    "analysisTrigger": "analysis::trigger",
    "bucketData": "bucket::data",
}
