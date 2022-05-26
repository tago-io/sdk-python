from typing import TypedDict, Union

import requests

from tagoio_sdk.common.tagoio_module import TagoIOModule


class margin(TypedDict):
    top: Union[str, int, float]
    """
    Top margin, accepts values labeled with units. Defaults to `0`.
    """

    right: Union[str, int, float]
    """
    Right margin, accepts values labeled with units. Defaults to `0`.
    """

    bottom: Union[str, int, float]
    """
    Bottom margin, accepts values labeled with units. Defaults to `0`.
    """

    left: Union[str, int, float]
    """
    Left margin, accepts values labeled with units. Defaults to `0`.
    """


class options(TypedDict):
    """
    PDF Custom Options
    """

    displayHeaderFooter: bool
    """
    Display header and footer. Defaults to `false`.
    """
    footerTemplate: str
    """
    HTML template for the print footer. Should use the same format as the `headerTemplate`.
    """
    format: str
    """
    Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.
    """
    headerTemplate: str
    """
    HTML template for the print header. Should be valid HTML markup with following classes used
    to inject printing values

    into them:
    - `'date'` formatted print date
    - `'title'` document title
    - `'url'` document location
    - `'pageNumber'` current page number
    - `'totalPages'` total pages in the document
    """
    height: Union[str, int, float]
    """
    Paper height, accepts values labeled with units.
    """
    landscape: bool
    """
    Paper orientation. Defaults to `false`.
    """
    margin: margin
    """
    Paper margins, defaults to none.
    """
    pageRanges: str
    """
    Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print
    all pages.
    """
    preferCSSPageSize: bool
    """
    Give any CSS `@page` size declared in the page priority over what is
    declared in `width` and `height` or `format`options.
    Defaults to `false`, which will scale the content to fit the paper size.
    """
    printBackground: bool
    """
    Print background graphics. Defaults to `false`.
    """
    scale: Union[int, float]
    """
    Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.
    """
    width: Union[str, int, float]
    """
    Paper width, accepts values labeled with units.
    """


class PDFParams(TypedDict):
    html: str
    """
    HTML as string
    """
    base64: str
    """
    HTML on base64 format
    """
    fileName: str
    """
    File name of pdf
    Without filename, it will generate base64 response
    With filename it will generate pdf binary
    """
    url: str
    """
    Generate pdf from URL
    """
    options: options
    """
    PDF Custom Options
    """


class PDFService(TagoIOModule):
    def generate(self, params: PDFParams) -> str:
        """
        Generate a PDF from html, url or base64
        """
        result = requests.post(
            "https://pdf.middleware.tago.io",
            data=params,
            headers={"token": self.params.token},
        )
        return result
