**Analysis**
============

Manage analysis in your application.

=======
list
=======

Lists all analyses from the application with pagination support.
Use this to retrieve and manage analyses in your application.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`AnalysisQuery`
        | Query parameters to filter the results.

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"]
            }

    **Returns:**

        | list[:ref:`AnalysisListItem`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        list_result = resources.analyses.list({
            "page": 1,
            "fields": ["id", "name"],
            "amount": 10,
            "orderBy": ["name", "asc"]
        })
        print(list_result)  # [{'id': 'analysis-id-123', 'name': 'Analysis Test', ...}]


=======
create
=======

Creates a new analysis in your application.

See: `Creating Analysis <https://help.tago.io/portal/en/kb/articles/120-creating-analysis>`_

    **Parameters:**

        | **analysisObj**: :ref:`AnalysisCreateInfo`
        | Data object to create new TagoIO Analysis

    **Returns:**

        | Dict[str, GenericID | GenericToken]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        new_analysis = resources.analyses.create({
            "name": "My Analysis",
            "runtime": "python",
            "tags": [{"key": "type", "value": "data-processing"}]
        })
        print(new_analysis["id"], new_analysis["token"])  # analysis-id-123, analysis-token-123


=======
edit
=======

Modifies an existing analysis.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

        | **analysisObj**: :ref:`AnalysisInfo`
        | Analysis object with data to replace

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Create" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.analyses.edit("analysis-id-123", {
            "name": "Updated Analysis",
            "active": False
        })
        print(result)  # Successfully Updated


=======
delete
=======

Deletes an analysis from your application.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Delete" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.analyses.delete("analysis-id-123")
        print(result)  # Successfully Removed


=======
info
=======

Retrieves detailed information about a specific analysis.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

    **Returns:**

        | :ref:`AnalysisInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Access" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        analysis_info = resources.analyses.info("analysis-id-123")
        print(analysis_info)  # {'id': 'analysis-id-123', 'name': 'My Analysis', ...}


=======
run
=======

Executes an analysis with optional scope parameters.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

        | *Optional* **scopeObj**: Dict[str, Any]
        | Simulate scope for analysis

    **Returns:**

        | Dict[str, GenericToken]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Run Analysis" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.analyses.run("analysis-id-123", {"environment": "production"})
        print(result["analysis_token"])  # analysis-token-123


=============
tokenGenerate
=============

Generates a new token for the analysis.
This is only allowed when the analysis is running in external mode.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

    **Returns:**

        | Dict[str, str]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        token = resources.analyses.tokenGenerate("analysis-id-123")
        print(token["analysis_token"])  # analysis-token-123


============
uploadScript
============

Uploads a script file to an analysis.
The file content must be base64-encoded. This automatically replaces the old script.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

        | **fileObj**: :ref:`ScriptFile`
        | Object with name, language and content (base64) of the file

    **Returns:**

        | string

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Upload Analysis Script" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.analyses.uploadScript("analysis-id-123", {
            "name": "script.py",
            "content": "base64-encoded-content",
            "language": "python"
        })
        print(result)  # Successfully Uploaded


==============
downloadScript
==============

Gets a download URL for the analysis script.
If version is specified in options, downloads a specific version.

See: `Analysis <https://docs.tago.io/docs/tagoio/analysis/>`_

    **Parameters:**

        | **analysisID**: str
        | Analysis identification

        | *Optional* **options**: Dict[Literal["version"], int]
        | Options for the Analysis script to download (e.g., {"version": 1})

    **Returns:**

        | Dict

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy "Analysis" / "Download Analysis Script" in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        download = resources.analyses.downloadScript("analysis-id-123", {"version": 1})
        print(download["url"])  # https://...
        print(download["expire_at"])  # 2025-01-13T...


============
listSnippets
============

Get all available snippets for a specific runtime environment.
Fetches analysis code snippets from the public TagoIO snippets repository.

See: `Script Examples <https://help.tago.io/portal/en/kb/articles/64-script-examples>`_

See: `Script Editor <https://help.tago.io/portal/en/kb/articles/104-script-editor>`_

    **Parameters:**

        | **runtime**: :ref:`SnippetRuntime`
        | The runtime environment to get snippets for

    **Returns:**

        | :ref:`SnippetsListResponse`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        deno_snippets = resources.analyses.listSnippets("deno-rt2025")

        # Print all snippet titles
        for snippet in deno_snippets["snippets"]:
            print(f"{snippet['title']}: {snippet['description']}")


==============
getSnippetFile
==============

Get the raw source code content of a specific snippet file.
Fetches the actual code content from the TagoIO snippets repository.

See: `Script Examples <https://help.tago.io/portal/en/kb/articles/64-script-examples>`_

See: `Script Editor <https://help.tago.io/portal/en/kb/articles/104-script-editor>`_

    **Parameters:**

        | **runtime**: :ref:`SnippetRuntime`
        | The runtime environment the snippet belongs to

        | **filename**: str
        | The filename of the snippet to retrieve

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()

        # Get TypeScript code for console example
        code = resources.analyses.getSnippetFile("deno-rt2025", "console.ts")
        print(code)

        # Get Python code for data processing
        python_code = resources.analyses.getSnippetFile("python-rt2025", "avg-min-max.py")
        print(python_code)

.. toctree::

    Analysis_Type
