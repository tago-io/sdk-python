import requests
from typing import Union

from tagoio_sdk.modules.Resources.AccountDeprecated import AccountDeprecated as Account
from tagoio_sdk.modules.Resources.Resources import Resources
from tagoio_sdk.modules.Resources.Device_Type import (
    ConfigurationParams,
    DeviceTokenDataList,
)
from tagoio_sdk.modules.Utils.utilsType import DownlinkOptions


def getDeviceToken(
    resource: Union[Account, Resources], device_id: str
) -> DeviceTokenDataList:
    """Get the token of a device.

    Returns:
        str: token of the device
    """
    device_tokens = resource.devices.tokenList(
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


def getNetworkId(resource: Union[Account, Resources], device_id: str) -> str:
    """Get the network id of a device.

    Returns:
        str: network id of the device
    """
    device = resource.devices.info(device_id)
    if not device.get("network"):
        raise ValueError("Device is not using a network.")

    return device["network"]


def getMiddlewareEndpoint(resource: Union[Account, Resources], network_id: str) -> str:
    """Get the middleware endpoint of a device.

    Returns:
        str: middleware endpoint of the device
    """
    network = resource.integration.networks.info(
        network_id, ["id", "middleware_endpoint", "name"]
    )
    if not network.get("middleware_endpoint"):
        raise TypeError("This device network doesn't support downlinks.")

    return network["middleware_endpoint"]


def getDownlinkParams(
    resource: Union[Account, Resources], device_id: str
) -> list[ConfigurationParams] | list[None]:
    """Get the downlink parameters of a device.

    Returns:
        str: downlink parameters of the device
    """
    params = resource.devices.paramList(deviceID=device_id)
    downlink_param = list(filter(lambda param: param["key"] == "downlink", params))

    return downlink_param


def putParamInDevice(
    resource: Union[Account, Resources], device_id: str, param_obj: ConfigurationParams
) -> None:
    """Put the downlink parameter in the device."""

    resource.devices.paramSet(deviceID=device_id, configObj=param_obj)


def sendDownlink(
    resource: Union[Account, Resources], device_id: str, dn_options: DownlinkOptions
) -> str:
    """Perform downlink to a device using official TagoIO support.

    Args:
        resource (Account or Resources): resource TagoIO SDK Account or Resources instanced class
        device_id (str): device_id id of your device
        dn_options (DownlinkOptions): dn_options downlink parameter options.
    """
    if not isinstance(resource, Account) and not isinstance(resource, Resources):
        raise TypeError(
            "The parameter 'account' must be an instance of a TagoIO Resources."
        )

    token = getDeviceToken(resource=resource, device_id=device_id)
    network_id = getNetworkId(resource=resource, device_id=device_id)
    middleware_endpoint = getMiddlewareEndpoint(
        resource=resource, network_id=network_id
    )
    downlink_param = getDownlinkParams(resource=resource, device_id=device_id)
    param_obj = {
        "id": downlink_param[0]["id"] if downlink_param else None,
        "key": "downlink",
        "value": str(dn_options["payload"]),
        "sent": False,
    }
    putParamInDevice(resource=resource, device_id=device_id, param_obj=param_obj)

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
