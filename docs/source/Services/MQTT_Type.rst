**MQTT Type**
===============

.. deprecated::
    Legacy MQTT is deprecated and will be removed in a future major version.
    Migrate to the new MQTT connector or use the HTTP API.
    See: https://docs.tago.io/docs/tagoio/integrations/networks/mqtt/

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
