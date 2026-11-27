**Service Authorization Types**
===============================


.. _GenericTokenAuthorization:

GenericToken
------------

    | **GenericToken**: str
    | Token used on TagoIO, string with 34 characters


.. _ServiceAuthorizationCreateInfo:

ServiceAuthorizationCreateInfo(:ref:`CommonTokenData`)
------------------------------------------------------

    **Attributes:**

        | analysis: Optional[:ref:`GenericID`]
        | [Optional] Luau Analysis whose MQTT Endpoint this authorization connects devices to. Set at creation only; it cannot change later. Needs a paid plan (Lite, Pro, or Max; TagoDeploy instances are not gated); on a Free account the request is refused with "The MQTT Endpoint needs a paid plan. Upgrade to use it."


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


.. _ServiceAuthorizationListItem:

ServiceAuthorizationListItem(:ref:`TokenDataList`)
--------------------------------------------------

    **Attributes:**

        | analysis: Optional[:ref:`GenericID`]
        | Luau Analysis the authorization is bound to for the MQTT Endpoint, or None.


.. _ServiceAuthorizationFilter:

ServiceAuthorizationFilter
--------------------------

    **Attributes:**

        | name: str
        | Name to filter service authorizations by.

        | token: :ref:`GenericToken`
        | Token to filter service authorizations by.

        | analysis: :ref:`GenericID`
        | Only the authorizations bound to this Analysis.


.. _ServiceAuthorizationQuery:

ServiceAuthorizationQuery(:ref:`Query`)
---------------------------------------

    **Attributes:**

        | fields: Optional[List["name" or "token" or "verification_code" or "created_at" or "analysis"]]
        | List of fields to include in the query results.

        | filter: Optional[:ref:`ServiceAuthorizationFilter`]
        | Filter criteria for the query.
