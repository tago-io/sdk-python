**Integration Connector Type**
==============================


.. _ConnectorIDeviceParameters:

IDeviceParameters
-----------------

    **Attributes:**

        | **name**: Optional[str]
        | Name of the device parameter.

        | **label**: Optional[str]
        | Display label for the device parameter.

        | **type**: Optional["text" or "dropdown" or "switch" or "number"]
        | The type of input for the device parameter.

        | **default**: Any
        | Default value for the device parameter.

        | **group**: Optional["default" or "main" or "advanced" or "hide"]
        | Group category for the device parameter.

        | **options**: Optional[List[Any]]
        | List of options (Optional only for dropdown).


.. _ConnectorCreateInfo:

ConnectorCreateInfo
-------------------

    **Attributes:**

        | **name**: Optional[str]
        | The name of the connector.

        | **description**: Optional[str]
        | Description of the connector.

        | **logo_url**: Optional[str]
        | URL for the connector's logo image.

        | **device_parameters**: Optional[List[:ref:`ConnectorIDeviceParameters`]]
        | List of device parameters for the connector.

        | **networks**: Optional[List[:ref:`GenericID`]]
        | List of network IDs associated with the connector.

        | **payload_encoder**: Optional[str]
        | Function to encode payload data.

        | **payload_decoder**: Optional[str]
        | Base64 decoded string for parsing payload data.

        | **install_text**: Optional[str]
        | Refers to the **description** in the Documentation settings.

        | **install_end_text**: Optional[str]
        | Refers to the **completion text** in the Documentation settings.

        | **device_annotation**: Optional[str]
        | Additional notes or annotations for the device.


.. _ConnectorInfo:

ConnectorInfo(:ref:`ConnectorCreateInfo`)
-----------------------------------------

    **Attributes:**

        | **id**: :ref:`GenericID`
        | Unique identifier for the connector.

        | **public**: bool
        | Indicates if the connector is public.

        | **description**: Optional[str]
        | Description of the connector.

        | **logo_url**: Optional[str]
        | URL for the connector's logo image.

        | **created_at**: datetime
        | Date and time when the connector was created.

        | **updated_at**: datetime
        | Date and time when the connector was last updated.

        | **device_parameters**: Optional[List[:ref:`ConnectorIDeviceParameters`]]
        | List of device parameters for the connector.

        | **networks**: Optional[List[:ref:`GenericID`]]
        | List of network IDs associated with the connector.

        | **install_text**: Optional[str]
        | Refers to the **description** in the Documentation settings.

        | **install_end_text**: Optional[str]
        | Refers to the **completion text** in the Documentation settings.

        | **device_annotation**: Optional[str]
        | Additional notes or annotations for the device.


.. _ConnectorQuery:

ConnectorQuery(:ref:`Query`)
----------------------------

    **Attributes:**

        | **fields**: Optional[List["name" or "id" or "description" or "logo_url" or "install_text" or "install_end_text" or "device_annotation" or "payload_decoder" or "networks"]]
        | List of fields to include in query results.

        | **filters**: Optional[:ref:`ConnectorInfo`]
        | Filter criteria for the connector query.
