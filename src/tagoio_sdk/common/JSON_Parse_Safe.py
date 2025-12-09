import json

from typing import Any


def JSONParseSafe(jsonString: str, default: Any = None) -> Any:
    """Safely parse JSON string with fallback to default value"""
    if not jsonString:
        return default

    try:
        return json.loads(jsonString)
    except (json.JSONDecodeError, TypeError, ValueError):
        return default if default is not None else {}
