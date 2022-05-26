Services
=========

================
**Constructors**
================

    **Parameters:**

        | **token**: str
        | Analysis Token

        | *Optional* **region**: Regions
        | region is optional parameter, the type is Regions = Literal["usa-1", "env"]

.. code-block::
    :caption: **Example:**

        from tagoio_sdk.modules.Services.Services import Services

        myServices = Services({"token": "my_analysis_token", "region": "usa-1})


==============
**Attachment**
==============

Send Attachment

    **Parameters:**

        | **archive**: ArchiveFile
        | Archive JSON Object

.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            Attachment = Services({"token": "my_analysis_token"}).Attachment

            Attachment.upload(
                {
                    "name": "Test",
                    "content": "base64",
                    "type": "Test",
                }
            )

==================
**ConsoleService**
==================

Log message in analysis console

    **Parameters:**

        | **message**: str
        | Log message

        | *Optional* **time**: datetime
        | Date of message

.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            console = Services({"token": "my_analysis_token"}).console
            console.log(
                {
                    "message": "Test",
                }
            )

=========
**Email**
=========

Send Email

    **Parameters:**

        | **email**: Union[Any, EmailWithRawText, EmailWithHTML, EmailWithTemplate]
        | Email objects

.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            email = Services({"token": "my_analysis_token"}).email
            email.send(
                {
                    "to": "myclien@tago.io",
                    "subject": "Test Subject",
                }
            )

========
**MQTT**
========

Publish to a MQTT Device

    **Parameters:**

        | **mqtt**: MQTTData
        | MQTT object, contains topic, bucket, message and options(retain and qos)


.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            mqtt = Services({"token": "my_analysis_token"}).MQTT

            mqtt.publish(
                {
                    "bucket": "my_device_id",
                    "message": "Test",
                    "topic": "teste/TEMPERATURE",
                    "options": {"qos": 0, "retain": False},
                }
            )

================
**Notification**
================

Send Notification

You can add ref_id from a bucket or dashboard, if it is valid it will show up a button Go To
Dashboard Any account with share of the dashboard/bucket will receive too.

    **Parameters:**

        | **notification**: NotificationCreate
        | Notification Object


.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            notification = Services({"token": "my_analysis_token"}).Notification

            notification.send(
                {
                    title: "Example",
                    message: "Message Test",
                }
            )

=======
**PDF**
=======

Generate a PDF from html, url or base64

    **Parameters:**

        | **params**: PDFParams
        | Parameters used to generate the pdf

.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            pdf = Services({"token": "my_analysis_token"}).PDF

            pdf.generate(
                {
                    base64: "base64"
                }
            )

=======
**SMS**
=======

Send SMS to phone number

    **Parameters:**

        | **sms**: SMSData
        | Data that sms will be send, number and message

.. code-block::
    :caption: **Example:**

            from tagoio_sdk.modules.Services.Services import Services

            sms = Services({"token": "my_analysis_token"}).sms

            sms.send(
                {
                    "to": "434434434434",
                    "message": "Test",
                }
            )



