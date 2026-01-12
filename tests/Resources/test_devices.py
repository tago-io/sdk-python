import os

from typing import Any
from typing import Dict

from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


# Mock data generators
def mockDeviceList() -> Dict[str, Any]:
    """Generate mock device list response."""
    return {
        "status": True,
        "result": [
            {
                "id": "device-id-123",
                "name": "Temperature Sensor",
                "active": True,
                "type": "mutable",
                "last_input": "2025-01-09T10:00:00.000Z",
                "created_at": "2025-01-01T00:00:00.000Z",
            }
        ],
    }


def mockDeviceCreate() -> Dict[str, Any]:
    """Generate mock device create response."""
    return {
        "status": True,
        "result": {
            "device_id": "device-id-new",
            "bucket_id": "bucket-id-new",
            "token": "new-token-123",
        },
    }


def mockDeviceInfo() -> Dict[str, Any]:
    """Generate mock device info response."""
    return {
        "status": True,
        "result": {
            "id": "device-id-123",
            "name": "Temperature Sensor",
            "active": True,
            "type": "mutable",
            "bucket": {"id": "bucket-id-123", "name": "Device Data"},
            "network": "network-id-123",
            "connector": "connector-id-123",
            "last_input": "2025-01-09T10:00:00.000Z",
            "created_at": "2025-01-01T00:00:00.000Z",
        },
    }


def mockConfigParams() -> Dict[str, Any]:
    """Generate mock configuration parameters."""
    return {
        "status": True,
        "result": [
            {"id": "param-id-123", "key": "threshold", "value": "25.5", "sent": False}
        ],
    }


def mockTokenList() -> Dict[str, Any]:
    """Generate mock token list response."""
    return {
        "status": True,
        "result": [
            {
                "token": "token-123",
                "name": "Default Token",
                "permission": "full",
                "device_id": "device-id-123",
                "created_at": "2025-01-01T00:00:00.000Z",
            }
        ],
    }


def mockTokenCreate() -> Dict[str, Any]:
    """Generate mock token create response."""
    return {"status": True, "result": {"token": "new-token-456", "expire_date": None}}


def mockDeviceData() -> Dict[str, Any]:
    """Generate mock device data response."""
    return {
        "status": True,
        "result": [
            {
                "id": "data-id-123",
                "variable": "temperature",
                "value": 25.5,
                "unit": "°C",
                "time": "2025-01-09T10:00:00.000Z",
            }
        ],
    }


def mockChunkList() -> Dict[str, Any]:
    """Generate mock chunk list response."""
    return {
        "status": True,
        "result": [
            {
                "id": "1704067200_1706745600",
                "from_date": "2025-01-01T00:00:00.000Z",
                "to_date": "2025-02-01T00:00:00.000Z",
                "amount": 1000,
            }
        ],
    }


def mockBackupResponse() -> Dict[str, Any]:
    """Generate mock backup response."""
    return {
        "status": True,
        "result": {"file_address": "/backups/device-123/backup.csv"},
    }


def testSendDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post(
        f"https://api.tago.io/device/{deviceID}/data",
        json={"status": True, "result": "1 Data Added"},
    )

    resources = Resources()
    response = resources.devices.sendDeviceData(
        deviceID, {"variable": "test", "value": 1}
    )

    assert response == "1 Data Added"
    assert isinstance(response, str)


def testEditDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.put(
        f"https://api.tago.io/device/{deviceID}/data",
        json={"status": True, "result": "1 item(s) updated"},
    )

    resources = Resources()
    response = resources.devices.editDeviceData(
        deviceID, {"id": "idOfTheRecord", "value": "new value", "unit": "new unit"}
    )

    assert response == "1 item(s) updated"
    assert isinstance(response, str)


def testDeleteDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.delete(
        f"https://api.tago.io/device/{deviceID}/data",
        json={"status": True, "result": "2 Data Removed"},
    )

    resources = Resources()
    response = resources.devices.deleteDeviceData(
        deviceID, {"ids": ["recordIdToDelete", "anotherRecordIdToDelete"]}
    )

    assert response == "2 Data Removed"
    assert isinstance(response, str)


