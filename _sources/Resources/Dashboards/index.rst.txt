**Dashboards**
==============

Manage dashboards in your application.

=============
listDashboard
=============

Lists all dashboards from your application with pagination support.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`Query`
        | Query parameters to filter and paginate the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["label", "asc"]
            }

    **Returns:**

        | list[:ref:`DashboardInfo`]
        | List of dashboard information objects.

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.listDashboard({
            "page": 1,
            "fields": ["id", "name"],
            "amount": 10,
            "orderBy": ["label", "asc"]
        })
        print(result)  # [{'id': 'dashboard-id-123', 'label': 'My Dashboard', ...}, ...]


======
create
======

Creates a new dashboard in your application.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardObj**: :ref:`DashboardCreateInfo`
        | Dashboard configuration object

    **Returns:**

        | dict
        | Object containing the created dashboard ID

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.create({
            "label": "My Dashboard",
            "tags": [{"key": "type", "value": "monitoring"}]
        })
        print(result)  # {'dashboard': 'dashboard-id-123'}


====
edit
====

Modifies an existing dashboard's properties.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **dashboardObj**: dict[str, Any]
        | Dictionary with properties to update

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.edit("dashboard-id-123", {
            "label": "Updated Dashboard",
            "active": False
        })
        print(result)  # Successfully Updated


======
delete
======

Deletes a dashboard from the application.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.delete("dashboard-id-123")
        print(result)  # Successfully Removed


====
info
====

Retrieves detailed information about a specific dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

    **Returns:**

        | :ref:`DashboardInfo`
        | Complete dashboard information

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        dashboard_info = resources.dashboards.info("dashboard-id-123")
        print(dashboard_info)  # {'id': 'dashboard-id-123', 'label': 'My Dashboard', ...}


=========
duplicate
=========

Creates a copy of an existing dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier to duplicate

        | *Optional* **dashboardObj**: dict
        | Duplication options

        .. code-block::
            :caption: **dashboardObj options:**

            dashboardObj = {
                "setup": Optional[Any],       # Custom setup configuration
                "new_label": Optional[str]    # Label for the duplicated dashboard
            }

    **Returns:**

        | dict
        | Object with dashboard_id and success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Duplicate" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.duplicate("dashboard-id-123", {
            "new_label": "Copy of My Dashboard"
        })
        print(result)  # {'dashboard_id': 'new-dashboard-id', 'message': 'Dashboard duplicated successfully'}


============
getPublicKey
============

Generates a new public access token for the dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | *Optional* **expireTime**: :ref:`ExpireTimeOption`
        | Time when token will expire (default: "never")

    **Returns:**

        | :ref:`PublicKeyResponse`
        | Object with public token and expiration time

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        public_key = resources.dashboards.getPublicKey("dashboard-id-123", "1day")
        print(public_key)  # {'token': 'token-id-123', 'expire_time': '2025-01-02T00:00:00.000Z'}


==================
listDevicesRelated
==================

Lists all devices associated with the dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

    **Returns:**

        | list[:ref:`DevicesRelated`]
        | List of devices related to the dashboard

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Related devices" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        devices = resources.dashboards.listDevicesRelated("dashboard-id-123")
        print(devices)  # [{'id': 'device-id-123', 'bucket': 'bucket-id'}, ...]


===================
listAnalysisRelated
===================

Lists all analyses associated with a dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

    **Returns:**

        | list[:ref:`AnalysisRelated`]
        | List of analyses related to the dashboard

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Related analysis" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        analyses = resources.dashboards.listAnalysisRelated("dashboard-id-123")
        print(analyses)  # [{'id': 'analysis-id-123', 'name': 'Analysis #1'}, ...]


=============================
runWidgetHeaderButtonAnalysis
=============================

Executes an analysis from a widget's header button.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_

    **Parameters:**

        | **analysisID**: :ref:`GenericID`
        | The ID of the analysis to run

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | The ID of the widget that contains the header button

        | *Optional* **scope**: dict[str, Any]
        | Data to send to the analysis (default: {})

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.runWidgetHeaderButtonAnalysis(
            "analysis-id-123",
            "dashboard-id-456",
            "widget-id-789",
            {"custom_data": "value"}
        )
        print(result)  # Analysis executed successfully


=======
Widgets
=======

The Widgets class provides methods to manage dashboard widgets. Access it through ``resources.dashboards.widgets``.

==============
widgets.create
==============

Creates a new widget for a specified dashboard with the given configuration.

**Note:** After created, the widget is not added into the dashboard arrangement. You must edit the dashboard to include it in the arrangement.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetObj**: :ref:`WidgetInfo`
        | Widget configuration object

    **Returns:**

        | dict[str, :ref:`GenericID`]
        | Object containing the created widget ID

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Create and Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.create("dashboard-id-123", {
            "data": [{
                "origin": "origin-id-123",
                "query": "last_value",
                "variables": ["temperature"]
            }],
            "display": {
                "show_units": True,
                "show_variables": True,
                "variables": [{
                    "origin": "origin-id-123",
                    "variable": "temperature"
                }]
            },
            "label": "Temperature",
            "type": "display",
        })
        print(result)  # {'widget': 'widget-id-456'}

        # To add the widget size to the dashboard
        # Before running this, make sure doesn't have more widgets in the dashboard.
        resources.dashboards.edit("dashboard-id-123", {
            "arrangement": [{
                "widget_id": result["widget"],
                "width": 1,
                "height": 2,
                "minW": 1,
                "minH": 2,
                "x": 0,
                "y": 0
            }]
        })


