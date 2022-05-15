from datetime import datetime
from typing import Union
from tagoio_sdk.common.Common_Type import Data
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Device.Device_Type import DataQuery, DeviceInfo
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Device(TagoIOModule):
    def info(self) -> DeviceInfo:
        result = self.doRequest({"path": "/info", "method": "get"})
        return DeviceInfo(**result["result"])

    def sendData(self, data: Union[Data, list[Data]]) -> list[Data]:
        result = self.doRequest({"path": "/data", "method": "post", "body": data})
        return result

    def getData(self, queryParams: DataQuery = None) -> list[Data]:
        result = self.doRequest(
            {"path": "/data", "method": "get", "params": queryParams}
        )

        if isinstance(result, int):
            result = [
                Data(
                    id="none",
                    origin="?",
                    time=datetime.now(),
                    value=result,
                    variable="?",
                )
            ]
            return result

        result = dateParserList(result, ["time"])
        return result
