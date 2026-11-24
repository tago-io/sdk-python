**Utils**
============

=========
envToJson
=========

Converts **Environment Variables** from the analysis to an object.

    **Parameters:**

        | **environment**: list[dict[key: str, value: str]]
        | Array of environment items from TagoIO.

    **Returns:**

        | **result**: dict[key: str, value: str]
        | Object representing the converted environment array.

    .. code-block::
        :caption: **Example:**

            EXAMPLE_OF_ENVIRONMENT_VARIABLES_FROM_THE_ANALYSIS = [
                {"key": "temperature", "value": "25"},
                {"key": "temperature", "value": "60"},
                {"key": "humidity", "value": "27"},
            ]

            from tagoio_sdk.modules.Utils.envToJson import envToJson


            def my_analysis(context, scope: list):
                env = envToJson(context.environment)
                # env = {
                #   'temperature': '60',
                #   'humidity': '27',
                # }

    **Note:**

    This method will replace duplicate keys with the last one.
