
**Run**
========

Manage services in account, be sure to use an account token with “write” permissions when using functions like create, edit and delete.


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

        | **customDomainData**: :ref:`CustomDomainCreate`
        | query params


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