============
widgets.edit
============

Updates an existing widget's configuration on a dashboard.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | **data**: dict
        | Dictionary with widget properties to update

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.edit("dashboard-id-123", "widget-id-456", {
            "label": "Updated Temperature",
        })
        print(result)  # Successfully Updated


==============
widgets.delete
==============

Permanently removes a widget from a dashboard.

**Note:** After deleted, the widget is not removed from the dashboard arrangement. You must edit the dashboard to remove it from the arrangement.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Delete and Edit" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.delete("dashboard-id-123", "widget-id-456")
        print(result)  # Successfully Removed

        # To remove sizes from all widgets from a dashboard
        # Before running this, make sure doesn't have more widgets in the dashboard.
        resources.dashboards.edit("dashboard-id-123", {"arrangement": []})


============
widgets.info
============

Retrieves detailed information about a specific widget.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

    **Returns:**

        | :ref:`WidgetInfo`
        | Complete widget information

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Dashboard" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.info("dashboard-id-123", "widget-id-456")
        print(result)  # {'id': 'widget-id-456', 'data': [{'query': 'last_value', ...}, ...], ...}


===============
widgets.getData
===============

Retrieves data or resource list for a specific widget based on the given parameters.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | *Optional* **params**: :ref:`GetDataModel`
        | Query parameters for data retrieval

    **Returns:**

        | object
        | Widget data and configuration

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.getData("dashboard-id-123", "widget-id-456", {
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "timezone": "UTC"
        })
        print(result)  # {'widget': {'analysis_run': None, 'dashboard': '6791456f8b726c0009adccec', ...}, ...}


================
widgets.sendData
================

Sends new data values to be displayed in the widget.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | **data**: :ref:`PostDataModel` or list[:ref:`PostDataModel`]
        | Data to send to the widget

        | *Optional* **bypassBucket**: bool
        | Whether to bypass bucket validation (default: False)

    **Returns:**

        | object
        | Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.sendData("dashboard-id-123", "widget-id-456", {
            "origin": "origin-id-123",
            "variable": "temperature",
            "value": 25.5,
            "unit": "C"
        })
        print(result)  # ['1 Data Added']


================
widgets.editData
================

Updates existing data values for a specific widget.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | **data**: :ref:`EditDataModel` or list[:ref:`EditDataModel`]
        | Data to update

        | *Optional* **bypassBucket**: bool
        | Whether to bypass bucket validation (default: False)

    **Returns:**

        | object
        | Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.editData("dashboard-id-123", "widget-id-456", {
            "origin": "origin-id-123",
            "id": "data-id-789",
            "value": 25.5
        })
        print(result)  # Device Data Updated


==================
widgets.deleteData
==================

Removes multiple data items from the widget by pairs of data ID and resource ID.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | **idPairs**: list[str]
        | List of data ID and resource ID pairs in format "data_id:resource_id"

    **Returns:**

        | str
        | Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.deleteData(
            "dashboard-id",
            "widget-id",
            [
                "data_1-id:device_A-id",
                "data_2-id:device_A-id",
                "data_3-id:device_B-id",
            ]
        )
        print(result)  # Successfully Removed


====================
widgets.editResource
====================

Updates resource values associated with the widget.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

        | **resourceData**: :ref:`EditDeviceResource` or list[:ref:`EditDeviceResource`]
        | Resource data to update

        | *Optional* **options**: :ref:`EditResourceOptions`
        | Edit options

    **Returns:**

        | object
        | Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.editResource(
            "dashboard-id-123",
            "widget-id-456",
            {
                "device": "device-id-789",
                "name": "Updated Device Name",
                "active": True
            },
            {"identifier": "my-identifier"}
        )
        print(result)  # Resource Updated


=====================
widgets.tokenGenerate
=====================

Generates a new authentication token for embedding a widget. Each call regenerates the token.

See: `Dashboard Overview <https://docs.tago.io/docs/tagoio/dashboards/>`_ | `Widgets <https://docs.tago.io/docs/tagoio/widgets/>`_

    **Parameters:**

        | **dashboardID**: :ref:`GenericID`
        | Dashboard identifier

        | **widgetID**: :ref:`GenericID`
        | Widget identifier

    **Returns:**

        | dict[str, :ref:`GenericToken`]
        | Object containing the widget token

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.dashboards.widgets.tokenGenerate("dashboard-id-123", "widget-id-456")
        print(result)  # {'widget_token': 'widget-token-123'}


.. toctree::

    Dashboard_Type
