from typing import Optional
from typing import TypedDict


HexadecimalPayload = str


class DownlinkOptions(TypedDict):
    payload: HexadecimalPayload
    port: str
    confirmed: Optional[bool]