def testListDevice(requests_mock: Mocker) -> None:
    """Test listDevice method of Devices class."""
    mock_response = mockDeviceList()
    requests_mock.get("https://api.tago.io/device", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.listDevice({"page": 1, "amount": 20})

    assert isinstance(result, list)
    assert len(result) > 0
    assert result[0]["id"] == "device-id-123"


def testCreateDevice(requests_mock: Mocker) -> None:
    """Test create method of Devices class."""
    mock_response = mockDeviceCreate()
    requests_mock.post("https://api.tago.io/device", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.create(
        {
            "name": "New Device",
            "network": "network-id-123",
            "connector": "connector-id-123",
            "type": "mutable",
        }
    )

    assert result["device_id"] == "device-id-new"
    assert result["token"] == "new-token-123"


def testEditDevice(requests_mock: Mocker) -> None:
    """Test edit method of Devices class."""
    device_id = "device-id-123"
    requests_mock.put(
        f"https://api.tago.io/device/{device_id}",
        json={"status": True, "result": "Successfully Updated"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.edit(device_id, {"name": "Updated Name"})

    assert result == "Successfully Updated"


def testDeleteDevice(requests_mock: Mocker) -> None:
    """Test delete method of Devices class."""
    device_id = "device-id-123"
    requests_mock.delete(
        f"https://api.tago.io/device/{device_id}",
        json={"status": True, "result": "Successfully Removed"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.delete(device_id)

    assert result == "Successfully Removed"


def testDeviceInfo(requests_mock: Mocker) -> None:
    """Test info method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockDeviceInfo()
    requests_mock.get(f"https://api.tago.io/device/{device_id}", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.info(device_id)

    assert result["id"] == "device-id-123"
    assert result["name"] == "Temperature Sensor"


def testParamSet(requests_mock: Mocker) -> None:
    """Test paramSet method of Devices class."""
    device_id = "device-id-123"
    requests_mock.post(
        f"https://api.tago.io/device/{device_id}/params",
        json={"status": True, "result": "Successfully Updated"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.paramSet(
        device_id, {"key": "threshold", "value": "30", "sent": False}
    )

    assert result == "Successfully Updated"


def testParamList(requests_mock: Mocker) -> None:
    """Test paramList method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockConfigParams()
    requests_mock.get(
        f"https://api.tago.io/device/{device_id}/params", json=mock_response
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.paramList(device_id)

    assert isinstance(result, list)
    assert result[0]["key"] == "threshold"


def testParamRemove(requests_mock: Mocker) -> None:
    """Test paramRemove method of Devices class."""
    device_id = "device-id-123"
    param_id = "param-id-123"
    requests_mock.delete(
        f"https://api.tago.io/device/{device_id}/params/{param_id}",
        json={"status": True, "result": "Successfully Removed"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.paramRemove(device_id, param_id)

    assert result == "Successfully Removed"


def testTokenList(requests_mock: Mocker) -> None:
    """Test tokenList method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockTokenList()
    requests_mock.get(
        f"https://api.tago.io/device/token/{device_id}", json=mock_response
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.tokenList(device_id)

    assert isinstance(result, list)
    assert result[0]["token"] == "token-123"


def testTokenCreate(requests_mock: Mocker) -> None:
    """Test tokenCreate method of Devices class."""
    mock_response = mockTokenCreate()
    requests_mock.post("https://api.tago.io/device/token", json=mock_response)

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.tokenCreate(
        "device-id-123", {"name": "New Token", "permission": "write"}
    )

    assert result["token"] == "new-token-456"


def testTokenDelete(requests_mock: Mocker) -> None:
    """Test tokenDelete method of Devices class."""
    token = "token-to-delete"
    requests_mock.delete(
        f"https://api.tago.io/device/token/{token}",
        json={"status": True, "result": "Successfully Removed"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.tokenDelete(token)

    assert result == "Successfully Removed"


def testGetDeviceData(requests_mock: Mocker) -> None:
    """Test getDeviceData method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockDeviceData()
    requests_mock.get(
        f"https://api.tago.io/device/{device_id}/data", json=mock_response
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.getDeviceData(device_id, {"variables": ["temperature"]})

    assert isinstance(result, list)
    assert result[0]["variable"] == "temperature"


def testEmptyDeviceData(requests_mock: Mocker) -> None:
    """Test emptyDeviceData method of Devices class."""
    device_id = "device-id-123"
    requests_mock.post(
        f"https://api.tago.io/device/{device_id}/empty",
        json={"status": True, "result": "All data removed"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.emptyDeviceData(device_id)

    assert result == "All data removed"


def testAmount(requests_mock: Mocker) -> None:
    """Test amount method of Devices class."""
    device_id = "device-id-123"
    requests_mock.get(
        f"https://api.tago.io/device/{device_id}/data_amount",
        json={"status": True, "result": 15234},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.amount(device_id)

    assert result == 15234


def testGetChunk(requests_mock: Mocker) -> None:
    """Test getChunk method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockChunkList()
    requests_mock.get(
        f"https://api.tago.io/device/{device_id}/chunk", json=mock_response
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.getChunk(device_id)

    assert isinstance(result, list)
    assert result[0]["amount"] == 1000


def testDeleteChunk(requests_mock: Mocker) -> None:
    """Test deleteChunk method of Devices class."""
    device_id = "device-id-123"
    chunk_id = "chunk-id-456"
    requests_mock.delete(
        f"https://api.tago.io/device/{device_id}/chunk/{chunk_id}",
        json={"status": True, "result": f"Chunk {chunk_id} deleted"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.deleteChunk(device_id, chunk_id)

    assert result == f"Chunk {chunk_id} deleted"


def testDataBackup(requests_mock: Mocker) -> None:
    """Test dataBackup method of Devices class."""
    device_id = "device-id-123"
    mock_response = mockBackupResponse()
    requests_mock.post(
        f"https://api.tago.io/device/{device_id}/data/backup", json=mock_response
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.dataBackup(
        {"deviceID": device_id, "file_address": "/backups/backup.csv", "headers": True}
    )

    assert result["file_address"] == "/backups/device-123/backup.csv"


def testDataRestore(requests_mock: Mocker) -> None:
    """Test dataRestore method of Devices class."""
    device_id = "device-id-123"
    requests_mock.post(
        f"https://api.tago.io/device/{device_id}/data/restore",
        json={"status": True, "result": "Data import added to the queue successfully!"},
    )

    resources = Resources({"token": "your_token_value"})
    result = resources.devices.dataRestore(
        {"deviceID": device_id, "file_address": "/backups/restore.csv"}
    )

    assert result == "Data import added to the queue successfully!"
