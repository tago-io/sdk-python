**Actions Type**
================


.. _TriggerGeofenceValueType:

TriggerGeofenceValueType
------------------------

    **Attributes:**

        | center: Optional[List[float]]
        | E.g [longitude, latitude]

        | radius: Optional[float]

        | coordinates: Optional[List[List[float]]]
        | E.g [[longitude, latitude], [longitude, latitude], ...]


.. _ActionTypeScriptParams:

ActionTypeScriptParams
----------------------

    **Attributes:**

        | script: List[:ref:`GenericID`]

        | type: "script"


.. _ActionTypeNotificationParams:

ActionTypeNotificationParams
----------------------------

    **Attributes:**

        | message: str

        | subject: str

        | type: "notification"


.. _ActionTypeNotificationRunParams:

ActionTypeNotificationRunParams
-------------------------------

    **Attributes:**

        | message: str

        | subject: str

        | run_user: :ref:`GenericID`

        | type: "notification_run"


.. _ActionTypeEmailParams:

ActionTypeEmailParams
---------------------

    **Attributes:**

        | message: str

        | subject: str

        | to: str

        | type: "email"


.. _ActionTypeSMSParams:

ActionTypeSMSParams
-------------------

    **Attributes:**

        | message: str

        | to: str

        | type: "sms"


.. _ActionTypeMQTTParams:

ActionTypeMQTTParams
--------------------

    **Attributes:**

        | bucket: str

        | payload: str

        | topic: str

        | type: "mqtt"


.. _ActionTypePostParams:

ActionTypePostParams
--------------------

    **Attributes:**

        | headers: Dict

        | type: "post"

        | url: str


.. _ActionTriggerResourceType:

ActionTriggerResourceType
-------------------------

    **Attributes:**

        | resource: "device" or "bucket" or "file" or "analysis" or "action" or "am" or "user" or "financial" or "profile"

        | when: "create" or "update" or "delete"

        | tag_key: str

        | tag_value: str


.. _ActionTriggerIntervalType:

ActionTriggerIntervalType
-------------------------

    **Attributes:**

        | interval: str


.. _ActionTriggerCronType:

ActionTriggerCronType
---------------------

    **Attributes:**

        | timezone: Union[str, datetime]

        | cron: str
        | The cron expression


.. _ActionTriggerConditionType:

ActionTriggerConditionType
--------------------------

    **Attributes:**

        | device: str

        | variable: str

        | is: :ref:`Conditionals`

        | value: str

        | second_value: Optional[str]

        | value_type: "string" or "number" or "boolean" or "*"

        | unlock: Optional[bool]


.. _ActionTriggerUsageType:

ActionTriggerUsageType
----------------------

    **Attributes:**

        | service_or_resource: "input" or "output" or "analysis" or "data_records" or "sms" or "email" or "run_users" or "push_notification" or "file_storage" or "device" or "dashboard" or "action" or "tcore" or "team_members" or "am"

        | condition: "=" or ">"

        | condition_value: float


.. _ActionTriggerGeofenceType:

ActionTriggerGeofenceType
-------------------------

    **Attributes:**

        | device: str

        | variable: str

        | is: "IN" or "OUT"

        | value: :ref:`TriggerGeofenceValueType`

        | unlock: Optional[bool]


.. _ActionTriggerType:

ActionTriggerType
-----------------

    **Attributes:**

        ActionTriggerType is a Union of:

            | :ref:`ActionTriggerResourceType`
            | :ref:`ActionTriggerIntervalType`
            | :ref:`ActionTriggerCronType`
            | :ref:`ActionTriggerConditionType`
            | :ref:`ActionTriggerUsageType`
            | :ref:`ActionTriggerGeofenceType`

.. _ActionCreateInfo:

ActionCreateInfo
----------------

    **Attributes:**

        | name: str
        | The name for the action

        | profile: Optional[:ref:`GenericID`]
        | Profile identification

        | active: Optional[bool]
        | True if the action is active or not. The default is true

        | tags: Optional[List[:ref:`TagsObj`]]
        | An array of tags

        | description: Optional[str]
        | Description of the action

        | lock: Optional[bool]

        | type: Optional[str]
        | Type of action

        | trigger: Optional[List[:ref:`ActionTriggerType`]]
        | Array of trigger configuration according to type

        | action: Dict
        | Action configuration

        | trigger_when_unlock: Optional[bool]
        | Trigger the action when unlock condition is met


.. _ActionInfo:

ActionInfo(:ref:`ActionCreateInfo`)
-----------------------------------

    **Attributes:**

        | id: :ref:`GenericID`

        | last_triggered: :ref:`ExpireTimeOption`

        | updated_at: datetime

        | created_at: datetime


.. _MQTTResourceAction:

MQTTResourceAction
------------------

    **Attributes:**

        | client_id: str

        | connected_at: str

        | disconnect_at: Optional[str]


.. _ActionQuery:

ActionQuery(:ref:`Query`)
-------------------------

    **Attributes:**

        | fields: Optional[List["name" or "active" or "last_triggered" or "created_at" or "updated_at"]]
