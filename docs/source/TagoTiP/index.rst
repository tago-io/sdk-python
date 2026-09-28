**TagoTiP**
===========

========
Instance
========

    **Parameters:**

        | **token**: str
        | Service Authorization token.

        | *Optional* **region**: str "us-e1" or "ue-w1" or "env"
        | Region is a optional parameter

.. code-block::
    :caption: **Example:**

        from tagoio_sdk import TagoTiP

        tagotip = TagoTiP({"token": "your-service-authorization-token"})


===
cmd
===

Send a command to a device through TagoTiP

Requires a Service Authorization token in the module token.

    **Parameters:**

        | **command**: :ref:`TagoTiPCommand`
        | Command object with serial, protocol and body

.. code-block::
    :caption: **Example:**

            from tagoio_sdk import TagoTiP

            tagotip = TagoTiP({"token": "your-service-authorization-token"})
            tagotip.cmd(
                {
                    "serial": "mqtt1",
                    "protocol": "mqtt",
                    "body": "reboot-now",
                }
            )


.. toctree::

    TagoTiP_Type
