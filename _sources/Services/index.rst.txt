**Services**
============

========
Instance
========

    **Parameters:**

        | *Optional* **token**: str
        | Token is a optional parameter (Analysis Token).

        | *Optional* **region**: str "usa-1" or "env"
        | Region is a optional parameter

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import Services

        services = Services()


==========
Attachment
==========

Send Attachment

    **Parameters:**

        | **archive**: :ref:`ArchiveFile`
        | Archive JSON Object

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.Attachment.upload(
                {
                    "name": "Test",
                    "content": "base64",
                    "type": "Test",
                }
            )

==============
ConsoleService
==============

Log message in analysis console

    **Parameters:**

        | **message**: str
        | Log message

        | *Optional* **time**: datetime
        | Date of message

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.console.log(
                {
                    "message": "Test",
                }
            )

=====
Email
=====

Send Email

    **Parameters:**

        | **email**: Any or :ref:`EmailWithRawText` or :ref:`EmailWithHTML` or :ref:`EmailWithTemplate`
        | Email objects

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.email.send(
                {
                    "to": "myclien@tago.io",
                    "subject": "Test Subject",
                }
            )

====
MQTT
====

Publish to a MQTT Device

    **Parameters:**

        | **mqtt**: :ref:`MQTTData`
        | MQTT object, contains topic, bucket, message and options(retain and qos)


.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.MQTT.publish(
                {
                    "bucket": "my_device_id",
                    "message": "Test",
                    "topic": "teste/TEMPERATURE",
                    "options": {"qos": 0, "retain": False},
                }
            )

============
Notification
============

Send Notification

You can add ref_id from a bucket or dashboard, if it is valid it will show up a button Go To
Dashboard Any account with share of the dashboard/bucket will receive too.

    **Parameters:**

        | **notification**: :ref:`NotificationCreate`
        | Notification Object


.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.Notification.send(
                {
                    title: "Example",
                    message: "Message Test",
                }
            )

===
PDF
===

Generate a PDF from html, url or base64

    **Parameters:**

        | **params**: :ref:`PDFParams`
        | Parameters used to generate the pdf

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.PDF.generate(
                {
                    base64: "base64"
                }
            )

===
SMS
===

Send SMS to phone number

    **Parameters:**

        | **sms**: :ref:`SMSData`
        | Data that sms will be send, number and message

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import Services

            services = Services()
            services.sms.send(
                {
                    "to": "434434434434",
                    "message": "Test",
                }
            )


.. toctree::

    Attachment_Type
    Email_Type
    MQTT_Type
    Notification_Type
    Pdf_Type
    SMS_Type



