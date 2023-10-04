**Profile**
============

Manage profiles in account.

====
info
====

Gets information about the bucket

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.info("Profile ID")

====
list
====

Lists all the profiles in your account

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.list()


========
summary
========

Gets profile summary

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.summary("Profile ID")


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

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.tokenList("Profile ID")
