**Profile Type**
=================


.. _ProfileListInfo:

ProfileListInfo
-----------------

TypedDict representing the information of a profile in a list.

    **Properties:**

        | **id**: :ref:`GenericID`
        | The ID of the profile.

        | **name**: str
        | The name of the profile.

        | **logo_url**: str
        | The URL of the profile's logo.


.. _ProfileLimit:

ProfileLimit
-----------------
TypedDict representing the limits of a profile.

    **Properties:**

        | **input**: Union[int, float]
        | The limit for input.

        | **output**: Union[int, float]
        | The limit for output.

        | **sms**: Union[int, float]
        | The limit for SMS.

        | **email**: Union[int, float]
        | The limit for email.

        | **analysis**: Union[int, float]
        | The limit for analysis.

        | **data_records**: Union[int, float]
        | The limit for data records.

        | **run_users**: Union[int, float]
        | The limit for run users.

        | **push_notification**: Union[int, float]
        | The limit for push notifications.

        | **file_storage**: Union[int, float]
        | The limit for file storage.


.. _ProfileAddOns:

ProfileAddOns
-----------------
TypedDict representing the add-ons of a profile.

    **Properties:**

        | **custom_dns**: bool
        | Whether the profile has the Custom Domain add-on purchased.

        | **mobile**: bool
        | Whether the profile has the Custom Mobile App add-on purchased.


.. _info:

info
-----------------
TypedDict representing the information of a profile.

    **Properties:**

        | **id**: :ref:`GenericID`
        | The ID of the profile.

        | **account**: :ref:`GenericID`
        | The ID of the account associated with the profile.

        | **name**: str
        | The name of the profile.

        | **logo_url**: str
        | The URL of the profile's logo.

        | **banner_url**: str
        | The URL of the profile's banner.

        | **created_at**: datetime
        | The datetime when the profile was created.

        | **updated_at**: datetime
        | The datetime when the profile was last updated.


.. _ProfileInfo:

ProfileInfo
-----------------
TypedDict representing the information of a profile.

    **Properties:**

        | **info**: :ref:`info`
        | The information of the profile.

        | **allocation**: :ref:`ProfileLimit`
        | The limits allocation of the profile.

        | **addons**: :ref:`ProfileAddOns`
        | The add-ons of the profile.

        | **account_plan**: str
        | The account plan associated with the profile.


.. _amount:

amount
-----------------
TypedDict representing the amount of resources used by a profile.

    **Properties:**

        | **device**: Union[int, float]
        | The amount of devices used.

        | **bucket**: Union[int, float]
        | The amount of buckets used.

        | **dashboard**: Union[int, float]
        | The amount of dashboards used.

        | **dashboard_shared**: Union[int, float]
        | The amount of shared dashboards used.

        | **analysis**: Union[int, float]
        | The amount of analyses used.

        | **action**: Union[int, float]
        | The amount of actions used.

        | **am**: Union[int, float]
        | The amount of AMs used.

        | **run_users**: Union[int, float]
        | The amount of run users used.

        | **dictionary**: Union[int, float]
        | The amount of dictionaries used.

        | **connectors**: Union[int, float]
        | The amount of connectors used.

        | **networks**: Union[int, float]
        | The amount of networks used.

        | **tcore**: Union[int, float]
        | The amount of Tcore used.


.. _limit_used:

limit_used
-----------------
TypedDict representing the limits used by a profile.

    **Properties:**

        | **input**: Union[int, float]
        | The amount of input used.

        | **output**: Union[int, float]
        | The amount of output used.

        | **analysis**: Union[int, float]
        | The amount of analysis used.

        | **sms**: Union[int, float]
        | The amount of SMS used.

        | **email**: Union[int, float]
        | The amount of email used.

        | **data_records**: Union[int, float]
        | The amount of data records used.

        | **run_users**: Union[int, float]
        | The amount of run users used.

        | **push_notification**: Union[int, float]
        | The amount of push notifications used.

        | **file_storage**: Union[int, float]
        | The amount of file storage used.

        | **tcore**: Union[int, float]
        | The amount of Tcore used.


.. _ProfileSummary:

ProfileSummary
-----------------
TypedDict representing the summary of a profile.

    **Properties:**

        | **limit**: :ref:`ProfileLimit`
        | The limits of the profile.

        | **amount**: :ref:`amount`
        | The amount of resources used by the profile.

        | **limit_used**: :ref:`limit_used`
        | The limits used by the profile.

        | **addons**: :ref:`ProfileAddOns`
        | The add-ons of the profile.
