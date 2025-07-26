from typing import Dict
from typing import List
from typing import Optional

from tagoio_sdk.common import Cache
from tagoio_sdk.common.Common_Type import GenericID
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.modules.Resources.Dictionaries_Types import DictionaryCreateInfo
from tagoio_sdk.modules.Resources.Dictionaries_Types import DictionaryInfo
from tagoio_sdk.modules.Resources.Dictionaries_Types import DictionaryQuery
from tagoio_sdk.modules.Resources.Dictionaries_Types import LanguageData
from tagoio_sdk.modules.Resources.Dictionaries_Types import LanguageEditData
from tagoio_sdk.modules.Resources.Dictionaries_Types import LanguageInfoQuery
from tagoio_sdk.modules.Utils.dateParser import dateParser
from tagoio_sdk.modules.Utils.dateParser import dateParserList


class Dictionaries(TagoIOModule):
    def list(self, queryObj: Optional[DictionaryQuery] = None) -> List[DictionaryInfo]:
        """
        @description:
            Lists all dictionaries from your application with pagination support.

        @see:
            https://help.tago.io/portal/en/kb/articles/487-dictionaries Dictionaries

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.list({
                "page": 1,
                "fields": ["id", "name", "slug"],
                "amount": 10,
                "orderBy": ["name", "asc"]
            })
            print(result)  # [{'id': 'dictionary-id-123', 'name': 'My Dictionary', 'slug': 'DICT'}, ...]
            ```
        """
        queryObj = queryObj or {}

        orderBy = "name,asc"
        if "orderBy" in queryObj:
            orderBy = f"{queryObj['orderBy'][0]},{queryObj['orderBy'][1]}"

        result = self.doRequest(
            {
                "path": "/dictionary",
                "method": "GET",
                "params": {
                    "page": queryObj.get("page", 1),
                    "fields": queryObj.get("fields", ["id", "name", "slug", "languages"]),
                    "filter": queryObj.get("filter", {}),
                    "amount": queryObj.get("amount", 20),
                    "orderBy": orderBy,
                },
            }
        )

        result = dateParserList(result, ["created_at", "updated_at"])

        return result

    def create(self, dictionaryObj: DictionaryCreateInfo) -> Dict[str, str]:
        """
        @description:
            Creates a new dictionary in your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language Using Dictionaries (Multi-Language)

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Create** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.create({
                "name": "My Dictionary",
                "slug": "DICT",
            })
            print(result["dictionary"])  # dictionary-id-123
            ```
        """
        result = self.doRequest(
            {
                "path": "/dictionary",
                "method": "POST",
                "body": dictionaryObj,
            }
        )

        return result

    def edit(self, dictionaryID: GenericID, dictionaryObj: dict) -> str:
        """
        @description:
            Modifies an existing dictionary's properties.

        @see:
            https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language Using Dictionaries (Multi-Language)

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.edit("dictionary-id-123", {
                "name": "Updated Dictionary",
            })
            print(result)  # Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}",
                "method": "PUT",
                "body": dictionaryObj,
            }
        )

        return result

    def delete(self, dictionaryID: GenericID) -> str:
        """
        @description:
            Deletes a dictionary from your application.

        @see:
            https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language Using Dictionaries (Multi-Language)

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Delete** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.delete("dictionary-id-123")
            print(result)  # Successfully Removed
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}",
                "method": "DELETE",
            }
        )

        Cache.clear_cache()

        return result

    def info(self, dictionaryID: GenericID) -> DictionaryInfo:
        """
        @description:
            Retrieves detailed information about a specific dictionary.

        @see:
            https://help.tago.io/portal/en/kb/articles/487-dictionaries Dictionaries

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.info("dictionary-id-123")
            print(result)  # {'id': 'dictionary-id-123', 'name': 'My Dictionary', 'slug': 'DICT', 'languages': ['en-US'], ...}
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}",
                "method": "GET",
            }
        )

        result = dateParser(result, ["created_at", "updated_at"])

        return result

    def languageEdit(self, dictionaryID: GenericID, locale: str, languageObj: LanguageEditData) -> str:
        """
        @description:
            Edits a language's content in a dictionary.

        @see:
            https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language Using Dictionaries (Multi-Language)

        @example:
            ```python
            resources = Resources()
            result = resources.dictionaries.languageEdit("dictionary-id-123", "en-US", {
                "dictionary": {"HELLO": "Hello"},
                "active": True
            })
            print(result)  # Dictionary language Successfully Updated
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}/{locale}",
                "method": "PUT",
                "body": languageObj,
            }
        )

        Cache.clear_cache()

        return result

    def languageDelete(self, dictionaryID: GenericID, locale: str) -> str:
        """
        @description:
            Removes a language from a dictionary.

        @see:
            https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language Using Dictionaries (Multi-Language)

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Edit** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.languageDelete("dictionary-id-123", "en-US")
            print(result)
            ```
        """
        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}/{locale}",
                "method": "DELETE",
            }
        )

        Cache.clear_cache()

        return result

    def languageInfo(
        self, dictionaryID: GenericID, locale: str, queryObj: Optional[LanguageInfoQuery] = None
    ) -> LanguageData:
        """
        @description:
            Retrieves language-specific content from a dictionary by ID.

        @see:
            https://help.tago.io/portal/en/kb/articles/487-dictionaries Dictionaries

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.languageInfo("dictionary-id-123", "en-US", {
                "fallback": True
            })
            print(result)  # {'ACCEPT': 'Accept', 'ACCEPTED': 'Accepted', ...}
            ```
        """
        queryObj = queryObj or {}

        result = self.doRequest(
            {
                "path": f"/dictionary/{dictionaryID}/{locale}",
                "method": "GET",
                "params": {
                    # Default to not getting the fallback language info if language is not found
                    # as this route is mainly used to edit a dictionary
                    "fallback": queryObj.get("fallback", False),
                },
            }
        )

        return result

    def languageInfoBySlug(self, slug: str, locale: str, queryObj: Optional[LanguageInfoQuery] = None) -> LanguageData:
        """
        @description:
            Retrieves language-specific content from a dictionary by its slug.

        @see:
            https://help.tago.io/portal/en/kb/articles/487-dictionaries Dictionaries

        @example:
            If receive an error "Authorization Denied", check policy **Dictionary** / **Access** in Access Management.
            ```python
            resources = Resources()
            result = resources.dictionaries.languageInfoBySlug("SLUG", "en-US", {
                "fallback": True
            })
            print(result)
            ```
        """
        queryObj = queryObj or {}

        result = self.doRequest(
            {
                "path": f"/dictionary/{slug}/{locale}",
                "method": "GET",
                "params": {
                    # Default to getting the fallback language info if language is not found
                    # as this route is mainly used to use the dictionary strings in applications
                    "fallback": queryObj.get("fallback", True),
                },
            }
        )

        return result
