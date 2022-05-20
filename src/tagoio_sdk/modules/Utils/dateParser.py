from contextlib import suppress
from typing import TypeVar

import dateutil.parser

T = TypeVar("T")


def dateParser(target: T, parameters: list[str]) -> T:
    for parameter in parameters:
        value = target.get(parameter) or None
        if isinstance(value, str):
            parsedDate = None
            with suppress(KeyError):
                parsedDate = dateutil.parser.parse(value, ignoretz=True)

            if parsedDate is not None:
                target[parameter] = parsedDate

    return target


def dateParserList(target: list[T], parameters: list[str]) -> list[T]:
    return list(map(lambda x: dateParser(x, parameters), target))
