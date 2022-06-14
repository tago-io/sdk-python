from tagoio_sdk.modules.Account.Account import Account


def getTokenByName(account: Account, deviceID: str, names: list[str] or str) -> str:
    """
    :param Account account: Account instance

    :param str deviceID: Id of device

    :param list[str] or str names: Array of names of the token, if null will return the first token
    found
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

    if tokens is None or tokens[0] is None:
        return None

    if names is None:
        return tokens[0].token

    if isinstance(names, list) is True:
        namesArray = names
    if isinstance(names, list) is False:
        namesArray = [names]

    for x in tokens:
        if x["name"] == namesArray[0]:
            token = x

    if token is None:
        raise ValueError(f"Can't find Token for {deviceID} in {namesArray}")

    return token["token"]
