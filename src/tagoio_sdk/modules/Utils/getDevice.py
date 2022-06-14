from tagoio_sdk.modules.Device.Device import Device
from tagoio_sdk.modules.Account.Account import Account
from tagoio_sdk.modules.Utils.getTokenByName import getTokenByName


def getDevice(account: Account, device_id: str) -> Device:
    """
    Get the TagoIO Device instanced class from a device id
    """
    if (isinstance(account, Account)) is False:
        raise ValueError(
            "The parameter 'account' must be an instance of a TagoIO Account."
        )

    token = getTokenByName(account, device_id)

    if token is None:
        raise ValueError(f"Token not found for the device id {device_id}")

    device = Device({"token": token})

    return device
