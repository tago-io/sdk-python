.. _Run:

**Run**
========

Manage services in account, be sure to use an account token with “write” permissions when using functions like create, edit and delete.

.. _ssoSAMLInfo:

============
ssoSAMLInfo
============

Get the SAML Single Sign-On information for the account's RUN.

.. _ssoSAMLEdit:

============
ssoSAMLEdit
============

Edit the SAML Single Sign-On metadata and mappings for the account's RUN.

    **Parameters:**

        | **data**: :ref:`RunSAMLEditInfo`
        | Updated data for a RUN's SAML Single Sign-On configuration.

.. _createCustomDomain: 

===================
createCustomDomain
===================

Create a TagoRUN custom domain for the profile.

    **Parameters:**

        | **profile_id**: str
        | ID of the profile

        | **customDomainData**: :ref:`CustomDomainCreate`
        | query params

.. _getCustomDomain:

================
getCustomDomain
================

Set details of TagoRun custom domain for the profile.

        **Parameters**
        
            | **profile_id**: str
            | ID of the profile

.. _deleteCustomDomain:

===================
deleteCustomDomain
===================

Delete a TagoRUN custom domain for the profile.

        **Parameters**

            | **profile_id**: str
            | ID of the profile

.. _regenerateCustomDomain:

=======================
regenerateCustomDomain
=======================

Regenerate a TagoRUN custom domain for the profile.

        **Parameters**

            | **profile_id**: str
            | ID of the profile
