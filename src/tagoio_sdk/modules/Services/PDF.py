from typing import Optional, TypedDict, Union

import requests

from tagoio_sdk.common.tagoio_module import TagoIOModule


class PDFResult(TypedDict):
    status: bool
    result: str


class margin(TypedDict):
    top: Optional[Union[str, int, float]]
    """
    Top margin, accepts values labeled with units. Defaults to `0`.
    """

    right: Optional[Union[str, int, float]]
    """
    Right margin, accepts values labeled with units. Defaults to `0`.
    """

    bottom: Optional[Union[str, int, float]]
    """
    Bottom margin, accepts values labeled with units. Defaults to `0`.
    """

    left: Optional[Union[str, int, float]]
    """
    Left margin, accepts values labeled with units. Defaults to `0`.
    """


class options(TypedDict):
    """
    PDF Custom Options
    """

    displayHeaderFooter: Optional[bool]
    """
    Display header and footer. Defaults to `false`.
    """
    footerTemplate: Optional[str]
    """
    HTML template for the print footer. Should use the same format as the `headerTemplate`.
    """
    format: Optional[str]
    """
    Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'.
    """
    headerTemplate: Optional[str]
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
    height: Optional[Union[str, int, float]]
    """
    Paper height, accepts values labeled with units.
    """
    landscape: Optional[bool]
    """
    Paper orientation. Defaults to `false`.
    """
    margin: Optional[margin]
    """
    Paper margins, defaults to none.
    """
    pageRanges: Optional[str]
    """
    Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print
    all pages.
    """
    preferCSSPageSize: Optional[bool]
    """
    Give any CSS `@page` size declared in the page priority over what is
    declared in `width` and `height` or `format`options.
    Defaults to `false`, which will scale the content to fit the paper size.
    """
    printBackground: Optional[bool]
    """
    Print background graphics. Defaults to `false`.
    """
    scale: Optional[Union[int, float]]
    """
    Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2.
    """
    width: Optional[Union[str, int, float]]
    """
    Paper width, accepts values labeled with units.
    """


class PDFParams(TypedDict):
    html: Optional[str]
    """
    HTML as string
    """
    base64: Optional[str]
    """
    HTML on base64 format
    """
    fileName: Optional[str]
    """
    File name of pdf
    Without filename, it will generate base64 response
    With filename it will generate pdf binary
    """
    url: Optional[str]
    """
    Generate pdf from URL
    """
    options: Optional[options]
    """
    PDF Custom Options
    """


class PDFService(TagoIOModule):
    def generate(self, params: PDFParams) -> PDFResult:
        """
        Generate a PDF from html, url or base64
        """
        result = requests.post(
            "https://pdf.middleware.tago.io",
            json=params,
            headers={"token": self.token},
        )
        return result
