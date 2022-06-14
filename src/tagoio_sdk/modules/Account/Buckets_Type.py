from datetime import datetime
from typing import Literal, TypedDict, Union

from tagoio_sdk.common.Common_Type import TagsObj

DataStorageType = Literal["immutable", "mutable", "legacy"]


class ExportBucketOption(TypedDict):
    start_date: datetime
    end_date: datetime


class BucketCreateInfo(TypedDict):
    name: str
    """
    A name for the bucket.
    """
    description: Union[str, None]
    """
    Set if the bucket will be visible or not. Default True.
    """
    visible: bool
    """
    Set if the bucket will be visible or not. Default True.
    """
    tags: list[TagsObj]
    """
    An array of tags.
    """
