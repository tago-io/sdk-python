**Device Type**
===============

.. _DeviceLocationGeoJSON:

LocationGeoJSON
---------------

    **Attributes:**

        **type**: "Point"

        **coordinates**: list[str]

.. _DeviceData:

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

        | **location**: :ref:`DeviceLocationGeoJSON`
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

        **query**: Enum[:ref:`DataQueryFirstLast`]

        **qty**: int

        **details**: bool

        **ordination**: "descending" or "ascending"

        **skip**: int

.. _DataQueryFirstLast:

DataQueryFirstLast
------------------
    **Attributes:**

        **query**: "last_item", "last_value", "last_location", "last_insert", "first_item", "first_value", "first_location", "first_insert"


.. _DataQuery:

DataQuery
---------

DataQuery = :ref:`DataQueryDefault` or :ref:`DataQueryFirstLast`


