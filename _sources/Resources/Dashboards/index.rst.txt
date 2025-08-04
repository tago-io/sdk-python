**Dashboards**
==============

Manage dashboards in account.

=============
listDashboard
=============

Retrieves a list with all dashboards from the account.

    **Parameters:**

        | **queryObj**: :ref:`Query`
        | Default query parameters for retrieving the list of dashboards.

    **Returns:**

        | **result**: list[:ref:`DashboardInfo`]
        | List of dashboard information.

=======
create
=======

Gets information about the dashboard

    **Parameters:**

        | **dashboardObj**: :ref:`DashboardCreateInfo`
        | Dashboard object

======
edit
======

Modify any property of the dashboards

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification

        | dashboardObj: :ref:`DashboardCreateInfo`
        | Dashboard Object with data to be replaced


======
delete
======

Deletes an dashboard from the account

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification


======
info
======

Gets information about the dashboard

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification


=========
duplicate
=========

Duplicate the dashboard to your own account

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification

        | dashboardObj: { "setup": Optional[any], "new_label": Optional[str] }
        | Dashboard Object with data of the duplicate dashboard


============
getPublicKey
============

Generate a new public token for the dashboard

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification

        | expireTime: :ref:`ExpireTimeOption` = "never"
        | Time when token will expire


===================
listDevicesRelated
===================

Get list of devices related with dashboard

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification


===================
listAnalysisRelated
===================

Get list of analysis related with a dashboard

    **Parameters:**

        | **dashboardID**: GenericID: str
        | Dashboard identification


=============================
runWidgetHeaderButtonAnalysis
=============================

Runs an analysis located in a widget's header button

    **Parameters:**

        | **analysisID**: GenericID: str
        | The id of the analysis to run

        | **dashboardID**: GenericID: str
        | Dashboard identification

        | **widgetID**: GenericID: str
        | The id of the widget that contains the header button

        | **scope**: Optional[any]
        | Data to send to the analysis

.. toctree::

    Dashboard_Type
