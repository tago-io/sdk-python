import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.types import ConfigurationParams, DeviceCreateResponse, DeviceListItem, DeviceTokenDataList, DeviceInfo, Data, TokenCreateResponse


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def mockDeviceList() -> list[DeviceListItem]:
    return {
        "status": True,
        "result": [
            {
                "id": "device1",
                "name": "Device 1",
                "type": "mutable",
                "profile": "profile_id",
                "created_at": "2023-02-21T15:17:35.880Z",
                "updated_at": "2023-02-21T15:17:35.880Z",
                "bucket": "bucket_id"
            }
        ]
    }


def testDeviceListMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.get("https://api.tago.io/device", json=mockDeviceList())

    resources = Resources()
    response = resources.devices.listDevice()

    assert response[0]["id"] == mockDeviceList()["result"][0]["id"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def mockDeviceCreate() -> DeviceCreateResponse:
    return {
        "status": True,
        "result": {
            "device_id": "mock_device_id",
            "bucket_id": "mock_bucket_id",
            "token": "mock_token",
        }
    }


def testDeviceCreateMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.post("https://api.tago.io/device", json=mockDeviceCreate())

    deviceObj = {
        "name": "device1",
        "type": "mutable",
        "network": "mock_network_id",
        "connector": "mock_connector_id",
        "serie_number": "mock_serie_number_id",
    }
    resources = Resources()
    response = resources.devices.create(deviceObj)

    assert response == mockDeviceCreate()["result"]
    assert isinstance(response, dict)


def testDeviceEditMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.put(f"https://api.tago.io/device/{deviceID}", json={"status": True, "result": "Successfully Updated"})

    deviceObj = {"tags": [{"key": "my_tag_key", "value": "my_tag_value"}]}
    resources = Resources()
    response = resources.devices.edit(deviceID, deviceObj)

    assert response == "Successfully Updated"
    assert isinstance(response, str)


def testDeviceDeleteMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.delete(f"https://api.tago.io/device/{deviceID}", json={"status": True, "result": "Successfully Removed"})

    resources = Resources()
    response = resources.devices.delete(deviceID)

    assert response == "Successfully Removed"
    assert isinstance(response, str)


def mockDeviceInfo() -> DeviceInfo:
    return {
        "status": True,
        "result": {
            "id": "device1",
            "profile": "profile_id",
            "name": "Device 1",
            "description": "Device 1 description",
            "visible": True,
        }
    }


def testDeviceInfoMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.get(f"https://api.tago.io/device/{deviceID}", json=mockDeviceInfo())

    resources = Resources()
    response = resources.devices.info(deviceID)

    assert response == mockDeviceInfo()["result"]
    assert isinstance(response, dict)


def testParamSetMethodMultipleConfigurationParams(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post(f"https://api.tago.io/device/{deviceID}/params", json={"status": True, "result": "Params Successfully Updated"})

    configObj = [{"key": "key1", "value": "value1"}, {"key": "key2", "value": "value2"}]
    resources = Resources()
    response = resources.devices.paramSet(deviceID, configObj)

    assert response == "Params Successfully Updated"
    assert isinstance(response, str)


def testParamSetMethodSingleConfigurationParams(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post(f"https://api.tago.io/device/{deviceID}/params", json={"status": True, "result": "Params Successfully Updated"})

    configObj = {"key": "key1", "value": "value1"}
    resources = Resources()
    response = resources.devices.paramSet(deviceID, configObj)

    assert response == "Params Successfully Updated"
    assert isinstance(response, str)


def mockParamList() -> list[ConfigurationParams]:
    return {
        "status": True,
        "result": [
            {
                "id": "param1",
                "key": "key1",
                "value": "value1",
                "sent": True,
            }
        ]
    }


def testParamListMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.get(f"https://api.tago.io/device/{deviceID}/params", json=mockParamList())

    resources = Resources()
    response = resources.devices.paramList(deviceID, sentStatus=True)

    assert response == mockParamList()["result"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testParamRemoveMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    paramID = "param1"
    requests_mock.delete(f"https://api.tago.io/device/{deviceID}/params/{paramID}", json={"status": True, "result": "Successfully Removed"})

    resources = Resources()
    response = resources.devices.paramRemove(deviceID, paramID)

    assert response == "Successfully Removed"
    assert isinstance(response, str)


def mockTokenList() -> list[DeviceTokenDataList]:
    return {
        "status": True,
        "result": [
            {
                "name": "token1",
                "token": "token_value1",
                "permission": "full",
                "created_at": "2023-02-21T15:17:35.880Z",
                "last_authorization": "2023-02-21T15:17:35.880Z",
                "expire_time": "2023-02-21T15:17:35.880Z",
            }
        ]
    }


def testTokenListMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.get(f"https://api.tago.io/device/token/{deviceID}", json=mockTokenList())

    resources = Resources()
    response = resources.devices.tokenList(deviceID)

    assert response[0]["token"] == mockTokenList()["result"][0]["token"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def mockTokenCreate() -> TokenCreateResponse:
    return {
        "status": True,
        "result": {
            "token": "token_value1",
            "permission": "full",
            "expire_date": "2023-02-21T15:17:35.880Z",
        }
    }


def testTokenCreateMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post("https://api.tago.io/device/token", json=mockTokenCreate())

    tokenParams = {"name": "token1", "permission": "full", "expire_time": "2023-02-21T15:17:35.880Z"}
    resources = Resources()
    response = resources.devices.tokenCreate(deviceID, tokenParams)

    assert response["token"] == mockTokenCreate()["result"]["token"]
    assert response["permission"] == mockTokenCreate()["result"]["permission"]
    assert isinstance(response, dict)


def testTokenDeleteMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    tokenToDelete = "token_value1"
    requests_mock.delete(f"https://api.tago.io/device/token/{tokenToDelete}", json={"status": True, "result": "Token Successfully Removed"})

    resources = Resources()
    response = resources.devices.tokenDelete(tokenToDelete)

    assert response == "Token Successfully Removed"
    assert isinstance(response, str)


def mockGetDeviceData() -> list[Data]:
    return {
        "status": True,
        "result": [
            {
                "id": "data1",
                "device": "device1",
                "variable": "temperature",
                "value": 22.5,
                "group": "group1",
                "time": "2023-02-21T15:17:35.880Z",
                "created_at": "2023-02-21T15:17:35.880Z",
            }
        ]
    }


def testGetDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.get(f"https://api.tago.io/device/{deviceID}/data", json=mockGetDeviceData())

    queryParams = {"variables": "temperature", "qty": 1}
    resources = Resources()
    response = resources.devices.getDeviceData(deviceID, queryParams)

    assert response[0]["group"] == mockGetDeviceData()["result"][0]["group"]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testEmptyDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post(f"https://api.tago.io/device/{deviceID}/empty", json={"status": True, "result": "Data Successfully Removed"})

    resources = Resources()
    response = resources.devices.emptyDeviceData(deviceID)

    assert response == "Data Successfully Removed"
    assert isinstance(response, str)
