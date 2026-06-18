**PDF Type**
============

.. _margin:

margin
------

    **Attributes:**

        | **top**: Optional[str or int or float]
        | [Optional] Top margin, accepts values labeled with units. Defaults to `0`.


        | **right**: Optional[str or int or float]
        | Right margin, accepts values labeled with units. Defaults to `0`.

        | **bottom**: Optional[str or int or float]
        | [Optional] Bottom margin, accepts values labeled with units. Defaults to `0`.

        | **left**: Optional[str or int or float]
        | [Optional] Left margin, accepts values labeled with units. Defaults to `0`.


.. _pdf_options:

options
-------

    **Attributes:**

        | **displayHeaderFooter**: Optional[bool]
        | [Optional] Display header and footer. Defaults to `false`.

        | **footerTemplate**: Optional[str]
        | [Optional] HTML template for the print footer. Should use the same format as the `headerTemplate`.

        | **format**: Optional[str]
        | [Optional] Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.

        | **headerTemplate**: Optional[str]
        | [Optional] HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values
        | into them:
        | - `'date'` formatted print date
        | - `'title'` document title
        | - `'url'` document location
        | - `'pageNumber'` current page number
        | - `'totalPages'` total pages in the document

        | **height**: Optional[str or int or float]
        | [Optional] Paper height, accepts values labeled with units.

        | **landscape**: Optional[bool]
        | [Optional] Paper orientation. Defaults to `false`.

        | **margin**: Optional[:ref:`margin`]
        | [Optional] Paper margins, defaults to none.

        | **pageRanges**: Optional[str]
        | [Optional] Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages.

        | **preferCSSPageSize**: Optional[bool]
        | [Optional] Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format`options. Defaults to `false`, which will scale the content to fit the paper size.

        | **printBackground**: Optional[bool]
        | [Optional] Print background graphics. Defaults to `false`.

        | **scale**: Optional[int or float]
        | [Optional] Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.

        | **width**: Optional[str or int or float]
        | [Optional] Paper width, accepts values labeled with units.


.. _PDFParams:

PDFParams
---------

    **Attributes:**

        | **html**: Optional[str]
        | [Optional] HTML as string

        | **base64**: Optional[str]
        | [Optional] HTML on base64 format

        | **fileName**: Optional[str]
        | [Optional] File name of pdf. Without filename, it will generate base64 response With filename it will generate pdf binary

        | **url**: Optional[str]
        | [Optional] Generate pdf from URL

        | **options**: Optional[:ref:`pdf_options`]
        | [Optional] PDF Custom Options

