**Dashboard Type**
==================


.. _Arrangement:

Arrangement
-----------

    Widget arrangement configuration on the dashboard layout.

    **Attributes:**

        | **widget_id**: str
        | Unique identifier for the widget

        | **x**: int or float
        | Horizontal position coordinate

        | **y**: int or float
        | Vertical position coordinate

        | **width**: int or float
        | Widget width

        | **height**: int or float
        | Widget height

        | **tab**: Optional[str]
        | Tab identifier where the widget is located


.. _DashboardCreateInfo:

DashboardCreateInfo
-------------------

    Information required to create a new dashboard.

    **Attributes:**

        | **label**: str
        | Dashboard label/name

        | **arrangement**: list[:ref:`Arrangement`]
        | Layout configuration for widgets

        | **tags**: list[:ref:`TagsObj`]
        | Tags for dashboard categorization

        | **visible**: bool
        | Dashboard visibility status


.. _icon:

icon
----

    Dashboard icon configuration.

    **Attributes:**

        | **url**: str
        | Icon URL

        | **color**: Optional[str]
        | Icon color Hexadecimal


.. _conditions:

conditions
----------

    Condition key-value pair for blueprint device filtering.

    **Attributes:**

        | **key**: str
        | Condition key

        | **value**: str
        | Condition value


.. _filter_conditions:

filter_conditions
-----------------

    Filter conditions for blueprint device selection.

    **Attributes:**

        | **blueprint_device**: str
        | Blueprint device identifier

        | **tag_key**: str
        | Tag key for filtering

        | **type**: str
        | Filter type


.. _shared:

shared
------

    Dashboard sharing information.

    **Attributes:**

        | **id**: str
        | Share identifier

        | **email**: str
        | Shared user email

        | **name**: str
        | Shared user name

        | **free_account**: bool
        | Whether the user has a free account

        | **allow_tags**: bool
        | Whether tags are allowed

        | **expire_time**: str
        | Share expiration time

        | **allow_share**: bool
        | Whether re-sharing is allowed


.. _BlueprintDeviceConfig:

BlueprintDeviceConfig
---------------------

    Blueprint device configuration for dynamic dashboards.

    **Attributes:**

        | **conditions**: list[:ref:`conditions`]
        | Device selection conditions

        | **name**: str
        | Blueprint name

        | **id**: str
        | Blueprint identifier

        | **label**: str
        | Blueprint label

        | **filter_conditions**: list[:ref:`filter_conditions`]
        | Filter conditions

        | **theme**: any
        | Theme configuration

        | **setup**: any
        | Setup configuration


.. _DashboardInfo:

DashboardInfo
-------------

    Complete dashboard information.

    **Attributes:**

        | **id**: :ref:`GenericID`
        | Dashboard unique identifier

        | **created_at**: datetime
        | Dashboard creation timestamp

        | **updated_at**: datetime
        | Last update timestamp

        | **last_access**: datetime
        | Last access timestamp

        | **group_by**: list
        | Grouping configuration

        | **tabs**: list
        | Dashboard tabs

        | **icon**: :ref:`icon`
        | Dashboard icon

        | **background**: any
        | Background configuration

        | **type**: str
        | Dashboard type

        | **blueprint_device_behavior**: "more_than_one" or "always"
        | Blueprint device behavior mode

        | **blueprint_selector_behavior**: "open" or "closed" or "always_open" or "always_closed"
        | Blueprint selector behavior mode

        | **blueprint_devices**: :ref:`BlueprintDeviceConfig`
        | Blueprint device configuration

        | **theme**: any
        | Dashboard theme

        | **setup**: any
        | Dashboard setup

        | **shared**: :ref:`shared`
        | Sharing configuration


.. _WidgetData:

WidgetData
----------

    Widget data configuration.

    **Attributes:**

        | **origin**: :ref:`GenericID`
        | Data origin identifier

        | **qty**: Optional[int or float]
        | Quantity of data points

        | **timezone**: Optional[str]
        | Timezone for data queries

        | **variables**: Optional[str]
        | Variables to query

        | **bucket**: Optional[:ref:`GenericID`]
        | Bucket identifier

        | **query**: Optional["min" or "max" or "count" or "avg" or "sum"]
        | Query type

        | **start_date**: Optional[datetime or str]
        | Query start date

        | **end_date**: Optional[datetime or str]
        | Query end date

        | **overwrite**: Optional[bool]
        | Whether to overwrite existing data


.. _WidgetResource:

WidgetResource
--------------

    Widget resource filtering configuration.

    **Attributes:**

        | **filter**: list[:ref:`TagsObj`]
        | Filter tags


