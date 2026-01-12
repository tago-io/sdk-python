from typing import List
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
from tagoio_sdk.modules.Resources.Device_Type import DeviceChunkData
from tagoio_sdk.modules.Resources.Device_Type import DeviceCreateInfo
from tagoio_sdk.modules.Resources.Device_Type import DeviceCreateResponse
from tagoio_sdk.modules.Resources.Device_Type import DeviceDataBackup
from tagoio_sdk.modules.Resources.Device_Type import DeviceDataBackupResponse
from tagoio_sdk.modules.Resources.Device_Type import DeviceDataRestore
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
        @description:
            Retrieves a list of all devices from the account with optional filtering and pagination.

        @see:
            https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            devices = resources.devices.listDevice({
                "page": 1,
                "amount": 20,
                "fields": ["id", "name", "active"],
                "filter": {"name": "Temperature*"},
                "orderBy": ["name", "asc"]
            })
            print(devices)  # [{'id': 'device-id-123', 'name': 'Temperature Sensor', ...}]
            ```
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
        @description:
            Creates a new device in the account with specified configuration and returns device credentials.

        @see:
            https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview
            https://help.tago.io/portal/en/kb/articles/481-device-types Device Types

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.create({
                "name": "Temperature Sensor",
                "network": "network-id-123",
                "connector": "connector-id-456",
                "type": "immutable",
                "chunk_period": "month",
                "chunk_retention": 6,
                "active": True
            })
            print(result)  # {'device_id': '...', 'bucket_id': '...', 'token': '...'}
            ```
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
        @description:
            Modifies any property of an existing device.

        @see:
            https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.edit("device-id-123", {
                "name": "Updated Sensor Name",
                "active": False,
                "tags": [{"key": "location", "value": "warehouse"}]
            })
            print(result)  # Successfully Updated
            ```
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
        @description:
            Permanently deletes a device from the account along with all its data.

        @see:
            https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.delete("device-id-123")
            print(result)  # Successfully Removed
            ```
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
        @description:
            Retrieves detailed information about a specific device.

        @see:
            https://help.tago.io/portal/en/kb/articles/478-devices Devices Overview

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            device_info = resources.devices.info("device-id-123")
            print(device_info)  # {'id': '...', 'name': '...', 'type': 'mutable', ...}
            ```
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
        @description:
            Creates new configuration parameters or updates existing ones for a device.

        @see:
            https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            # Create new parameter
            result = resources.devices.paramSet("device-id-123", {
                "key": "threshold",
                "value": "25.5",
                "sent": False
            })
            # Update existing parameter
            result = resources.devices.paramSet("device-id-123", {
                "key": "threshold",
                "value": "30.0",
                "sent": False
            }, "param-id-456")
            print(result)  # Successfully Updated
            ```
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

    def paramList(self, deviceID: GenericID, sentStatus: bool = None) -> list[ConfigurationParams]:
        """
        @description:
            Retrieves a list of configuration parameters for a device.

        @see:
            https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            # Get all parameters
            params = resources.devices.paramList("device-id-123")
            # Get only sent parameters
            sent_params = resources.devices.paramList("device-id-123", sentStatus=True)
            print(params)  # [{'id': '...', 'key': 'threshold', 'value': '25.5', 'sent': False}]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/params",
                "method": "GET",
                "params": {"sent_status": str(sentStatus).lower() if sentStatus is not None else None},
            }
        )
        return result

    def paramRemove(self, deviceID: GenericID, paramID: GenericID) -> str:
        """
        @description:
            Removes a specific configuration parameter from a device.

        @see:
            https://help.tago.io/portal/en/kb/articles/configuration-parameters Configuration Parameters

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.paramRemove("device-id-123", "param-id-456")
            print(result)  # Successfully Removed
            ```
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
        @description:
            Retrieves a list of all authentication tokens for a device with optional filtering.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            tokens = resources.devices.tokenList("device-id-123", {
                "page": 1,
                "amount": 20,
                "fields": ["name", "token", "permission"],
                "orderBy": ["created_at", "desc"]
            })
            print(tokens)  # [{'name': 'Default Token', 'token': '...', 'permission': 'full', ...}]
            ```
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
        result = dateParserList(result, ["created_at", "expire_time"])

        return result

    def tokenCreate(self, deviceID: GenericID, tokenParams: TokenData) -> TokenCreateResponse:
        """
        @description:
            Generates and retrieves a new authentication token for a device.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Create Token** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.tokenCreate("device-id-123", {
                "name": "Production Token",
                "permission": "write",
                "expire_time": "never"
            })
            print(result)  # {'token': 'new-token-value', 'expire_date': None}
            ```
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
        @description:
            Permanently deletes an authentication token.

        @see:
            https://help.tago.io/portal/en/kb/articles/495-access-tokens Device Tokens

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Delete Token** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.tokenDelete("token-to-delete")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/token/{token}",
                "method": "DELETE",
            }
        )
        return result

    def getDeviceData(self, deviceID: GenericID, queryParams: DataQuery = None) -> list[Data]:
        """
        @description:
            Retrieves data from all variables in the device with optional query filters.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            # Get all data
            data = resources.devices.getDeviceData("device-id-123")
            # Get specific variable data
            temp_data = resources.devices.getDeviceData("device-id-123", {
                "variables": ["temperature"],
                "qty": 10
            })
            print(temp_data)  # [{'variable': 'temperature', 'value': 25.5, 'time': '...', ...}]
            ```
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
        @description:
            Permanently removes all data from a device. This operation cannot be undone.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.emptyDeviceData("device-id-123")
            print(result)  # All data has been removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/empty",
                "method": "POST",
            }
        )
        return result

    def sendDeviceData(self, deviceID: GenericID, data: Union[DataCreate, list[DataCreate]]) -> str:
        """
        @description:
            Sends data to a device. Accepts a single data object or an array of data objects.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.sendDeviceData("device-id-123", {
                "variable": "temperature",
                "value": 25.5,
                "unit": "°C",
                "time": "2025-01-09 13:44:33",
                "location": {"lat": 42.2974279, "lng": -85.628292}
            })
            # Send multiple data points
            result = resources.devices.sendDeviceData("device-id-123", [
                {"variable": "temperature", "value": 25.5},
                {"variable": "humidity", "value": 60}
            ])
            print(result)  # Successfully Inserted
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

    def editDeviceData(self, deviceID: GenericID, updatedData: Union[DataEdit, list[DataEdit]]) -> str:
        """
        @description:
            Modifies existing data records in a device. Requires the data record ID.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.editDeviceData("device-id-123", {
                "id": "data-record-id",
                "value": 30.0,
                "unit": "°F"
            })
            # Edit multiple records
            result = resources.devices.editDeviceData("device-id-123", [
                {"id": "record-1-id", "value": 25.5},
                {"id": "record-2-id", "value": 65}
            ])
            print(result)  # Device Data Updated
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

    def deleteDeviceData(self, deviceID: GenericID, queryParam: DataQuery = None) -> str:
        """
        @description:
            Deletes data from a device based on specified query parameters.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Edit** in Access Management.
            ```python
            resources = Resources()
            # Delete specific records by ID
            result = resources.devices.deleteDeviceData("device-id-123", {
                "ids": ["record-id-1", "record-id-2"]
            })
            # Delete by variable
            result = resources.devices.deleteDeviceData("device-id-123", {
                "variables": ["old_sensor"],
                "qty": 100
            })
            print(result)  # Successfully Removed
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
        @description:
            Gets the amount of data stored in a device.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data Device Data Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Access** in Access Management.
            ```python
            resources = Resources()
            amount = resources.devices.amount("device-id-123")
            print(amount)  # 15234
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/data_amount",
                "method": "GET",
            }
        )
        return result

    def getChunk(self, deviceID: GenericID) -> List[DeviceChunkData]:
        """
        @description:
            Retrieves chunk information from an immutable device.

        @see:
            https://help.tago.io/portal/en/kb/articles/chunk-management Chunk Management

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Manage chunks** in Access Management.
            ```python
            resources = Resources()
            chunks = resources.devices.getChunk("device-id-123")
            print(chunks)  # [{'amount': 0, 'id': 'chunk-id-123', 'from_date': '2025-01-09T00:00:00.000+00:00', ...}]
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/chunk",
                "method": "GET",
            }
        )

        return result

    def deleteChunk(self, deviceID: GenericID, chunkID: GenericID) -> str:
        """
        @description:
            Deletes a chunk from an immutable device.

        @see:
            https://help.tago.io/portal/en/kb/articles/chunk-management#Delete_chunks Delete Chunks

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Manage chunks** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.deleteChunk("device-id-123", "chunk-id-123")
            print(result)  # Chunk chunk-id-123 deleted
            ```
        """
        result = self.doRequest(
            {
                "path": f"/device/{deviceID}/chunk/{chunkID}",
                "method": "DELETE",
            }
        )

        return result

    def dataBackup(self, params: DeviceDataBackup, chunkID: Optional[GenericID] = None) -> DeviceDataBackupResponse:
        """
        @description:
            Schedule to export the device's data to TagoIO Files.
            For mutable devices, exports all data. For immutable devices with chunkID, exports specific chunk.

        @see:
            https://help.tago.io/portal/en/kb/articles/55-data-export Data Export
            https://help.tago.io/portal/en/kb/articles/device-data#Backing_Up_Data Backing Up Data

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Export Data** in Access Management.
            ```python
            resources = Resources()
            import time
            timestamp = int(time.time())
            result = resources.devices.dataBackup({
                "deviceID": "device-id-123",
                "file_address": f"/backups/device-id-123/{timestamp}",
                "headers": True
            })
            print(result)  # {'file_address': 'backups/device-id-123/1736433519380.csv'}
            ```
        """
        body = {
            "chunk_id": chunkID,
            "headers": params.get("headers"),
            "file_address": params.get("file_address"),
        }

        path = f"/device/{params['deviceID']}/chunk/backup" if chunkID else f"/device/{params['deviceID']}/data/backup"

        result = self.doRequest(
            {
                "path": path,
                "method": "POST",
                "body": body,
            }
        )

        return result

    def dataRestore(self, params: DeviceDataRestore) -> str:
        """
        @description:
            Restores data to a device from a CSV file in TagoIO Files.

        @see:
            https://help.tago.io/portal/en/kb/articles/device-data#Importing Importing Device Data
            https://api.docs.tago.io/#7ebca255-6c38-43d3-97d0-9b62155f202e Import Data API

        @example:
            If receive an error "Authorization Denied", check policy **Device** / **Import Data** in Access Management.
            ```python
            resources = Resources()
            result = resources.devices.dataRestore({
                "deviceID": "device-id-123",
                "file_address": "/backups/backup.csv"
            })
            print(result)  # Data import added to the queue successfully!
            ```
        """
        body = {
            "file_address": params.get("file_address"),
        }

        result = self.doRequest(
            {
                "path": f"/device/{params['deviceID']}/data/restore",
                "method": "POST",
                "body": body,
            }
        )

        return result
