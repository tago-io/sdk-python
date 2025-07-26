
**Run**
========

Manage services in account.

=======
info
=======

Get information about the TagoRUN service.

        **Returns**

            | **result**: :ref:`RunInfo`
            | Information about the TagoRUN service.


=======
edit
=======

Edit the TagoRUN service information.

    **Parameters:**

        | **data**: :ref:`RunInfo`
        | Updated information for the TagoRUN service.

    **Returns:**

        | **result**: str
        | Success message.


============
listUsers
============

List users in the TagoRUN service.

    **Parameters:**

        | **query**: :ref:`Query`
        | Query parameters for filtering and sorting the user list.

    **Returns:**

        | **result**: list[:ref:`UserInfo`]
        | List of user information.


============
userInfo
============

Get information about a specific user in the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

    **Returns:**

        | **result**: :ref:`UserInfo`
        | Information about the user.


================
userCreate
================

Create a new user in the TagoRUN service.

    **Parameters:**

        | **data**: :ref:`UserCreateInfo`
        | Information for creating the user.

    **Returns:**

        | **result**: str
        | Success message.


================
userCreate
================

Create a new user in the TagoRUN service.

    **Parameters:**

        | **data**: :ref:`UserCreateInfo`
        | Information for creating the user.

    **Returns:**

        | **result**: str
        | Success message.


================
userEdit
================

Edit information about a specific user in the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

        | **data**: :ref:`UserInfo`
        | Updated information for the user.

    **Returns:**

        | **result**: str
        | Success message.


==================
userDelete
==================

Delete a specific user from the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

    **Returns:**

        | **result**: str
        | Success message.


==================
loginAsUser
==================

Log in as a specific user in the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

        | **options**: Optional[:ref:`LoginAsUserOptions`]
        | Additional options for the login.

    **Returns:**

        | **result**: :ref:`LoginResponse`
        | Login response.


================
emailTest
================

Send a test email from the TagoRUN service.

    **Parameters:**

        | **data**: :ref:`EmailBase`
        | Email data including subject and body.

    **Returns:**

        | **result**: str
        | Success message.


======================
notificationList
======================

List notifications for a specific user in the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

    **Returns:**

        | **result**: list[:ref:`NotificationInfo`]
        | List of notification information.


======================
notificationCreate
======================

Create a new notification for a specific user in the TagoRUN service.

    **Parameters:**

        | **userID**: :ref:`GenericID`
        | ID of the user.

        | **data**: :ref:`NotificationCreate`
        | Information for creating the notification.

    **Returns:**

        | **result**: :ref:`NotificationCreateReturn`
        | Information about the created notification.


======================
notificationEdit
======================

Edit information about a specific notification in the TagoRUN service.

    **Parameters:**

        | **notificationID**: :ref:`GenericID`
        | ID of the notification.

        | **data**: :ref:`NotificationCreate`
        | Updated information for the notification.

    **Returns:**

        | **result**: str
        | Success message.


======================
notificationDelete
======================

Delete a specific notification from the TagoRUN service.

    **Parameters:**

        | **notificationID**: :ref:`GenericID`
        | ID of the notification.

    **Returns:**

        | **result**: str
        | Success message.


============
ssoSAMLInfo
============

Get the SAML Single Sign-On information for the account's RUN.


============
ssoSAMLEdit
============

Edit the SAML Single Sign-On metadata and mappings for the account's RUN.

    **Parameters:**

        | **data**: :ref:`RunSAMLEditInfo`
        | Updated data for a RUN's SAML Single Sign-On configuration.


===================
createCustomDomain
===================

Create a TagoRUN custom domain for the profile.

    **Parameters:**

            | **profile_id**: str
            | ID of the profile

.. toctree::

    Run_Types


================
getCustomDomain
================

Set details of TagoRun custom domain for the profile.

        **Parameters**

            | **profile_id**: str
            | ID of the profile


===================
deleteCustomDomain
===================

Delete a TagoRUN custom domain for the profile.

        **Parameters**

            | **profile_id**: str
            | ID of the profile


=======================
regenerateCustomDomain
=======================

Regenerate a TagoRUN custom domain for the profile.

        **Parameters**

            | **profile_id**: str
            | ID of the profile
