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

        **color**: str

        **triggers**: :ref:`NotificationTriggerAnalysis` or :ref:`NotificationTriggerHTTP`or list[:ref:`NotificationTriggerProfile`],



.. _NotificationIconImage:

NotificationIconImage
---------------------

    **Attributes:**

        **image_url**: str

        **bg_color**: HexColor: str

        **fit**: "fill" or "contain" or "cover"


.. _NotificationIconSVG:

NotificationIconSVG
--------------------

    **Attributes:**

        **svg_url**: str

        **svg_color**: HexColor: str

        **bg_color**: HexColor: str


.. _NotificationCreate:

NotificationCreate
--------------------

    **Attributes:**

        **title**: str

        **message**: str

        **read**: bool

        **icon**: :ref:`NotificationIconSVG` or :ref:`NotificationIconImage`

        **buttons**: list[:ref:`NotificationButton`]

        **buttons_enabled**: bool

        **buttons_autodisable**: bool
