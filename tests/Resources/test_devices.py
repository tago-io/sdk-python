import os
from requests_mock.mocker import Mocker

from tagoio_sdk.modules.Resources.Resources import Resources


os.environ["T_ANALYSIS_TOKEN"] = "your_token_value"


def testSendDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.post(f"https://api.tago.io/device/{deviceID}/data",
                       json={"status": True, "result": "1 Data Added"})

    resources = Resources()
    response = resources.devices.sendDeviceData(deviceID, {"variable": "test",  "value": 1})

    assert response == "1 Data Added"
    assert isinstance(response, str)


def testEditDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.put(f"https://api.tago.io/device/{deviceID}/data",
                      json={"status": True, "result": "1 item(s) updated"})

    resources = Resources()
    response = resources.devices.editDeviceData(deviceID,  {"id": "idOfTheRecord", "value": "new value", "unit": "new unit"})

    assert response == "1 item(s) updated"
    assert isinstance(response, str)


def testDeleteDeviceDataMethod(requests_mock: Mocker) -> None:
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    deviceID = "device1"
    requests_mock.delete(f"https://api.tago.io/device/{deviceID}/data",
                         json={"status": True, "result": "2 Data Removed"})

    resources = Resources()
    response = resources.devices.deleteDeviceData(deviceID,  {"ids": ["recordIdToDelete", "anotherRecordIdToDelete"]})

    assert response == "2 Data Removed"
    assert isinstance(response, str)
