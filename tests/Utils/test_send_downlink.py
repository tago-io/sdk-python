import pytest
from requests_mock.mocker import Mocker
from tagoio_sdk.modules.Account.Device_Type import (
    ConfigurationParams,
    DeviceTokenDataList,
)
from tagoio_sdk.modules.Utils.sendDownlink import (
    getDeviceToken,
    getDownlinkParams,
    getMiddlewareEndpoint,
    getNetworkId,
    sendDownlink,
)
from tagoio_sdk.modules.Account.Account import Account


def mockDeviceToken() -> list[DeviceTokenDataList]:
    """Mock to return the list of DeviceTokenDataList."""
    return {
        "status": True,
        "result": [
            {
                "name": "Default",
                "serie_number": "0000000000000000",
                "last_authorization": None,
            }
        ],
    }


def mockConfigurationParams() -> list[ConfigurationParams]:
    """Mock to return the list of ConfigurationParams."""
    return {
        "status": True,
        "result": [
            {
                "id": "6400fcf41f1ee8000913e6df",
                "key": "123",
                "value": "213",
                "sent": False,
            },
            {
                "id": "64020577ad714b00093b9b20",
                "key": "downlink",
                "value": "test",
                "sent": False,
            },
        ],
    }


def testMethodGetDeviceTokenSuccessfully(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    params_url = (
        "?page=1&fields=name&fields=serie_number&fields=last_authorization&amount=10"
    )
    requests_mock.get(
        f"https://api.tago.io/device/token/{deviceID}{params_url}",
        json=mockDeviceToken(),
    )

    my_account = Account({"token": "fake_token"})
    response = getDeviceToken(account=my_account, device_id=deviceID)

    assert response == mockDeviceToken()["result"][0]
    assert isinstance(response, dict)


def testMethodGetDeviceTokenFail(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    params_url = (
        "?page=1&fields=name&fields=serie_number&fields=last_authorization&amount=10"
    )
    requests_mock.get(
        f"https://api.tago.io/device/token/{deviceID}{params_url}",
        json={"status": True, "result": []},
    )

    my_account = Account({"token": "fake_token"})
    with pytest.raises(TypeError):
        getDeviceToken(account=my_account, device_id=deviceID)


def testMethodGetNetworkIdSuccessfully(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}",
        json={"status": True, "result": {"network": "fake_network_id"}},
    )

    my_account = Account({"token": "fake_token"})
    response = getNetworkId(account=my_account, device_id=deviceID)

    assert response == "fake_network_id"
    assert isinstance(response, str)


def testMethodGetNetworkIdFail(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}",
        json={"status": True, "result": {}},
    )

    my_account = Account({"token": "fake_token"})
    with pytest.raises(ValueError):
        getNetworkId(account=my_account, device_id=deviceID)


def testMethodGetMiddlewareEndpointSuccessfully(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}",
        json={"status": True, "result": {"middleware_endpoint": "fake_endpoint"}},
    )

    my_account = Account({"token": "fake_token"})
    response = getMiddlewareEndpoint(account=my_account, network_id=networkID)

    assert response == "fake_endpoint"
    assert isinstance(response, str)


def testMethodGetMiddlewareEndpointFail(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}",
        json={"status": True, "result": {}},
    )

    my_account = Account({"token": "fake_token"})
    with pytest.raises(TypeError):
        getMiddlewareEndpoint(account=my_account, network_id=networkID)


def testMethodGetDownlinkParamsSuccessfully(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}/params",
        json=mockConfigurationParams(),
    )

    my_account = Account({"token": "fake_token"})
    response = getDownlinkParams(account=my_account, device_id=deviceID)

    assert response[0] == mockConfigurationParams()["result"][1]
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def testMethodGetDownlinkParamsEmptyList(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}/params",
        json={"status": True, "result": []},
    )

    my_account = Account({"token": "fake_token"})
    response = getDownlinkParams(account=my_account, device_id=deviceID)

    assert response == []


def testMethodSendDownlinkSuccessfully(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.post(
        f"https://api.tago.io/device/{deviceID}/params",
        json={"status": True, "result": "Params Successfully Updated"},
    )
    params_url = (
        "?page=1&fields=name&fields=serie_number&fields=last_authorization&amount=10"
    )
    requests_mock.get(
        f"https://api.tago.io/device/token/{deviceID}{params_url}",
        json=mockDeviceToken(),
    )
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}",
        json={"status": True, "result": {"network": "fake_network_id"}},
    )
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}/params",
        json=mockConfigurationParams(),
    )
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}",
        json={"status": True, "result": {"middleware_endpoint": "fake_endpoint"}},
    )

    requests_mock.post("https://fake_endpoint/downlink", status_code=200)

    my_account = Account({"token": "fake_token"})
    response = sendDownlink(
        account=my_account,
        device_id=deviceID,
        dn_options={"payload": "test", "port": 123},
    )

    assert response == "Downlink accepted with status code - 200"
    assert isinstance(response, str)


def testMethodSendDownlinkFail(requests_mock: Mocker):
    """
    :param requests_mock are a plugin of pytest to mock the requests.
    """
    deviceID = "fake_device_id"
    requests_mock.post(
        f"https://api.tago.io/device/{deviceID}/params",
        json={"status": True, "result": "Params Successfully Updated"},
    )
    params_url = (
        "?page=1&fields=name&fields=serie_number&fields=last_authorization&amount=10"
    )
    requests_mock.get(
        f"https://api.tago.io/device/token/{deviceID}{params_url}",
        json=mockDeviceToken(),
    )
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}",
        json={"status": True, "result": {"network": "fake_network_id"}},
    )
    requests_mock.get(
        f"https://api.tago.io/device/{deviceID}/params",
        json=mockConfigurationParams(),
    )
    networkID = "fake_network_id"
    requests_mock.get(
        f"https://api.tago.io/integration/network/{networkID}",
        json={"status": True, "result": {"middleware_endpoint": "fake_endpoint"}},
    )

    requests_mock.post("https://fake_endpoint/downlink", status_code=422)

    my_account = Account({"token": "fake_token"})
    with pytest.raises(TypeError):
        sendDownlink(
            account=my_account,
            device_id=deviceID,
            dn_options={"payload": "test", "port": 123},
        )


def testMethodSendDownlinkFailWrongInstanceOfAccount():
    my_account = "fake_account"
    deviceID = "fake_device_id"
    with pytest.raises(TypeError):
        sendDownlink(
            account=my_account,
            device_id=deviceID,
            dn_options={"payload": "test", "port": 123},
        )