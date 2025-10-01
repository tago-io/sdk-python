**Analysis Type**
=================


.. _ScriptFile:

ScriptFile
----------

    **Attributes:**

        | name: str

        | content: :ref:`Base64`

        | language: "node" or "python"



.. _AnalysisCreateInfo:

AnalysisCreateInfo
------------------

    **Attributes:**

        | name: str

        | description: Optional[str]

        | interval: Optional[str]

        | run_on: Optional["tago" or "external"]

        | file_name: Optional[str]

        | runtime: Optional["node" or "python"]

        | active: Optional[bool]

        | profile: Optional[:ref:`GenericID`]

        | variables: Optional[List[Dict[str, Union[str, int, bool]]]]

        | tags: Optional[List[:ref:`TagsObj`]]



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