.. _DeviceResourceView:

DeviceResourceView
------------------

    Available views for device resources in widgets.

    **Type:**

        | Literal[f"tags.{str}", f"param.{str}", "name", "id", "bucket_name", "network_name", "connector_name", "connector", "network", "bucket", "last_input", "created_at", "active"]


.. _WidgetDeviceResource:

WidgetDeviceResource
--------------------

    Device resource configuration for widgets.

    **Attributes:**

        | **type**: "device"
        | Resource type

        | **view**: :ref:`DeviceResourceView`
        | View configuration

        | **editable**: "name" or f"tags.{str}" or f"param.{str}"
        | Editable fields


.. _EditDeviceResource:

EditDeviceResource
------------------

    Device resource edit configuration.

    **Attributes:**

        | **device**: :ref:`GenericID`
        | Device identifier

        | **name**: Optional[str]
        | Device name

        | **active**: Optional[bool]
        | Device active status

        | **edit**: dict[str, str or bool]
        | Fields to edit


.. _EditResourceOptions:

EditResourceOptions
-------------------

    Options for editing resources.

    **Attributes:**

        | **identifier**: Optional[str]
        | Resource identifier


.. _WidgetInfo:

WidgetInfo
----------

    Complete widget information.

    **Attributes:**

        | **analysis_run**: Optional[:ref:`GenericID`]
        | Analysis run identifier

        | **dashboard**: Optional[:ref:`GenericID`]
        | Dashboard identifier

        | **display**: any
        | Display configuration

        | **data**: Optional[list[:ref:`WidgetData`]]
        | Widget data configuration

        | **resource**: Optional[list[:ref:`WidgetDeviceResource`]]
        | Widget resource configuration

        | **id**: Optional[:ref:`GenericID`]
        | Widget identifier

        | **label**: str
        | Widget label

        | **realtime**: Optional[bool]
        | Real-time update status

        | **type**: str
        | Widget type


.. _DevicesRelated:

DevicesRelated
--------------

    Device information related to dashboard.

    Extends BucketDeviceInfo with additional bucket field.

    **Attributes:**

        | **id**: :ref:`GenericID`
        | Device identifier

        | **name**: str
        | Device name

        | **bucket**: :ref:`GenericID`
        | Bucket identifier


.. _AnalysisRelated:

AnalysisRelated
---------------

    Analysis information related to dashboard.

    **Attributes:**

        | **id**: :ref:`GenericID`
        | Analysis identifier

        | **name**: str
        | Analysis name


.. _PostDataModel:

PostDataModel
-------------

    Model for posting data to widgets.

    **Attributes:**

        | **origin**: :ref:`GenericID`
        | Data origin identifier

        | **variable**: str
        | Variable name


.. _BlueprintDeviceOrigin:

BlueprintDeviceOrigin
---------------------

    Blueprint device configuration with origin reference for widget data queries.

    **Attributes:**

        | **origin**: :ref:`GenericID`
        | Origin identifier

        | **id**: :ref:`GenericID`
        | Device identifier

        | **bucket**: Optional[:ref:`GenericID`]
        | Bucket identifier


.. _widgetOverwrite:

widgetOverwrite
---------------

    Widget data overwrite options.

    **Attributes:**

        | **start_date**: Optional[any]
        | Override start date

        | **end_date**: Optional[any]
        | Override end date

        | **timezone**: Optional[any]
        | Override timezone


.. _GetDataModel:

GetDataModel
------------

    Model for retrieving widget data.

    **Attributes:**

        | **overwrite**: Optional[:ref:`widgetOverwrite`]
        | Overwrite options

        | **blueprint_devices**: Optional[list[:ref:`BlueprintDeviceOrigin`]]
        | Blueprint devices list

        | **page**: Optional[int or float]
        | Page number for pagination

        | **amount**: Optional[int or float]
        | Amount of items per page


.. _PublicKeyResponse:

PublicKeyResponse
-----------------

    Response containing dashboard public access token.

    **Attributes:**

        | **token**: :ref:`GenericToken`
        | Public access token

        | **expire_time**: :ref:`ExpireTimeOption`
        | Token expiration time


.. _EditDataModel:

EditDataModel
-------------

    Model for editing widget data.

    **Extends:** :ref:`PostDataModel`

    **Additional Attributes:**

        | **id**: :ref:`GenericID`
        | Data record identifier


.. _widgetOverwriteOptions:

widgetOverwriteOptions
----------------------

    Available options for widget data override.

    **Type:**

        | Literal["start_date", "end_date", "timezone"]