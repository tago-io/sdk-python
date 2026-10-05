**Dictionaries**
================

Manage dictionaries in your application.

========
list
========

Lists all dictionaries from your application with pagination support.

See: `Dictionaries <https://help.tago.io/portal/en/kb/articles/487-dictionaries>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`DictionaryQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name", "slug", "languages"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"]
            }

    **Returns:**

        | list[:ref:`DictionaryInfo`]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.list({
            "page": 1,
            "fields": ["id", "name", "slug"],
            "amount": 10,
            "orderBy": ["name", "asc"]
        })
        print(result)  # [{'id': 'dictionary-id-123', 'name': 'My Dictionary', 'slug': 'DICT'}, ...]


========
create
========

Creates a new dictionary in your application.

See: `Using Dictionaries (Multi-Language) <https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language>`_

    **Parameters:**

        | **dictionaryObj**: :ref:`DictionaryCreateInfo`
        | Dictionary information

    **Returns:**

        | dict

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.create({
            "name": "My Dictionary",
            "slug": "DICT",
        })
        print(result["dictionary"])  # dictionary-id-123


========
edit
========

Modifies an existing dictionary's properties.

See: `Using Dictionaries (Multi-Language) <https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

        | **dictionaryObj**: dict
        | Dictionary information to update

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.edit("dictionary-id-123", {
            "name": "Updated Dictionary",
        })
        print(result)  # Successfully Updated


========
delete
========

Deletes a dictionary from your application.

See: `Using Dictionaries (Multi-Language) <https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.delete("dictionary-id-123")
        print(result)  # Successfully Removed


========
info
========

Retrieves detailed information about a specific dictionary.

See: `Dictionaries <https://help.tago.io/portal/en/kb/articles/487-dictionaries>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

    **Returns:**

        | :ref:`DictionaryInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.info("dictionary-id-123")
        print(result)  # {'id': 'dictionary-id-123', 'name': 'My Dictionary', 'slug': 'DICT', 'languages': ['en-US'], ...}


============
languageEdit
============

Edits a language's content in a dictionary.

See: `Using Dictionaries (Multi-Language) <https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

        | **locale**: str
        | Language code

        | **languageObj**: :ref:`LanguageEditData`
        | Language data to update

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.languageEdit("dictionary-id-123", "en-US", {
            "dictionary": {"HELLO": "Hello"},
            "active": True
        })
        print(result)  # Dictionary language Successfully Updated


==============
languageDelete
==============

Removes a language from a dictionary.

See: `Using Dictionaries (Multi-Language) <https://help.tago.io/portal/en/kb/articles/489-using-dictionaries-multi-language>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

        | **locale**: str
        | Language code

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.languageDelete("dictionary-id-123", "en-US")
        print(result)


============
languageInfo
============

Retrieves language-specific content from a dictionary by ID.

See: `Dictionaries <https://help.tago.io/portal/en/kb/articles/487-dictionaries>`_

    **Parameters:**

        | **dictionaryID**: str
        | Dictionary ID

        | **locale**: str
        | Language code

        | *Optional* **queryObj**: :ref:`LanguageInfoQuery`
        | Query options

    **Returns:**

        | :ref:`LanguageData`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.languageInfo("dictionary-id-123", "en-US", {
            "fallback": True
        })
        print(result)  # {'ACCEPT': 'Accept', 'ACCEPTED': 'Accepted', ...}


==================
languageInfoBySlug
==================

Retrieves language-specific content from a dictionary by its slug.

See: `Dictionaries <https://help.tago.io/portal/en/kb/articles/487-dictionaries>`_

    **Parameters:**

        | **slug**: str
        | Dictionary slug

        | **locale**: str
        | Language code

        | *Optional* **queryObj**: :ref:`LanguageInfoQuery`
        | Query options

    **Returns:**

        | :ref:`LanguageData`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dictionaries.languageInfoBySlug("SLUG", "en-US", {
            "fallback": True
        })
        print(result)

.. toctree::


.. toctree::

    Dictionaries_Type
