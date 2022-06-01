from datetime import datetime
from typing import Union

from tagoio_sdk.common.Common_Type import Data, GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Account.Device_Type import ConfigurationParams
from tagoio_sdk.modules.Device.Device_Type import DataQuery, DeviceInfo
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Device(TagoIOModule):
    """
    The Device object contain a device

    :param TagoIOModule:
    """

    def info(self) -> DeviceInfo:
        """
        Get information about the current device

        :example:

            myDevice = Device({ "token": "my_device_token" })

            result = myDevice.info()

        :rtype: DeviceInfo
        """
        result = self.doRequest({"path": "/info", "method": "get"})
        return DeviceInfo(**result["result"])

    def sendData(self, data: Union[Data, list[Data]]) -> str:
        """
        Send data to device

        :param Union[Data, list[Data]] data: An array or one object with data to be send to
        TagoIO using device token

        :example:

            myDevice = Device({ "token": "my_device_token" })

            result = myDevice.sendData({
                "variable": "temperature",
                "unit": "F",
                "value": 55,
                "time": "2015-11-03 13:44:33",
                "location": { "lat": 42.2974279, "lng": -85.628292 },
            })

        :rtype: str
        """
        result = self.doRequest({"path": "/data", "method": "post", "body": data})
        return result

    def getData(self, queryParams: DataQuery = None) -> list[Data]:
        """
        Get data from TagoIO Device.

        :param DataQuery queryParams: Object with query params

        :example:

            myDevice = Device({ "token": "my_device_token" })

            result = myDevice.getData({
                "query": "last_item",
                "variable": "humidity",
            })

        :rtype: list[Data]
        """
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

    def editData(self, data: Union[Data, list[Data]]) -> str:
        """
        Edit data in a Mutable-type device.

        :param Union[Data, list[Data]] data: Array or object with the data to be edited,
        each object with the data's ID.

        :example:

            myDevice = Device({"token": "my_device_token"})

            result = myDevice.editData(
                {
                    "id": "id_of_the_data_item",
                    "value": "123",
                    "time": "2022-04-01 12:34:56",
                    "location": {"lat": 42.2974279, "lng": -85.628292},
                }
            )

        :return: Success message with the amount of data items updated.

        :rtype: str
        """
        result = self.doRequest(
            {
                "path": "/data",
                "method": "PUT",
                "body": data,
            }
        )
        return result

    def deleteData(self, queryParams: DataQuery) -> str:
        """
        Delete data from device

        :param DataQuery queryParams: Object with query params

        :example:

            myDevice = Device({ "token": "my_device_token" });

            result = await myDevice.deleteData({
                "query": "last_item",
                "variable": "humidity",
                "value": 10
            });

        :rtype: str
        """
        if queryParams is None:
            queryParams = {"query": "last_item"}

        if queryParams.query == "default":
            del queryParams.query

        result = self.doRequest(
            {
                "path": "/data",
                "method": "DELETE",
                "params": queryParams,
            }
        )
        return result

    def getParameters(self, onlyUnRead: bool) -> list[ConfigurationParams]:
        """
        Get parameters from device

        :param bool onlyUnRead: set true to get only unread parameters

        :example:

            myDevice = Device({ "token": "my_device_token" })

            result = myDevice.getParameters()

        :rtype: list[ConfigurationParams]
        """
        params = {}

        if onlyUnRead is True:
            params.sentStatus = True

        result = self.doRequest(
            {
                "path": "/device/params",
                "method": "GET",
                "params": params,
            }
        )
        return result

    def setParameterAsRead(self, parameterID: GenericID) -> str:
        """
        Mark parameter as read

        :param GenericID parameterID: Parameter identification

        :example:

            myDevice = Device({ "token": "my_device_token" })

            result = myDevice.setParameterAsRead({"parameterID": "parameter_id"})

        :rtype: str
        """
        result = self.doRequest(
            {
                "path": f"/device/params/{parameterID}",
                "method": "PUT",
            }
        )
        return result
