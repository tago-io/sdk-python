**Buckets**
============

Manage buckets in account Be sure to use an account token with “write” permissions when using functions like create, edit and delete.

====
info
====

Gets information about the bucket

    **Parameters:**

        | **bucketID**: GenericID: str
        | Bucket ID

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" }).Buckets
        result = myAccount.info("Bucket ID")

======
amount
======

Get Amount of data on the Bucket

    **Parameters:**

        | **bucketID**: GenericID: str
        | Bucket ID

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({ "token": "my_account_token" }).Buckets
        result = myAccount.amount("Bucket ID")
