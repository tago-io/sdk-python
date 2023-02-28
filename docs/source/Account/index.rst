
**Account**
==========

To set up an account object, you need a token that you need to get from our admin website and the region. Make sure to use tokens with the correct write/read privileges for the current function that you want to use.

========
Instance
========

    **Parameters:**

        | **token**: str
        | Account Token

        | *Optional* **region**: Regions: "usa-1" or "env"
        | Region is a optional parameter

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Account

        myAccount = Account({"token": "my_account_token", "region": "usa-1"})

.. toctree::

    Billing/index
    Buckets/index
    Dashboards/index
    Devices/index
    Profile/index
    Run/index
