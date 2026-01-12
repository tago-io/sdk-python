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


.. _UsageStatistic:

UsageStatistic
-----------------
TypedDict representing a single usage statistic with timestamp.

Not all of the services will be present for every statistic, only if for the usage period the service was used.

    **Properties:**

        | **time**: datetime
        | Timestamp for the usage statistic.

        | **input**: Union[int, float]
        | Input data usage.

        | **output**: Union[int, float]
        | Output data usage.

        | **analysis**: Union[int, float]
        | Analysis execution time used.

        | **sms**: Union[int, float]
        | SMS messages sent.

        | **email**: Union[int, float]
        | Email messages sent.

        | **data_records**: Union[int, float]
        | Data records stored.

        | **run_users**: Union[int, float]
        | Run users used.

        | **push_notification**: Union[int, float]
        | Push notifications sent.

        | **file_storage**: Union[int, float]
        | File storage used.

        | **tcore**: Union[int, float]
        | TCore resources used.


.. _AuditLogEvent:

AuditLogEvent
-----------------
TypedDict representing a single audit log event.

    **Properties:**

        | **resourceName**: str
        | Name of the resource that triggered the event.

        | **message**: str
        | Descriptive message about the event.

        | **resourceID**: :ref:`GenericID`
        | ID of the resource that triggered the event.

        | **who**: :ref:`GenericID`
        | ID of the account that performed the action.

        | **date**: datetime
        | Timestamp when the event occurred.


.. _AuditLogStatistics:

AuditLogStatistics
------------------
TypedDict representing statistics for an audit log query.

    **Properties:**

        | **recordsMatched**: int
        | Number of records that matched the query.

        | **recordsScanned**: int
        | Number of records scanned during the query.

        | **bytesScanned**: int
        | Number of bytes scanned during the query.


.. _AuditLog:

AuditLog
-----------------
TypedDict representing an audit log query result.

    **Properties:**

        | **events**: list[:ref:`AuditLogEvent`]
        | List of audit log events.

        | **statistics**: :ref:`AuditLogStatistics`
        | Statistics about the query execution.

        | **status**: Literal["Running", "Complete", "Failed", "Timeout", "Unknown"]
        | Current status of the audit log query.

        | **queryId**: str
        | Unique identifier for the audit log query.


.. _AuditLogFilter:

AuditLogFilter
-----------------
TypedDict representing filters for audit log queries.

    **Properties:**

        | **resourceID**: :ref:`GenericID`
        | Filter by specific resource ID.

        | **resourceName**: Literal["action", "am", "analysis", "connector", "dashboard", "device", "dictionary", "network", "profile", "run", "runuser"]
        | Filter by resource type.

        | **find**: str
        | Search string for filtering events.

        | **start_date**: Union[str, datetime]
        | Start date for the query range.

        | **end_date**: Union[str, datetime]
        | End date for the query range.

        | **limit**: int
        | Maximum number of results to return.


.. _AddonInfo:

AddonInfo
-----------------
TypedDict representing profile addon information.

    **Properties:**

        | **id**: :ref:`GenericID`
        | The addon ID.

        | **name**: str
        | The addon name.

        | **logo_url**: Optional[str]
        | URL of the addon's logo.


.. _StatisticsDate:

StatisticsDate
-----------------
TypedDict representing parameters for fetching usage statistics.

    **Properties:**

        | **timezone**: str
        | Timezone to be used in the statistics entries (default: "UTC").

        | **date**: Union[str, datetime]
        | Timestamp for fetching hourly statistics in a day.

        | **start_date**: Union[str, datetime]
        | Starting date for fetching statistics in an interval.

        | **end_date**: Union[str, datetime]
        | End date for fetching statistics in an interval.

        | **periodicity**: Literal["hour", "day", "month"]
        | Periodicity of the statistics to fetch (default: "hour").


.. _ProfileTeam:

ProfileTeam
-----------------
TypedDict representing a team member with access to a profile.

    **Properties:**

        | **active**: bool
        | Whether the team member's access is active.

        | **created_at**: datetime
        | When the team member was added.

        | **email**: str
        | Email address of the team member.

        | **id**: str
        | Account ID of the team member.

        | **name**: str
        | Name of the team member.


.. _ProfileCreateInfo:

ProfileCreateInfo
-----------------
TypedDict representing the information needed to create a new profile.

    **Properties:**

        | **name**: str
        | Name of the profile to be created.


.. _ProfileCredentials:

ProfileCredentials
------------------
TypedDict representing credentials required for sensitive profile operations.

    **Properties:**

        | **password**: str
        | Account password.

        | **pin_code**: str
        | Two-factor authentication PIN code (required when 2FA is enabled).
