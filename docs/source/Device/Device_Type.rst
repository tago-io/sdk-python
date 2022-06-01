**Device Type**
===============

.. _LocationGeoJSON:

LocationGeoJSON
---------------

    **Attributes:**

        **type**: "Point"

        **coordinates**: list[str]

.. _Data:

Data
----

    **Attributes:**

        | **id**: str
        | Data ID.

        | **device**: str
        | ID of the device holding the data.

        | **variable**: str
        | Name of the variable for the data.

        | **value**: str or float or int or bool
        | Data value.

        | **group**: str
        | Series for the data. Used for grouping different data values.

        | **unit**: str
        | Unit for the data value.

        | **location**: :ref:`LocationGeoJSON`
        | Location for the data value.

        | **metadata**: any
        | Metadata for the data value.

        | **time**: date
        | Timestamp for the data value.

        | **created_at**: date
        | Timestamp for the data value. Determined by the API.


.. _DataQueryDefault:

DataQueryDefault
----------------
    **Attributes:**

        **query**: "default"

        **qty**: int

        **details**: bool

        **ordination**: "descending" or "ascending"

        **skip**: int

.. _DataQueryFirstLast:

DataQueryFirstLast
------------------
    **Attributes:**

        **query**: "last_item" or "last_value" or "last_location" or "last_insert" or "first_item" or "first_value" or "first_location" or "first_insert"


.. _DataQuery:

DataQuery
---------

DataQuery = :ref:`DataQueryDefault` or :ref:`DataQueryFirstLast`


