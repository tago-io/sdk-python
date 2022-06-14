from functools import reduce

from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisEnvironment


def reduceFunction(pv, cv):
    pv[cv.key] = cv.value
    return pv


def envToJson(environment: list[AnalysisEnvironment]) -> AnalysisEnvironment:
    """
    Convert Environment Array to Object

    Note: It will replace duplicate keys for the last one

    :param AnalysisEnvironment environment Array of environment
    items from TagoIO
    """
    return reduce(reduceFunction, environment)
