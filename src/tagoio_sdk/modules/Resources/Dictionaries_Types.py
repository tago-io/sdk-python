from datetime import datetime
from typing import Dict
from typing import List
from typing import Literal
from typing import Optional
from typing import TypedDict

from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.Common_Type import Query


class DictionaryCreateInfo(TypedDict):
    name: str
    slug: str
    fallback: str
    """First dictionary language E.g "en-US" """


class DictionaryLanguage(TypedDict):
    code: str
    """Language code E.g "en-US" """
    active: bool


class DictionaryInfo(DictionaryCreateInfo):
    id: GenericID
    languages: List[DictionaryLanguage]
    created_at: datetime
    updated_at: datetime


class LanguageData(TypedDict):
    Dict[str, str]


class LanguageEditData(TypedDict):
    dictionary: LanguageData
    active: bool


class LanguageInfoQuery(TypedDict, total=False):
    fallback: Optional[bool]


class DictionaryQuery(Query):
    fields: Optional[Literal["name", "slug", "languages", "fallback", "created_at", "updated_at"]]
    filter: Optional[DictionaryInfo]
