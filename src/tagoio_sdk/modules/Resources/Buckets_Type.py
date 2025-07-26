from datetime import datetime
from typing import Literal
from typing import Optional
from typing import TypedDict
from typing import Union

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import TagsObj


DataStorageType = Literal["immutable", "mutable", "legacy"]


class ExportBucketOption(TypedDict):
    start_date: Optional[datetime]
    end_date: Optional[datetime]


class BucketDeviceInfo(TypedDict):
    id: GenericID
    name: str


class BucketCreateInfo(TypedDict):
    name: str
    """
    A name for the bucket.
    """
    description: Optional[Union[str, None]]
    """
    Set if the bucket will be visible or not. Default True.
    """
    visible: Optional[bool]
    """
    Set if the bucket will be visible or not. Default True.
    """
    tags: Optional[list[TagsObj]]
    """
    An array of tags.
    """
