**Buckets**
============

Manage buckets in account.

====
info
====

Gets information about the bucket

    **Parameters:**

        | **bucketID**: GenericID: str
        | Bucket ID

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.buckets.info("Bucket ID")

======
amount
======

Get Amount of data on the Bucket

    **Parameters:**

        | **bucketID**: GenericID: str
        | Bucket ID

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.buckets.amount("Bucket ID")
