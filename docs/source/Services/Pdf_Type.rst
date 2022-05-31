**Notification Type**
===============

.. _margin:

margin
------

    **Attributes:**

        | **top**: str or int or float
        | Top margin, accepts values labeled with units. Defaults to `0`.


        | **right**: str or int or float
        | Right margin, accepts values labeled with units. Defaults to `0`.

        | **bottom**: str or int or float
        | Bottom margin, accepts values labeled with units. Defaults to `0`.

        | **left**: str or int or float
        | Left margin, accepts values labeled with units. Defaults to `0`.


.. _options:

options
-------

    **Attributes:**

        | **displayHeaderFooter**: bool
        | Display header and footer. Defaults to `false`.

        | **footerTemplate**: str
        | HTML template for the print footer. Should use the same format as the `headerTemplate`.

        | **format**: str
        | Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.

        | **headerTemplate**: str
        | HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values
        | into them:
        | - `'date'` formatted print date
        | - `'title'` document title
        | - `'url'` document location
        | - `'pageNumber'` current page number
        | - `'totalPages'` total pages in the document

        | **height**: str or int or float
        | Paper height, accepts values labeled with units.

        | **landscape**: bool
        | Paper orientation. Defaults to `false`.

        | **margin**: :ref:`margin`
        | Paper margins, defaults to none.

        | **pageRanges**: str
        | Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.

        | **preferCSSPageSize**: bool
        | Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format`options. Defaults to `false`, which will scale the content to fit the paper size.

        | **printBackground**: bool
        | Print background graphics. Defaults to `false`.

        | **scale**: int or float
        | Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.

        | **width**: str or int or float
        | Paper width, accepts values labeled with units.


.. _PDFParams:

PDFParams
---------

    **Attributes:**

        | **html**: str
        | HTML as string

        | **base64**: str
        | HTML on base64 format

        | **fileName**: str
        | File name of pdf. Without filename, it will generate base64 response With filename it will generate pdf binary

        | **url**: str
        | Generate pdf from URL

        | **options**: :ref:`options`
        | PDF Custom Options

