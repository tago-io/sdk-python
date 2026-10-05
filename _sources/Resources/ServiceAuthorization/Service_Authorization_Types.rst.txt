**Service Authorization Types**
===============================


.. _GenericTokenAuthorization:

GenericToken
------------

    | **GenericToken**: str
    | Token used on TagoIO, string with 34 characters


.. _TokenCreateResponseAuthorization:

TokenCreateResponse
-------------------

    **Attributes:**

        | token: :ref:`GenericTokenAuthorization`
        | The authorization token.

        | name: str
        | Name of the token.

        | profile: :ref:`GenericID`
        | Profile ID associated with the token.

        | additional_parameters: Optional[str]
        | [Optional] Verification code to validate middleware requests.


.. _ServiceAuthorizationFilter:

ServiceAuthorizationFilter
--------------------------

    **Attributes:**

        | name: str
        | Name to filter service authorizations by.

        | token: :ref:`GenericToken`
        | Token to filter service authorizations by.


.. _ServiceAuthorizationQuery:

ServiceAuthorizationQuery(:ref:`Query`)
---------------------------------------

    **Attributes:**

        | fields: Optional[List["name" or "token" or "verification_code" or "created_at"]]
        | List of fields to include in the query results.

        | filter: Optional[:ref:`ServiceAuthorizationFilter`]
        | Filter criteria for the query.
