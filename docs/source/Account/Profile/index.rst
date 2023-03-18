**Profile**
============

Manage profiles in account be sure to use an account token with “write” permissions when using functions like create, edit and delete.

====
info
====

Gets information about the bucket

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" })
        result = myAccount.profile.info("Profile ID")

====
list
====

Lists all the profiles in your account

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" })
        result = myAccount.profile.list()


========
summary
========

Gets profile summary

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" })
        result = myAccount.profile.summary("Profile ID")


========
tokenList
========

Gets profile tokenList

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification
        | **queryObj**: Optional[:ref:`Query`]
        | Token Query

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" })
        result = myAccount.profile.tokenList("Profile ID")
