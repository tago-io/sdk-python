**Analysis**
============

Manage analysis in account.

=======
list
=======

Retrieves a list with all analyses from the account

    **Parameters:**

        | *Optional* **queryObj**: :ref:`AnalysisQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj: {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name","asc"],
            }

    **Returns:**

        | list[:ref:`AnalysisListItem`]

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.list()


=======
create
=======

Create a new analysis

    **Parameters:**

        | **analysisInfo**: :ref:`AnalysisCreateInfo`
        | Analysis information

    **Returns:**

        | Dict[str, GenericID | GenericToken]

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.create({
                "name": "My Analysis",
                "runtime": "python",
                "active": True,
            })


=======
edit
=======

Modify any property of the analyze

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

        | **analysisInfo**: :ref:`AnalysisCreateInfo`
        | Analysis information

    **Returns:**

        | string

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.edit("analysisID", { "name": "My Analysis Edited" })


=======
delete
=======

Deletes an analysis from the account

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

    **Returns:**

        | string

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.delete("analysisID")


=======
info
=======

Gets information about an analysis

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

    **Returns:**

        | :ref:`AnalysisInfo`

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.info("analysisID")


=======
run
=======

Run an analysis

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

    **Returns:**

        | Dict[str, GenericToken]

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.run("analysisID")


=============
tokenGenerate
=============

Generate a new token for the analysis

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

    **Returns:**

        | Dict[str, str]

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.tokenGenerate("analysisID")


============
uploadScript
============

Upload a file (base64) to Analysis. Automatically erase the old one

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

        | **file**: :ref:`ScriptFile`
        | File information

    **Returns:**

        | string

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources
            import base64

            data = "print(Hello, World!)"
            encoded_bytes = base64.b64encode(data.encode('utf-8')).decode('utf-8')

            resources = Resources()
            resources.analysis.uploadScript("analysisID", {
                "name": "My Script",
                "content": encoded_bytes,
                "language": "python",
            })


==============
downloadScript
==============

Get a url to download the analysis. If `version` is specified in `options`, downloads a specific version.

    **Parameters:**

        | **analysisID**: GenericID: str
        | Analysis ID

        | *Optional* **options**: Dict["version", int]
        | Options

    **Returns:**

        | Dict[str, Any]

    .. code-block::
        :caption: **Example:**

            from tagoio_sdk import Resources

            resources = Resources()
            resources.analysis.downloadScript("analysisID")

.. toctree::

    Analysis_Type
