Services
=========

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
            Attachment = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).Attachment

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
            console = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).console
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
            email = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).email
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
            mqtt = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).MQTT

            mqtt.publish(
                {
                    "bucket": "62756963c5b6db0013f1fc83",
                    "message": "hi",
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
            notification = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).Notification

            notification.send(
                {

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
            pdf = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).PDF

            pdf.publish(
                {

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
            sms = Services({"token": "cd48a6ea-1a36-4908-93e3-81be397b4989111"}).sms

            sms.send(
                {
                    "to": "434434434434",
                    "message": "Test",
                }
            )



