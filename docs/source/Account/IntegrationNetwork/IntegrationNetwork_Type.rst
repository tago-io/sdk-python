**Integration Network Type**
=================


.. _serial_number:

serial_number
-----------------
    **Attributes:**

        | **mask**: Optional[str]
        | **label**: Optional[str]
        | **image**: Optional[str]
        | **case**: Optional[str]
        | **help**: Optional[str]
        | **required**: bool


.. _IDeviceParameters:

IDeviceParameters
-----------------
    **Attributes:**

        | **name**: Optional[str]
        | **label**: Optional[str]
        | **type**: Optional["text" or "dropdown" or "switch" or "number"]
        | **default**: Optional[any]
        | **group**: Optional["default" or "main" or "advanced" or "hide"]
        | **options**: Optional[list[any]]


.. _NetworkCreateInfo:

NetworkCreateInfo
-----------------
    **Attributes:**

        | **name**: Optional[str]
        | **description**: Optional[str]
        | **logo_irl**: Optional[str]
        | **icon_url**: Optional[str]
        | **banner_url**: Optional[str]
        | **device_parameters**: Optional[list[IDeviceParameters]]
        | **middleware_endpoint**: Optional[str]
        | **payload_encoder**: Optional[str]
        | **payload_decoder**: Optional[str]
        | **public**: Optional[bool]
        | **documentation_url**: Optional[str]
        | **serial_number**: Optional[serial_number]
        | **require_devices_access**: Optional[bool]


.. _NetworkInfo:

NetworkInfo
-----------------
    **Attributes:**

        | **id**: GenericID
        | **name**: Optional[str]
        | **description**: Optional[str]
        | **logo_url**: Optional[str]
        | **icon_url**: Optional[str]
        | **banner_url**: Optional[str]
        | **device_parameters**: Optional[list[IDeviceParameters]]
        | **middleware_endpoint**: Optional[str]
        | **payload_encoder**: Optional[str]
        | **payload_decoder**: Optional[str]
        | **public**: Optional[bool]
        | **documentation_url**: Optional[str]
        | **serial_number**: Optional[serial_number]


.. _NetworkTokenInfo:

NetworkTokenInfo
-----------------
    **Attributes:**

        | **id**: GenericID
        | **created_at**: datetime
        | **updated_at**: datetime
        | **Network**: GenericID
        | **type**: "type" or "Network"


.. _NetworkQuery:

NetworkQuery
---------------

    NetworkQuery = Union[
        Query and
        Literal[
            "name" or
            "description" or
            "logo_url" or
            "icon_url" or
            "banner_url" or
            "device_parameters" or
            "middleware_endpoint" or
            "payload_encoder" or
            "payload_decoder" or
            "serial_number" or
            "documentation_url" or
            "public" or
            "created_at" or
            "updated_at"
        ]
    ]
