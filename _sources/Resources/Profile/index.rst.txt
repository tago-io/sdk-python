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

    **Returns:**

        | **result**: :ref:`ProfileInfo`

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.info("Profile ID")

====
list
====

Lists all the profiles in your account

    **Returns:**

        | **result**: list[:ref:`ProfileListInfo`]

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

    **Returns:**

        | **result**: :ref:`ProfileSummary`

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.summary("Profile ID")


=========
tokenList
=========

Gets profile tokenList

    **Parameters:**

        | **profileID**: GenericID: str
        | Profile identification
        | **queryObj**: Optional[:ref:`Query`]
        | Token Query

    **Returns:**

        | **result**: list[:ref:`TokenDataList`]

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.tokenList("Profile ID")

.. toctree::

    Profile_Types
