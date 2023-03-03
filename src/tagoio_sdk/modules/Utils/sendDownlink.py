import requests
from tagoio_sdk.modules.Account.Account import Account
from tagoio_sdk.modules.Account.Device_Type import (
    ConfigurationParams,
    DeviceTokenDataList,
)
from tagoio_sdk.modules.Utils.utilsType import DownlinkOptions


def getDeviceToken(account: Account, device_id: str) -> DeviceTokenDataList:
    """Get the token of a device.

    Returns:
        str: token of the device
    """
    device_tokens = account.devices.tokenList(
        device_id,
        {
            "page": 1,
            "fields": ["name", "serie_number", "last_authorization"],
            "amount": 10,
        },
    )

    if not device_tokens:
        raise TypeError("Device doesn't have any token.")

    for token in device_tokens:
        if (
            token["serie_number"] is not None
            and token["last_authorization"] is not None
        ):
            return token

    raise TypeError(
        "Can't perform the downlink. Wait for at least 1 uplink from the NS to use"
        " this operation."
    )


def getNetworkId(account: Account, device_id: str) -> str:
    """Get the network id of a device.

    Returns:
        str: network id of the device
    """
    device = account.devices.info(device_id)
    if not device.get("network"):
        raise ValueError("Device is not using a network.")

    return device["network"]


def getMiddlewareEndpoint(account: Account, network_id: str) -> str:
    """Get the middleware endpoint of a device.

    Returns:
        str: middleware endpoint of the device
    """
    network = account.integration.networks.info(
        network_id, ["id", "middleware_endpoint", "name"]
    )
    if not network.get("middleware_endpoint"):
        raise TypeError("This device network doesn't support downlinks.")

    return network["middleware_endpoint"]


def getDownlinkParams(
    account: Account, device_id: str
) -> list[ConfigurationParams] | list[None]:
    """Get the downlink parameters of a device.

    Returns:
        str: downlink parameters of the device
    """
    params = account.devices.paramList(deviceID=device_id)
    downlink_param = list(filter(lambda param: param["key"] == "downlink", params))

    return downlink_param


def putParamInDevice(
    account: Account, device_id: str, param_obj: ConfigurationParams
) -> None:
    """Put the downlink parameter in the device."""

    account.devices.paramSet(deviceID=device_id, configObj=param_obj)


def sendDownlink(account: Account, device_id: str, dn_options: DownlinkOptions) -> str:
    """Perform downlink to a device using official TagoIO support.

    Args:
        account (Account): account TagoIO SDK Account instanced class
        device_id (str): device_id id of your device
        dn_options (DownlinkOptions): dn_options downlink parameter options.
    """
    if not isinstance(account, Account):
        raise TypeError(
            "The parameter 'account' must be an instance of a TagoIO Account."
        )

    token = getDeviceToken(account=account, device_id=device_id)
    network_id = getNetworkId(account=account, device_id=device_id)
    middleware_endpoint = getMiddlewareEndpoint(account=account, network_id=network_id)
    downlink_param = getDownlinkParams(account=account, device_id=device_id)
    param_obj = {
        "id": downlink_param[0]["id"] if downlink_param else None,
        "key": "downlink",
        "value": str(dn_options["payload"]),
        "sent": False,
    }
    putParamInDevice(account=account, device_id=device_id, param_obj=param_obj)

    data = {
        "device": token["serie_number"],
        "authorization": token["last_authorization"],
        "payload": dn_options["payload"],
        "port": dn_options["port"],
    }

    result = requests.post(f"https://{middleware_endpoint}/downlink", data)

    if result.status_code in range(400, 500):
        raise TypeError(
            f"Downlink failed with status {result.status_code}: {result.text}"
        )

    return f"Downlink accepted with status code - {result.status_code}"
