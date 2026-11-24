**Notifications Type**
======================


.. _NotificationTriggerAnalysis:

NotificationTriggerAnalysis
---------------------------

    **Attributes:**

        | analysis_id: :ref:`GenericID`
        | ID of the analysis to trigger.


.. _NotificationTriggerHTTP:

NotificationTriggerHTTP
-----------------------

    **Attributes:**

        | url: str
        | The URL to make the request to.

        | method: "POST" or "GET" or "PUT" or "DELETE" or "REDIRECT"
        | HTTP method to use for the request.

        | body: dict[str, Any]
        | Body of the HTTP request.


.. _NotificationTriggerProfile:

NotificationTriggerProfile
--------------------------

    **Attributes:**

        | share_profile: "accept" or "refuse"
        | Action to take on a profile share.


.. _NotificationButton:

NotificationButton
------------------

    **Attributes:**

        | id: str
        | Unique identifier for the button.

        | label: str
        | Text displayed on the button.

        | color: Optional[str]
        | Color of the button.

        | triggers: :ref:`NotificationTriggerAnalysis` or :ref:`NotificationTriggerHTTP` or list[:ref:`NotificationTriggerProfile`]
        | Actions triggered when the button is clicked.


.. _NotificationIconImage:

NotificationIconImage
---------------------

    **Attributes:**

        | image_url: str
        | URL of the image to use as the notification icon.

        | bg_color: Optional[HexColor]
        | Background color for the icon.

        | fit: Optional["fill" or "contain" or "cover"]
        | How the image should fit in its container.


.. _NotificationIconSVG:

NotificationIconSVG
-------------------

    **Attributes:**

        | svg_url: str
        | URL of the SVG to use as the notification icon.

        | svg_color: Optional[HexColor]
        | Color of the SVG.

        | bg_color: Optional[HexColor]
        | Background color for the icon.


.. _NotificationCreate:

NotificationCreate
------------------

    **Attributes:**

        | title: str
        | Title of the notification.

        | message: str
        | Content of the notification.

        | read: Optional[bool]
        | Whether the notification has been read.

        | icon: Optional[:ref:`NotificationIconSVG` or :ref:`NotificationIconImage`]
        | Icon for the notification.

        | buttons: Optional[list[:ref:`NotificationButton`]]
        | Buttons to display with the notification.

        | buttons_enabled: Optional[bool]
        | Whether buttons are enabled.

        | buttons_autodisable: Optional[bool]
        | Whether buttons should automatically disable after being clicked.


.. _NotificationQuery:

NotificationQuery(:ref:`Query`)
-------------------------------

    **Attributes:**

        | fields: Optional[List["created_at"]]
        | Fields to include in the query response.

        | filter: Optional[Dict["read", bool]]
        | Filters for the query.


.. _NotificationInfo:

NotificationInfo(:ref:`NotificationCreate`)
--------------------------------------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the notification.

        | created_at: datetime
        | When the notification was created.


.. _NotificationInfoBasic:

NotificationInfoBasic
---------------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the notification.

        | created_at: datetime
        | When the notification was created.


.. _NotificationCreateReturn:

NotificationCreateReturn
------------------------

    **Attributes:**

        | id: :ref:`GenericID`
        | Unique identifier for the newly created notification.
