**Profile**
===========

Manage profiles in your TagoIO account.

====
info
====

Retrieves detailed information about a specific profile using its ID or 'current' for the active profile.

See: `Profiles <https://help.tago.io/portal/en/kb/articles/198-profiles>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification (use "current" for the active profile)

    **Returns:**

        | :ref:`ProfileInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        profile_info = resources.profile.info("profile-id-123")
        # Or get current profile
        current_profile = resources.profile.info("current")
        print(profile_info)  # {'info': {'id': 'profile-id-123', 'account': 'account-id-123', ...}, ...}


====
list
====

Retrieves a list of all profiles associated with the current account.

See: `Profiles <https://help.tago.io/portal/en/kb/articles/198-profiles>`_

    **Returns:**

        | list[:ref:`ProfileListInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.list()
        print(result)  # [{'id': 'profile-id-123', 'name': 'Profile Test', ...}]


=======
summary
=======

Retrieves a summary of the profile's usage and statistics.

See: `Profiles <https://help.tago.io/portal/en/kb/articles/198-profiles>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

    **Returns:**

        | :ref:`ProfileSummary`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Account** / **Access profile** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.summary("profile-id-123")
        print(result)  # {'amount': {'device': 10, 'bucket': 10, 'dashboard': 5, ...}, ...}


=========
tokenList
=========

Retrieves a list of all tokens associated with a specific profile.

See: `Account Token <https://help.tago.io/portal/en/kb/articles/495-account-token>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | *Optional* **queryObj**: :ref:`Query`
        | Query parameters to filter the results

        .. code-block::
            :caption: **Default queryObj:**

            queryObj = {
                "page": 1,
                "amount": 20,
                "fields": ["name", "token", "permission"],
                "filter": {},
                "orderBy": ["created_at", "asc"]
            }

    **Returns:**

        | list[:ref:`TokenDataList`]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.tokenList("profile-id-123", {
            "page": 1,
            "amount": 20,
            "fields": ["name", "token", "permission"]
        })
        print(result)  # [{'name': 'Token #1', 'token': 'token-value', 'permission': 'full', ...}, ...]


======
create
======

Creates a new profile with the specified name and optional resource allocation settings.

See: `Profiles <https://help.tago.io/portal/en/kb/articles/198-profiles>`_

    **Parameters:**

        | **profileObj**: :ref:`ProfileCreateInfo`
        | Profile information to create

        | *Optional* **allocate_free_resources**: bool
        | Whether to allocate free resources to the new profile (default: False)

    **Returns:**

        | dict with key "id" containing the new profile ID

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.create({"name": "New Profile"}, allocate_free_resources=True)
        print(result)  # {'id': 'profile-id-123'}


====
edit
====

Updates profile information with the provided data.

See: `Profiles <https://help.tago.io/portal/en/kb/articles/198-profiles>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **profileObj**: dict
        | Profile information to update

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.edit("profile-id-123", {"name": "Updated Profile Name"})
        print(result)  # Successfully Updated


======
delete
======

Permanently removes a profile from the account.

See: `Two-Factor Authentication (2FA) <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **credentials**: :ref:`ProfileCredentials`
        | Account credentials (password and pin_code if 2FA is enabled)

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        # The "pin_code" field is required when 2FA is activated
        result = resources.profile.delete("profile-id-123", {"password": "your-password", "pin_code": "123456"})
        print(result)  # Successfully Removed


==================
usageStatisticList
==================

Retrieves usage statistics for a profile within a specified time period.

Usage statistics are cumulative: if a service was not used in a time period, the statistics for that time period will not be in the object.

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | *Optional* **dateObj**: :ref:`StatisticsDate`
        | Date range and periodicity parameters

    **Returns:**

        | list[:ref:`UsageStatistic`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Account** / **Access profile statistics** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.usageStatisticList("profile-id-123", {
            "start_date": "2024-09-01",
            "end_date": "2024-12-31",
            "periodicity": "day"
        })
        print(result)  # [{'time': '2024-09-02T00:01:29.749Z', 'analysis': 0.07, 'data_records': 67254, ...}, ...]


========
auditLog
========

Creates a new audit log query for tracking profile activities.

See: `Audit Log <https://help.tago.io/portal/en/kb/articles/audit-log>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | *Optional* **filterObj**: :ref:`AuditLogFilter`
        | Filters to apply to the audit log query

    **Returns:**

        | :ref:`AuditLog`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.auditLog("profile-id-123", {
            "start_date": "2024-12-01",
            "end_date": "2024-12-07"
        })
        print(result)


==============
auditLogQuery
==============

Retrieves audit log entries using a previously created query.

See: `Audit Log <https://help.tago.io/portal/en/kb/articles/audit-log>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **queryId**: str
        | Query ID from a previous auditLog call

    **Returns:**

        | :ref:`AuditLog`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.auditLogQuery("profile-id-123", "query-id-456")
        print(result)


===========
serviceEdit
===========

Updates service configuration and resource limits for a profile.

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **serviceObj**: dict
        | Service configuration and resource limits to update

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.serviceEdit("profile-id-123", {
            "input": 350000,
            "output": 342153,
            "analysis": 5
        })
        print(result)  # Profile resource allocation Successfully Updated


=================================
transferTokenToAnotherProfile
=================================

Transfers the current authentication token to another profile.

    **Parameters:**

        | **targetProfileID**: :ref:`GenericID`
        | Target profile identification

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.transferTokenToAnotherProfile("target-profile-123")
        print(result)


===========
tokenCreate
===========

Creates a new authentication token for the specified profile.

See: `Account Token <https://help.tago.io/portal/en/kb/articles/495-account-token>`_

See: `Two-Factor Authentication (2FA) <https://help.tago.io/portal/en/kb/articles/526-two-factor-authentication>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **tokenParams**: :ref:`CommonTokenData`
        | Token parameters including name, permission, email, and password

    **Returns:**

        | :ref:`TokenCreateResponse`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        # The "pin_code" / "otp_type" field is required when 2FA is activated
        result = resources.profile.tokenCreate("profile-id-123", {
            "name": "API Access",
            "permission": "full",
            "email": "example@email.com",
            "password": "your-password"
        })
        print(result)  # {'token': 'token-value', 'name': 'API Access', ...}


===========
tokenDelete
===========

Revokes and removes an authentication token from the profile.

See: `Account Token <https://help.tago.io/portal/en/kb/articles/495-account-token>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **token**: :ref:`GenericToken`
        | Token to be deleted

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.tokenDelete("profile-id-123", "token-xyz")
        print(result)  # Token Successfully Removed


=============
addTeamMember
=============

Adds a new team member to the profile using their email address.

See: `Team Management - Sharing your Profile <https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **email**: str
        | Email address of the team member to invite

    **Returns:**

        | str - Success message

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.addTeamMember("profile-id-123", "user@example.com")
        print(result)  # User invited


========
teamList
========

Retrieves a list of all team members that have access to the specified profile.

See: `Team Management - Sharing your Profile <https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

    **Returns:**

        | list[:ref:`ProfileTeam`]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.profile.teamList("profile-id-123")
        print(result)  # [{'id': 'account-id-123', 'active': False, 'name': 'John Doe', ...}, ...]


================
deleteTeamMember
================

Removes a team member from the profile.

See: `Team Management - Sharing your Profile <https://help.tago.io/portal/en/kb/articles/106-sharing-your-profile>`_

    **Parameters:**

        | **profileID**: :ref:`GenericID`
        | Profile identification

        | **accountId**: str
        | Account ID of the team member to remove

    **Returns:**

        | str - Success message

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.profile.deleteTeamMember("profile-id-123", "account-id-456")
        print(result)  # Account Successfully Removed


.. toctree::

    Profile_Types
