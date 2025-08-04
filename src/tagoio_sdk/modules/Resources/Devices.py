from typing import Optional
from typing import Union

from tagoio_sdk.common.Common_Type import Data
from tagoio_sdk.common.Common_Type import DataCreate
from tagoio_sdk.common.Common_Type import DataEdit
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import GenericToken
from tagoio_sdk.common.Common_Type import TokenCreateResponse
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Device.Device_Type import DataQuery
from tagoio_sdk.modules.Device.Device_Type import DeviceInfo
from tagoio_sdk.modules.Resources.Device_Type import ConfigurationParams
from tagoio_sdk.modules.Resources.Device_Type import DeviceCreateInfo
from tagoio_sdk.modules.Resources.Device_Type import DeviceCreateResponse
from tagoio_sdk.modules.Resources.Device_Type import DeviceEditInfo
from tagoio_sdk.modules.Resources.Device_Type import DeviceListItem
from tagoio_sdk.modules.Resources.Device_Type import DeviceQuery
from tagoio_sdk.modules.Resources.Device_Type import DeviceTokenDataList
from tagoio_sdk.modules.Resources.Device_Type import ListDeviceTokenQuery
from tagoio_sdk.modules.Resources.Device_Type import TokenData
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Devices(TagoIOModule):
    def listDevice(self, queryObj: DeviceQuery = None) -> list[DeviceListItem]:
        """
        Retrieves a list with all devices from the account

        :default:

            queryObj: {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"],
                "resolveBucketName": False
            }

        :param DeviceQuery queryObj: Search query params
        """
        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            seccondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{seccondArgument}"
        else:
            orderBy = "name,asc"

        result = self.doRequest(
            {
                "path": "/device",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["id", "name"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": orderBy,
                    "resolveBucketName": queryObj.get("resolveBucketName") or False,
                },
            }
        )

        result = dateParserList(
            result,
            [
                "last_input",
                "last_output",
                "updated_at",
                "created_at",
                "inspected_at",
            ],
        )

        return result

    def create(self, deviceObj: DeviceCreateInfo) -> DeviceCreateResponse:
        """
        Generates and retrieves a new action from the Device

        :param DeviceCreateInfo deviceObj: Object data to create new device
        """
        result = self.doRequest(
            {
                "path": "/device",
                "method": "POST",
                "body": deviceObj,
            }
        )
        return result

    def edit(self, deviceID: GenericID, deviceObj: DeviceEditInfo) -> str:
        """
        Modify any property of the device

        :param GenericID deviceID: Device ID

        :param DeviceEditInfo deviceObj: Device object with fields to replace
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}",
                "method": "PUT",
                "body": deviceObj,
            }
        )
        return result

    def delete(self, deviceID: GenericID) -> str:
        """
        Deletes an device from the account

        :param GenericID deviceID: Device ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}",
                "method": "DELETE",
            }
        )
        return result

    def info(self, deviceID: GenericID) -> DeviceInfo:
        """
        Get Info of the Device

        :param GenericID deviceID: Device ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}",
                "method": "GET",
            }
        )

        result = dateParser(
            result,
            [
                "last_input",
                "last_output",
                "updated_at",
                "created_at",
                "inspected_at",
                "last_retention",
            ],
        )
        return result

    def paramSet(
        self,
        deviceID: GenericID,
        configObj: Union[ConfigurationParams, list[ConfigurationParams]],
        paramID: Optional[GenericID] = None,
    ) -> str:
        """
        Create or edit param for the Device

        :param deviceID Device ID

        :param configObj Configuration Data

        :param paramID Parameter ID
        """
        body = configObj
        if paramID and not isinstance(configObj, list):
            body = {
                "id": paramID,
                **configObj,
            }

        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/params",
                "method": "POST",
                "body": body,
            }
        )

        return result

    def paramList(
        self, deviceID: GenericID, sentStatus: bool = None
    ) -> list[ConfigurationParams]:
        """
        List Params for the Device

        :param GenericID deviceID: Device ID

        :param bool sentStatus: True return only sent=true, False return only sent=false
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/params",
                "method": "GET",
                "params": {"sent_status": sentStatus},
            }
        )
        return result

    def paramRemove(self, deviceID: GenericID, paramID: GenericID) -> str:
        """
        Remove param for the Device

        :param GenericID deviceID: Device ID

        :param GenericID paramID: Parameter ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/params/{paramID}",
                "method": "DELETE",
            }
        )
        return result

    def tokenList(
        self,
        deviceID: GenericID,
        queryObj: ListDeviceTokenQuery = None,
    ) -> list[DeviceTokenDataList]:
        """
        Retrieves a list of all tokens

        :default:

            queryObj: {
                "page": 1,
                "fields": ["name", "token", "permission"],
                "filter": {},
                "amount": 20,
                "orderBy": ["created_at", "desc"],
            }

        :param GenericID deviceID: Device ID

        :param ListDeviceTokenQuery queryObj: Search query params
        """

        if queryObj is None:
            queryObj = {}
        if "orderBy" in queryObj:
            firstArgument = queryObj["orderBy"][0]
            secondArgument = queryObj["orderBy"][1]
            orderBy = f"{firstArgument},{secondArgument}"
        else:
            orderBy = "created_at,desc"

        result = self.doRequest(
            {
                "path": f"/device/token/{deviceID}",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page") or 1,
                    "fields": queryObj.get("fields") or ["name", "token", "permission"],
                    "filter": queryObj.get("filter") or {},
                    "amount": queryObj.get("amount") or 20,
                    "orderBy": orderBy,
                },
            }
        )
        result = dateParserList(
            result, ["created_at", "last_authorization", "expire_time"]
        )

        return result

    def tokenCreate(
        self, deviceID: GenericID, tokenParams: TokenData
    ) -> TokenCreateResponse:
        """
        Generates and retrieves a new token

        :param deviceID: Device ID

        :param tokenParams: Params for new token
        """
        result = self.doRequest(
            {
                "path": "/device/token",
                "method": "POST",
                "body": {"device": deviceID, **tokenParams},
            }
        )
        result = dateParser(result, ["expire_date"])
        return result

    def tokenDelete(self, token: GenericToken) -> str:
        """
        Delete a token

        :param GenericToken token: Token
        """
        result = self.doRequest(
            {
                "path": f"/device/token/{token}",
                "method": "DELETE",
            }
        )
        return result

    def getDeviceData(
        self, deviceID: GenericID, queryParams: DataQuery = None
    ) -> list[Data]:
        """
        Get data from all variables in the device.

        :param deviceID: Device ID.

        :param queryParams: Query parameters to filter the results.

        :rtype: Array with the data values stored in the device.

        :example:

            myDevice = Account({ "token": "my_device_token" })

            result = myAccount.devices.getDeviceData(
                "Device Id", {"variables": "location"}
            )
        """
        if queryParams is None:
            queryParams = {}
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data",
                "method": "GET",
                "params": queryParams,
            }
        )
        return dateParserList(result, ["time", "created_at"])

    def emptyDeviceData(self, deviceID: GenericID) -> str:
        """
        Empty all data in a device.

        :param GenericID deviceID: Device ID.

        :rtype: Success message.
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/empty",
                "method": "POST",
            }
        )
        return result

    def sendDeviceData(
        self, deviceID: GenericID, data: Union[DataCreate, list[DataCreate]]
    ) -> str:
        """
        Send data to a device.

        :param GenericID deviceID: Device ID.

        :param DataCreate data: An array or one object with data to be send to TagoIO.

        :rtype: Success message.

        Example::
        ```python
        # Example of using the function
        resources = Resource()
        resource.devices.sendDeviceData("myDeviceID", {
            "variable": "temperature",
            "unit": "F",
            "value": 55,
            "time": "2015-11-03 13:44:33",
            "location": { "lat": 42.2974279, "lng": -85.628292 },
        })
        ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data",
                "method": "POST",
                "body": data,
            }
        )

        return result

    def editDeviceData(
        self, deviceID: GenericID, updatedData: Union[DataEdit, list[DataEdit]]
    ) -> str:
        """
        Edit data in a device.

        :param GenericID deviceID: Device ID.

        :param DataEdit data: A single or an array of updated data records.

        :rtype: Success message.

        Example::
        ```python
        # Example of using the function
        resources = Resource()
        resource.devices.editDeviceData("myDeviceID", {"id": "idOfTheRecord", "value": "new value", "unit": "new unit"})
        ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data",
                "method": "PUT",
                "body": updatedData,
            }
        )

        return result

    def deleteDeviceData(
        self, deviceID: GenericID, queryParam: DataQuery = None
    ) -> str:
        """
        Delete data from a device.

        :param GenericID deviceID: Device ID.

        :param DataQuery queryParam: Parameters to specify what should be deleted on the device's data.

        :rtype: Success message.

        Example::
        ```python
        # Example of using the function
        resources = Resource()
        resource.devices.deleteDeviceData("myDeviceID", {"ids": ["recordIdToDelete", "anotherRecordIdToDelete" ]})
        ```
        """
        if queryParam is None:
            queryParam = {}
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data",
                "method": "DELETE",
                "params": queryParam,
            }
        )

        return result

    def amount(self, deviceID: GenericID) -> Union[int, float]:
        """
        Get Amount of data stored in the Device
        :param deviceID: Device ID
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data_amount",
                "method": "GET",
            }
        )
        return result
