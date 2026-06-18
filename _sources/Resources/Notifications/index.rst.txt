**Notifications**
=================

Manage notifications in your application.

=======
list
=======

Retrieves all notifications from the application with optional filtering.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | *Optional* **queryObj**: :ref:`NotificationQuery`
        | Query parameters to filter the results.

    **Returns:**

        | list[:ref:`NotificationInfo`]

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.notifications.list({"filter": {"read": False}, "amount": 10})
        print(result)  # [{'id': 'notification-id-123', 'title': 'System Update', 'message': 'Features', ...}]


==========
markAsRead
==========

Marks one or multiple notifications as read.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | **notificationIDS**: Union[str, list[str]]
        | Notification ID or list of notification IDs

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        # Mark single notification
        resources.notifications.markAsRead("notification-id-123")

        # Mark multiple notifications
        resources.notifications.markAsRead(["id-1", "id-2"])


============
markAsUnread
============

Marks one or multiple notifications as unread.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | **notificationIDS**: Union[str, list[str]]
        | Notification ID or list of notification IDs

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        # Mark single notification
        resources.notifications.markAsUnread("notification-id-123")

        # Mark multiple notifications
        resources.notifications.markAsUnread(["id-1", "id-2"])


=============
markAllAsRead
=============

Marks all notifications in the application as read.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | None

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.notifications.markAllAsRead()
        print(result)  # All TagoIO Notification Run Successfully Updated


==================
notificationButton
==================

Records when a notification button is pressed by the user.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | **notificationID**: str
        | Notification ID

        | **buttonID**: str
        | Button ID

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.notifications.notificationButton("notification-123", "button-456")
        print(result)


======
create
======

Creates a new notification in the system.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | **notificationData**: :ref:`NotificationCreate`
        | Notification data to create

    **Returns:**

        | dict

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.notifications.create({"title": "System Update", "message": "New features available"})
        print(result["id"])  # notification-id-123


======
remove
======

Permanently deletes a notification from the system.

See: `Notification <https://help.tago.io/portal/en/kb/articles/11-notification>`_

    **Parameters:**

        | **notificationID**: str
        | Notification ID

    **Returns:**

        | string

    .. code-block:: python

        from tagoio_sdk import Resources

        resources = Resources()
        result = resources.notifications.remove("notification-123")
        print(result)  # Successfully Removed

.. toctree::


.. toctree::

    Notification_Type
