**Email Type**
===============

.. _AttachmentOptions:

AttachmentOptions
-----------------

    **Attributes:**

        | **archive**: str
        | Archive itself

        | **filename**: str
        | Name for the archive


.. _TemplateOptions:

TemplateOptions
---------------

    **Attributes:**

        | **name**: str
        | Template name
        | You can create an e-mail template on TagoRUN options at https://admin.tago.io/run

        | **params**: Optional[dict[str, Union[int, float]]]
        | [Optional] Parameters to parse on Template
        | You can use that parameter as local variable using $PARAMETER_KEY$  example params = { name: 'John' } will be $name$ on template document

.. _EmailBase:

EmailBase
----------

    **Attributes:**

        | **to**: str
        | E-mail address to be sent
        | example: "myclien@tago.io"

        | **from_name**: Optional[str]
        | [Optional] Name of origin
        | example: "My Run"

        | **subject**: str
        | Subject of the e-mail only allow with message or html

        | **attachment**: Optional[:ref:`AttachmentOptions`]
        | [Optional] Attachment for the e-mail



.. _EmailRawText:

EmailRawText
------------

    **Attributes:**

        | **message**: str
        | Message in raw text for email body



.. _EmailHTML:

EmailHTML
---------

    **Attributes:**

        | **html**: str
        | HTML email body


.. _EmailWithTemplate:

EmailWithTemplate
-----------------

    **Attributes:**

        | **to**: str
        | E-mail address to be sent
        | example: "myclien@tago.io"

        | **from_name**: Optional[str]
        | [Optional] Name of origin
        | example: "My Run"

        | **attachment**: Optional[:ref:`AttachmentOptions`]
        | [Optional] Attachment for the e-mail

        | **template**: Optional[:ref:`TemplateOptions`]
        | [Optional] Use TagoRUN E-Mail Template
        | If you use template together with attachment the back-end will generate a parameter called 'URL'


.. _EmailWithHTML:

EmailWithHTML
-----------------

    EmailWithHTML: :ref:`EmailBase` or :ref:`EmailHTML`

.. _EmailWithRawText:

EmailWithRawText
-----------------

    EmailWithRawText = :ref:`EmailBase` or :ref:`EmailRawText`
