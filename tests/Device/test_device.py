from faker.generator import Generator
from requests_mock.mocker import Mocker
from tests.conftest import (
    mockBodyCreateDevice,
    mockConfigurationParams,
    mockDeviceInfo,
    mockReturnGetData,
)
from src.tagoio_sdk.modules.Device.Device import Device


def testDeviceMethodInfo(
    faker: Generator, requests_mock: Mocker, mockDeviceInfo: mockDeviceInfo
):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockDeviceInfo is a fixture to return the object DeviceInfo.
    """

    requests_mock.get(
        "https://api.tago.io/info", json={"status": True, "result": mockDeviceInfo}
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).info()

    assert response == mockDeviceInfo
    assert isinstance(response, dict)


def testDeviceMethodSendData(
    faker: Generator, requests_mock: Mocker, mockBodyCreateDevice: mockBodyCreateDevice
):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockBodyCreateDevice is a fixture to return the object Data.
    """

    requests_mock.post(
        "https://api.tago.io/data", json={"status": True, "result": "1 Data Added"}
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).sendData(data=mockBodyCreateDevice)

    assert response == "1 Data Added"
    assert isinstance(response, str)


def testDeviceMethodGetData(
    faker: Generator, requests_mock: Mocker, mockReturnGetData: mockReturnGetData
):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockReturnGetData is a fixture to return the object Data.
    """

    requests_mock.get(
        "https://api.tago.io/data", json={"status": True, "result": mockReturnGetData}
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).getData()

    assert len(response) == 10
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testDeviceMethodEditData(faker: Generator, requests_mock: Mocker):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.put(
        "https://api.tago.io/data", json={"status": True, "result": "1 item(s) updated"}
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).editData(
        data=[{"id": faker.pystr(), "value": 66}]
    )

    assert response == "1 item(s) updated"
    assert isinstance(response, str)


def testDeviceMethodDeleteData(faker: Generator, requests_mock: Mocker):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.delete(
        "https://api.tago.io/data", json={"status": True, "result": "1 Data Removed"}
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).deleteData(queryParams=None)

    assert response == "1 Data Removed"
    assert isinstance(response, str)


def testDeviceMethodGetParameters(
    faker: Generator,
    requests_mock: Mocker,
    mockConfigurationParams: mockConfigurationParams,
):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    :param mockConfigurationParams is a fixture to return the object ConfigurationParams.
    """

    requests_mock.get(
        "https://api.tago.io/device/params",
        json={"status": True, "result": [mockConfigurationParams]},
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).getParameters()

    assert response[0] == mockConfigurationParams
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testDeviceMethodSetParameterAsRead(faker: Generator, requests_mock: Mocker):
    """
    :param faker are a plugin of pytest to generate fake data.
    :param requests_mock are a plugin of pytest to mock the requests.
    """

    requests_mock.put(
        "https://api.tago.io/device/params/63f66cf4b26aff0009cd2a2e",
        json={"status": True, "result": "Params Successfully Updated"},
    )

    tokenFake = {"token": faker.pystr()}
    response = Device(params=tokenFake).setParameterAsRead(
        parameterID="63f66cf4b26aff0009cd2a2e"
    )

    assert response == "Params Successfully Updated"
    assert isinstance(response, str)
