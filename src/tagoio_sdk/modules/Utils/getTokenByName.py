from typing import Optional

from tagoio_sdk.modules.Resources.AccountDeprecated import AccountDeprecated as Account


def getTokenByName(
    account: Account, deviceID: str, names: Optional[list[str] or str] = None
) -> str:
    """
    :param Account account: Account instance

    :param str deviceID: Id of device

    :param list[str] or str names: Array of names of the token, if null will return the first token
    found
    @deprecated Use the Resources.devices.tokenList method instead
    """
    if (isinstance(account, Account)) is False:
        raise ValueError(
            "The parameter 'account' must be an instance of a TagoIO Account."
        )

    tokens = account.devices.tokenList(
        deviceID,
        {
            "page": 1,
            "amount": 20,
            "fields": [
                "name",
                "token",
                "permission",
                "created_at",
                "last_authorization",
            ],
            "filter": {},
        },
    )

    if tokens is None or len(tokens) == 0:
        return None

    if names is None:
        return tokens[0]["token"]

    names = names if isinstance(names, list) else [names]

    if len(names) == 0:
        return tokens[0]["token"]

    for token in tokens:
        if token["name"] == names[0]:
            token = token

    if token is None or "token" not in token:
        raise ValueError(f"Can't find Token for {deviceID} in {names}")

    return token["token"]
