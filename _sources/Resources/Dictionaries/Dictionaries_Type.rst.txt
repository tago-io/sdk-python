**Dictionaries Type**
=====================


.. _DictionaryCreateInfo:

DictionaryCreateInfo
--------------------

    **Attributes:**

        | name: str
        | Name of the dictionary.

        | slug: str
        | Unique identifier slug for the dictionary.

        | fallback: str
        | First dictionary language E.g "en-US"


.. _DictionaryLanguage:

DictionaryLanguage
------------------

    **Attributes:**

        | code: str
        | Language code E.g "en-US"

        | active: bool
        | Indicates if the language is active.


.. _DictionaryInfo:

DictionaryInfo(:ref:`DictionaryCreateInfo`)
--------------------------------------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the dictionary.

        | languages: List[:ref:`DictionaryLanguage`]
        | List of languages supported by the dictionary.

        | created_at: datetime
        | Date and time when the dictionary was created.

        | updated_at: datetime
        | Date and time when the dictionary was last updated.


.. _LanguageData:

LanguageData
------------

    **Attributes:**

        | Dict[str, str]
        | Dictionary of key-value pairs for translations.


.. _LanguageEditData:

LanguageEditData
----------------

    **Attributes:**

        | dictionary: :ref:`LanguageData`
        | The dictionary containing the translations.

        | active: bool
        | Indicates if the language is active.


.. _LanguageInfoQuery:

LanguageInfoQuery
-----------------

    **Attributes:**

        | fallback: Optional[bool]
        | Whether to return fallback language data if requested language is not found.


.. _DictionaryQuery:

DictionaryQuery(:ref:`Query`)
-----------------------------

    **Attributes:**

        | fields: Optional[Literal["name", "slug", "languages", "fallback", "created_at", "updated_at"]]
        | List of fields to include in the query results.

        | filter: Optional[:ref:`DictionaryInfo`]
        | Filter criteria for the query.
