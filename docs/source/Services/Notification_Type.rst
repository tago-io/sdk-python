**Notification Type**
===============

.. _NotificationTriggerAnalysis:

NotificationTriggerAnalysis
---------------------------

    **Attributes:**

        **analysis_id**: GenericID: str


.. _NotificationTriggerHTTP:

NotificationTriggerHTTP
------------------------

    **Attributes:**

        **url**: str

        **method**: "POST" or "GET" or "PUT" or "DELETE" or "REDIRECT"

        **body**: dict[str, Any]


.. _NotificationTriggerProfile:

NotificationTriggerProfile
--------------------------

    **Attributes:**

        **share_profile**: "accept" or "refuse"


.. _NotificationButton:

NotificationButton
------------------

    **Attributes:**

        **id**: str

        **label**: str

        **color**: Optional[str]

        **triggers**: :ref:`NotificationTriggerAnalysis` or :ref:`NotificationTriggerHTTP`or list[:ref:`NotificationTriggerProfile`],



.. _NotificationIconImage:

NotificationIconImage
---------------------

    **Attributes:**

        **image_url**: str

        **bg_color**: Optional[HexColor: str]

        **fit**: Optional["fill" or "contain" or "cover"]


.. _NotificationIconSVG:

NotificationIconSVG
--------------------

    **Attributes:**

        **svg_url**: str

        **svg_color**: Optional[HexColor: str]

        **bg_color**: Optional[HexColor: str]


.. _NotificationCreate:

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
