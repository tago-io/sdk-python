**Run**
=======

Manage TagoRUN environment configuration and users.

====
info
====

Retrieves information about the current Run environment configuration.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_ | `Run Themes <https://help.tago.io/portal/en/kb/articles/run-themes>`_

    **Returns:**

        | :ref:`RunInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Profile** / **Access TagoRun settings** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.info()
        print(result)  # {'name': 'My Run Environment', 'logo': 'https://example.com/logo.png', ...}


====
edit
====

Updates the Run environment configuration settings.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_ | `Run Themes <https://help.tago.io/portal/en/kb/articles/run-themes>`_

    **Parameters:**

        | **data**: dict
        | Run configuration data to update

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Profile** / **Edit TagoRun settings** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.edit({"name": "My Run Environment", "logo": "https://example.com/logo.png"})
        print(result)  # TagoIO Run Successfully Updated


=========
listUsers
=========

Retrieves a paginated list of Run users with customizable fields and filtering options.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_

    **Parameters:**

        | **query**: :ref:`Query`
        | Query parameters for filtering and sorting

        .. code-block::
            :caption: **Default query:**

            query = {
                "page": 1,
                "fields": ["id", "name"],
                "filter": {},
                "amount": 20,
                "orderBy": ["name", "asc"]
            }

    **Returns:**

        | list[:ref:`UserInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", or return empty list check policy **Run User** / **Access** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.listUsers({
            "page": 1,
            "fields": ["id", "name", "email"],
            "amount": 20
        })
        print(result)  # [{'id': 'user-id-123', 'name': 'John Doe', 'email': 'example@email.com'}]


========
userInfo
========

Retrieves detailed information about a specific Run user.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

    **Returns:**

        | :ref:`UserInfo`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Access** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.userInfo("user-id-123")
        print(result)  # {'id': 'user-id-123', 'name': 'John Doe', 'email': 'example@email.com', ...}


==========
userCreate
==========

Creates a new user in the Run environment.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_

    **Parameters:**

        | **data**: :ref:`UserCreateInfo`
        | User creation data

    **Returns:**

        | dict

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Create** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.userCreate({
            "name": "John Doe",
            "email": "john@example.com",
            "password": "secure123",
            "timezone": "America/New_York"
        })
        print(result)  # {'user': 'user-id-123'}


========
userEdit
========

Updates information for an existing Run user.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

        | **data**: dict
        | User data to update

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Edit** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.userEdit("user-id-123", {"name": "Updated Name"})
        print(result)  # TagoIO Run User Successfully Updated


==========
userDelete
==========

Permanently deletes a user from the Run environment.

See: `TagoRun <https://help.tago.io/portal/en/kb/articles/191-tagorun>`_

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Delete** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.userDelete("user-id-123")
        print(result)  # Successfully Removed


===========
loginAsUser
===========

Generates a login token to authenticate as a specific Run user.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

        | *Optional* **options**: :ref:`LoginAsUserOptions`
        | Login options (e.g., expire_time)

    **Returns:**

        | :ref:`LoginResponse`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Login as user** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.loginAsUser("user-id-123")
        print(result["token"])  # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ...


=========
emailTest
=========

Tests the email configuration by sending a test message.

    **Parameters:**

        | **data**: :ref:`EmailTestData`
        | Email test data with subject and body

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.emailTest({"subject": "Test Email", "body": "This is a test message"})
        print(result)  # E-mail sent to example@email.com


================
notificationList
================

Retrieves a list of notifications for a specific Run user.

See: `Notifications for Users <https://help.tago.io/portal/en/kb/articles/223-notifications-for-users>`_

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

    **Returns:**

        | list[:ref:`NotificationInfo`]

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Access notification** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.notificationList("user-id-123")
        print(result)  # [{'id': 'notification-id-123', 'title': 'System Update', 'message': 'Features', ...}]


==================
notificationCreate
==================

Creates a new notification for a Run user.

See: `Notifications for Users <https://help.tago.io/portal/en/kb/articles/223-notifications-for-users>`_

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | User identification

        | **data**: :ref:`NotificationCreate`
        | Notification data

    **Returns:**

        | :ref:`NotificationCreateReturn`

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Create notification** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.notificationCreate("user-id-123", {
            "title": "Update",
            "message": "New feature available"
        })
        print(result)  # {'id': 'notification-id-123'}


================
notificationEdit
================

Updates an existing notification in the Run environment.

See: `Notifications for Users <https://help.tago.io/portal/en/kb/articles/223-notifications-for-users>`_

    **Parameters:**

        | **notificationID**: :ref:`GenericID`
        | Notification identification

        | **data**: dict
        | Notification data to update

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Edit notification** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.notificationEdit("notification-id-123", {"title": "Updated Title"})
        print(result)  # TagoIO Notification User Successfully Updated


==================
notificationDelete
==================

Deletes a notification from the Run environment.

See: `Notifications for Users <https://help.tago.io/portal/en/kb/articles/223-notifications-for-users>`_

    **Parameters:**

        | **notificationID**: :ref:`GenericID`
        | Notification identification

    **Returns:**

        | str

    .. code-block:: python

        # If receive an error "Authorization Denied", check policy **Run User** / **Delete notification** in Access Management.
        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.run.notificationDelete("notification-id-123")
        print(result)  # Successfully Removed


===========
ssoSAMLInfo
===========

Retrieves the SAML Single Sign-On configuration information for the Run environment.

See: `Single Sign-On (SSO) <https://help.tago.io/portal/en/kb/articles/491-single-sign-on-sso>`_

    **Returns:**

        | :ref:`RunSAMLInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.ssoSAMLInfo()
        print(result)  # {'sp': {'entity_id': 'https://example.com', ...}, ...}


===========
ssoSAMLEdit
===========

Updates the SAML SSO configuration for the Run environment.

See: `Single Sign-On (SSO) <https://help.tago.io/portal/en/kb/articles/491-single-sign-on-sso>`_

    **Parameters:**

        | **data**: :ref:`RunSAMLEditInfo`
        | SAML SSO configuration data

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.ssoSAMLEdit({
            "active": True,
            "idp_metadata": "<xml>...</xml>"
        })
        print(result)  # TagoIO Run SAML SSO Successfully Updated


==================
createCustomDomain
==================

Creates a custom domain configuration for the Run environment.

See: `Custom Domain Configuration <https://help.tago.io/portal/en/kb/articles/custom-domain-configuration>`_

    **Parameters:**

        | **profile_id**: str
        | Profile identification

        | **customDomainData**: :ref:`CustomDomainCreate`
        | Custom domain configuration data

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.createCustomDomain("profile-id-123", {
            "domain": "app.mycompany.com"
        })
        print(result)  # Custom domain created successfully


===============
getCustomDomain
===============

Retrieves the custom domain configuration for a Run profile.

See: `Custom Domain Configuration <https://help.tago.io/portal/en/kb/articles/custom-domain-configuration>`_

    **Parameters:**

        | **profile_id**: str
        | Profile identification

    **Returns:**

        | :ref:`CustomDomainInfo`

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.getCustomDomain("profile-id-123")
        print(result)  # {'domain': 'app.mycompany.com', 'verified': True, ...}


==================
deleteCustomDomain
==================

Removes the custom domain configuration from a Run profile.

See: `Custom Domain Configuration <https://help.tago.io/portal/en/kb/articles/custom-domain-configuration>`_

    **Parameters:**

        | **profile_id**: str
        | Profile identification

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.deleteCustomDomain("profile-id-123")
        print(result)  # Custom domain deleted successfully


======================
regenerateCustomDomain
======================

Regenerates the custom domain configuration for a Run profile.

See: `Custom Domain Configuration <https://help.tago.io/portal/en/kb/articles/custom-domain-configuration>`_

    **Parameters:**

        | **profile_id**: str
        | Profile identification

    **Returns:**

        | str

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources({"token": "YOUR-PROFILE-TOKEN"})
        result = resources.run.regenerateCustomDomain("profile-id-123")
        print(result)  # Custom domain regenerated successfully


.. toctree::

    Run_Types
