**Dashboards Type**
====================


.. _Arrangement:

Arrangement
------------

    **Attributes:**

        | **widget_id**: str
        | **x**: int or float
        | **y**: int or float
        | **width**: int or float
        | **height**: int or float
        | **tab**: Optional[str]


.. _DashboardCreateInfo:

DashboardCreateInfo
--------------------

    **Attributes:**

        **label**: str

        **arrangement**: list[Arrangement]

        **tags**: list[:ref:`TagsObj`]

        **visible**: bool

.. _icon:

icon
-----

    **Attributes:**

        | **url**: str
        | **color**: Optional[str]

.. _conditions:

conditions
-----------

    **Attributes:**

        | **key**: str
        | **value**: str

.. _filter_conditions:

filter_conditions
------------------
    **Attributes:**

        | **blueprint_device**: str
        | **tag_key**: str
        | **type**: str


.. _shared:

shared
--------

    **Attributes:**

        | **id**: str
        | **email**: str
        | **name**: str
        | **free_account**: bool
        | **allow_tags**: bool
        | **expire_time**: str
        | **allow_share**: bool

.. _blueprint_devices_conditions:

blueprint_devices
-------------------

    **Attributes:**

        | **conditions**: list[conditions]
        | **name**: str
        | **id**: str
        | **label**: str
        | **filter_conditions**: list[filter_conditions]
        | **theme**: any
        | **setup**: any

.. _DashboardInfo:

DashboardInfo
---------------

    **Attributes:**

        | **id**: :ref:`GenericID`
        | **created_at**: datetime
        | **updated_at**: datetime
        | **last_access**: datetime
        | **group_by**: list
        | **tabs**: list
        | **icon**: icon
        | **background**: any
        | **type**: str
        | **blueprint_device_behavior**: "more_than_one" or "always"
        | **blueprint_selector_behavior**: "open" or "closed" or "always_open" or "always_closed"
        | **blueprint_devices**: blueprint_devices
        | **theme**: any
        | **setup**: any
        | **shared**: shared

.. _WidgetData:

WidgetData
------------

    **Attributes:**

        | **origin**: GenericID
        | **qty**: Optional[Union[int, float]]
        | **timezone**: Optional[str]
        | **variables**: Optional[str]
        | **bucket**: Optional[GenericID]
        | **query**: Optional["min" or "max" or "count" or "avg" or "sum"]
        | **start_date**: Optional[Union[datetime, str]]
        | **end_date**: Optional[Union[datetime, str]]
        | **overwrite**: Optional[bool]

.. _WidgetResource:

WidgetResource
-----------------

    **Attributes:**

        filter: list[:ref:`TagsObj`]

.. _DeviceResourceView:

DeviceResourceView
-------------------

        | **view**: f"tags.{str}" or f"param.{str}" or "name" or "id" or "bucket_name" or "network_name" or "connector_name" or "connector" or "network" or "bucket" or "last_input" or "created_at" or "active"


.. _WidgetDeviceResource:

WidgetDeviceResource
-----------------------

    **Attributes:**

        | **type**: "device"
        | **view**: DeviceResourceView
        | **editable**: "name" or f"tags.{str}" or f"param.{str}"

.. _EditDeviceResource:

EditDeviceResource
--------------------

    **Attributes:**

        | **device**: GenericID
        | **name**: Optional[str]
        | **active**: Optional[bool]
        | **edit**: dict[str, Union[str, bool]]

.. _EditResourceOptions:

EditResourceOptions
---------------------

    **Attributes:**

        | **identifier**: Optional[str]

.. _WidgetInfo:

WidgetInfo
-------------

    **Attributes:**

        | **analysis_run**: Optional[GenericID]
        | **dashboard**: Optional[GenericID]
        | **display**: any
        | **data**: Optional[list[WidgetData]]
        | **resource**: Optional[list[WidgetDeviceResource]]
        | **id**: Optional[GenericID]
        | **label**: str
        | **realtime**: Optional[bool]
        | **type**: str

.. _DevicesRelated:

DevicesRelated
---------------

    **Attributes:**

        | **bucket**: GenericID

.. _AnalysisRelated:

AnalysisRelated
---------------

    **Attributes:**

        | **id**: GenericID
        | **name**: str

.. _PostDataModel:

PostDataModel
--------------

    **Attributes:**

        | **origin**: GenericID
        | **variable**: str

.. _blueprint_devices_origin:

blueprint_devices
-------------------

    **Attributes:**

        | **origin**: GenericID
        | **id**: GenericID
        | **bucket**: Optional[GenericID]

.. _widgetOverwrite:

widgetOverwrite
----------------

    **Attributes:**

        | **start_date**: Optional[any]
        | **end_date**: Optional[any]
        | **timezone**: Optional[any]

.. _GetDataModel:

GetDataModel
-------------

    **Attributes:**

        | **overwrite**: Optional[widgetOverwrite]
        | **blueprint_devices**: Optional[list[blueprint_devices]]
        | **page**: Optional[Union[int, float]]
        | **amount**: Optional[Union[int, float]]

.. _PublicKeyResponse:

PublicKeyResponse
-------------------

    **Attributes:**

        | **token**: GenericToken
        | **expire_time**: ExpireTimeOption

.. _EditDataModel:

EditDataModel
--------------

    | **EditDataModel** = :ref:`PostDataModel` and {id: :ref:`GenericID`}


.. _PublicKeyResponseType:

PublicKeyResponse
------------------

    | **PublicKeyResponse** = PublicKeyResponse


.. _widgetOverwriteOptions:

widgetOverwriteOptions
-----------------------
    | **widgetOverwriteOptions** = "start_date" or "end_date" or "timezone"
