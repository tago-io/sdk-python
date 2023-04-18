**Account**
==========

Manage Account. Be sure to use an account token with “write” permissions when using functions like create, edit and delete.

=========
info
=========

Gets all account information.

    **Return:**

        | **AccountInfo**: :ref:`AccountInfo`

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        account = Account({ "token": "my_account_token" })
        result = account.info()
