**Analysis Type**
=================


.. _ScriptFile:

ScriptFile
----------

    **Attributes:**

        | name: str

        | content: :ref:`Base64`

        | language: :ref:`RunTypeOptions`



.. _AnalysisCreateInfo:

AnalysisCreateInfo
------------------

    **Attributes:**

        | name: str

        | description: Optional[str]

        | interval: Optional[str]

        | run_on: Optional["tago" or "external"]

        | file_name: Optional[str]

        | runtime: Optional[:ref:`RunTypeOptions`]

        | active: Optional[bool]

        | profile: Optional[:ref:`GenericID`]

        | variables: Optional[List[Dict[str, Union[str, int, bool]]]]

        | tags: Optional[List[:ref:`TagsObj`]]

        | mqtt: Optional[:ref:`AnalysisMqttChanges`]
        | MQTT Endpoint settings. Luau Analyses only; other runtimes answer 400.



.. _AnalysisInfo:

AnalysisInfo(:ref:`AnalysisCreateInfo`)
---------------------------------------

    **Attributes:**

        | id: :ref:`GenericID`

        | token: str

        | last_run: :ref:`ExpireTimeOption`

        | created_at: datetime

        | updated_at: datetime

        | locked_at: Any

        | console: Optional[List[str]]

        | mqtt: NotRequired[:ref:`AnalysisMqtt`]
        | MQTT Endpoint state. Returned by info, not by list. Absent on servers without the MQTT Endpoint, such as older TagoDeploy instances.


.. _AnalysisMqttEvents:

AnalysisMqttEvents
------------------

    Session events of the MQTT Endpoint that also run the code; a PUBLISH always runs it.
    Each event is opt-in and off by default. info returns all three keys; create and edit accept any subset.

    **Attributes:**

        | connect: bool
        | Run the code when a device connects. Off by default.

        | subscribe: bool
        | Run the code once per filter when a device subscribes. Off by default.

        | unsubscribe: bool
        | Run the code once per filter when a device unsubscribes. Off by default.


.. _AnalysisMqttPorts:

AnalysisMqttPorts
-----------------

    Ports devices use to reach the MQTT Endpoint.

    **Attributes:**

        | plain: int
        | Port without TLS.

        | secure: int
        | Port with TLS.


.. _AnalysisMqttChanges:

AnalysisMqttChanges
-------------------

    MQTT Endpoint settings on create and edit. Edit merges them into the stored settings.
    Turning the MQTT Endpoint or an event on needs a paid plan (Lite, Pro, or Max; TagoDeploy instances are not gated).
    On a Free account the request is refused with "The MQTT Endpoint needs a paid plan. Upgrade to use it.";
    turning things off is always allowed.

    **Attributes:**

        | active: Optional[bool]
        | Turns the MQTT Endpoint on or off. Luau Analyses only. Off by default.

        | events: Optional[:ref:`AnalysisMqttEvents`]
        | Session events to turn on or off.


.. _AnalysisMqtt:

AnalysisMqtt(:ref:`AnalysisMqttChanges`)
----------------------------------------

    MQTT Endpoint state of an Analysis, as info returns it.

    **Attributes:**

        | host: Optional[str]
        | Read only. Host devices connect to; present only when the instance configures one.

        | ports: Optional[:ref:`AnalysisMqttPorts`]
        | Read only. Ports devices connect to; present only with host.


.. _AnalysisMqttOutcome:

AnalysisMqttOutcome
-------------------

    How an MQTT Endpoint test run ended.

    **Type:**

        | Literal["ran", "failed", "refused", "rate_limited", "too_large"]


.. _AnalysisMqttTry:

AnalysisMqttTry
---------------

    Message for an MQTT Endpoint test run.

    **Attributes:**

        | topic: str
        | Topic name, without +, #, or NUL.

        | payload: str
        | Payload the code receives, as a string.

        | qos: Optional[0 or 1 or 2]
        | QoS of the message. Default 1.


.. _AnalysisMqttTryResult:

AnalysisMqttTryResult
---------------------

    Result of an MQTT Endpoint test run.

    **Attributes:**

        | outcome: :ref:`AnalysisMqttOutcome`
        | How the run ended.

        | duration_ms: int
        | Time the run took to answer, admission wait included, in milliseconds.


.. _AnalysisQuery:

AnalysisQuery(:ref:`Query`)
---------------------------

    **Attributes:**

        | fields: Optional[List["name" or "active" or "run_on" or "last_run" or "created_at" or "updated_at"]]


.. _AnalysisListItem:

AnalysisListItem
----------------

    **Attributes:**

        | id: Optional[:ref:`GenericID`]

        | name: Optional[str]

        | active: Optional[bool]

        | run_on: Optional["tago" or "external"]

        | last_run: Optional[:ref:`ExpireTimeOption`]

        | created_at: Optional[datetime]

        | updated_at: Optional[datetime]

        | locked_at: Optional[datetime]

        | console: Optional[List[str]]


.. _SnippetRuntime:

SnippetRuntime
--------------

    Available runtime environments for snippets.

    **Type:**

        | Literal["node-legacy", "python-legacy", "node-rt2025", "python-rt2025", "deno-rt2025"]


.. _SnippetItem:

SnippetItem
-----------

    Individual snippet metadata.

    **Attributes:**

        | id: str
        | Unique identifier for the snippet

        | title: str
        | Human-readable title

        | description: str
        | Description of what the snippet does

        | language: str
        | Programming language (typescript, javascript, python)

        | tags: List[str]
        | Array of tags for categorization

        | filename: str
        | Filename of the snippet

        | file_path: str
        | Full path to the file in the runtime directory


.. _SnippetsListResponse:

SnippetsListResponse
--------------------

    API response containing all snippets metadata for a runtime.

    **Attributes:**

        | runtime: :ref:`SnippetRuntime`
        | Runtime environment identifier

        | schema_version: int
        | Schema version for the API response format

        | generated_at: str
        | ISO timestamp when the response was generated

        | snippets: List[:ref:`SnippetItem`]
        | Array of all available snippets for this runtime
