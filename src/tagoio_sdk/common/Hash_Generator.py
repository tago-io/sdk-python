import json

from typing import Any
from typing import Dict


def hash_generator(obj: Any) -> int:
    """
    Generate a hash from any object by converting it to JSON string

    Args:
        obj: Any object that can be serialized to JSON

    Returns:
        A 32-bit integer hash
    """
    obj_string = json.dumps(obj, sort_keys=True)

    hash_value = 0

    if len(obj_string) == 0:
        return hash_value

    for i in range(len(obj_string)):
        char = ord(obj_string[i])
        hash_value = ((hash_value << 5) - hash_value) + char
        hash_value = hash_value & 0xFFFFFFFF  # Convert to 32bit integer

    return hash_value


def generateRequestID(request_obj: Dict) -> int:
    """
    Generate a unique ID for a request object

    Args:
        request_obj: A dictionary containing request information

    Returns:
        A unique request ID as integer
    """
    obj_key = {
        "url": request_obj.get("url"),
        "token": request_obj.get("headers", {}).get("token"),
        "params": request_obj.get("params"),
        "body": request_obj.get("data") or request_obj.get("body"),
        "method": request_obj.get("method"),
    }

    request_id = hash_generator(obj_key)

    return request_id
