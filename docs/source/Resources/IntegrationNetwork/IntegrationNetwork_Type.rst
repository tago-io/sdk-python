**Integration Network Type**
============================


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


.. _NetworkIDeviceParameters:

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


.. _DeviceNetworkToken:

DeviceNetworkToken
------------------
    **Attributes:**

        | **token**: uuid
        | **network**: GenericID
        | **name**: str
        | **created_at**: datetime


.. _IntegrationTokenData:

TokenData
-----------------
    **Attributes:**

        | **name**: str
        | **expire_time**: Optional[ExpireTimeOption]
        | **permission**: PermissionOption
        | **serie_number**: Optional[str]
        | **verification_code**: Optional[str]
        | **middleware**: Optional[str]
