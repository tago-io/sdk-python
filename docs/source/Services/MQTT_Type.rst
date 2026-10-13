**MQTT Type**
===============

.. deprecated::
    Migrate to TagoTIP: https://docs.tago.io/docs/tagotip/transports/mqtt

.. _mqtt_options:

options
-------

    **Attributes:**

        **retain**: Optional[bool]

        **qos**: Optional[int or float]


.. _MQTTData:

MQTTData
--------

    **Attributes:**

        **topic**: str

        **message**: str

        **bucket**: GenericID: str

        **options**: Optional[:ref:`mqtt_options`]
