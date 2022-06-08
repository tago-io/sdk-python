**Profile**
============

Manage profiles in account Be sure to use an account token with “write” permissions when using functions like create, edit and delete.

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

        myAccount = Account({ "token": "my_account_token" }).Profile
        result = myAccount.info("Profile ID")

====
list
====

Lists all the profiles in your account

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" }).Profile
        result = myAccount.list()


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

        myAccount = Account({ "token": "my_account_token" }).Profile
        result = myAccount.summary("Profile ID")
