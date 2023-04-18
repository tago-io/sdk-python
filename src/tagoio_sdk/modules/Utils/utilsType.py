from typing import TypedDict, Optional


HexadecimalPayload = str


class DownlinkOptions(TypedDict):
    payload: HexadecimalPayload
    port: str
    confirmed: Optional[bool]
