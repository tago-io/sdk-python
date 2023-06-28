**Account**
==========

Manage Account.

=========
info
=========

Gets all account information.

    **Return:**

        | **AccountInfo**: :ref:`AccountInfo`

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.account.info()
