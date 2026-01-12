**Notification Type**
=====================

.. _ServiceNotificationTriggerAnalysis:

NotificationTriggerAnalysis
---------------------------

    **Attributes:**

        **analysis_id**: GenericID: str


.. _ServiceNotificationTriggerHTTP:

NotificationTriggerHTTP
------------------------

    **Attributes:**

        **url**: str

        **method**: "POST" or "GET" or "PUT" or "DELETE" or "REDIRECT"

        **body**: dict[str, Any]


.. _ServiceNotificationTriggerProfile:

NotificationTriggerProfile
--------------------------

    **Attributes:**

        **share_profile**: "accept" or "refuse"


.. _ServiceNotificationButton:

NotificationButton
------------------

    **Attributes:**

        **id**: str

        **label**: str

        **color**: Optional[str]

        **triggers**: :ref:`ServiceNotificationTriggerAnalysis` or :ref:`ServiceNotificationTriggerHTTP` or List[:ref:`ServiceNotificationTriggerProfile`]



.. _ServiceNotificationIconImage:

NotificationIconImage
---------------------

    **Attributes:**

        **image_url**: str

        **bg_color**: Optional[HexColor: str]

        **fit**: Optional["fill" or "contain" or "cover"]


.. _ServiceNotificationIconSVG:

NotificationIconSVG
--------------------

    **Attributes:**

        **svg_url**: str

        **svg_color**: Optional[HexColor: str]

        **bg_color**: Optional[HexColor: str]


.. _ServiceNotificationCreate:

NotificationCreate
--------------------

    **Attributes:**

        **title**: str

        **message**: str

        **read**: Optional[bool]

        **icon**: Optional[:ref:`NotificationIconSVG` or :ref:`NotificationIconImage`]

        **buttons**: Optional[list[:ref:`NotificationButton`]]

        **buttons_enabled**: Optional[bool]

        **buttons_autodisable**: Optional[bool]
