import time

from typing import Any
from typing import Dict
from typing import Optional

from tagoio_sdk.common.Hash_Generator import generateRequestID


# Cache structure: {(request_id, expire_timestamp): cached_object}
cache_obj = {}


def clear_cache_ttl() -> None:
    """
    Clear expired items from the cache
    """
    current_time = int(time.time() * 1000)  # Current time in milliseconds
    expired_keys = []

    for item in cache_obj.keys():
        if item[1] < current_time:
            expired_keys.append(item)

    for key in expired_keys:
        del cache_obj[key]


def add_cache(request_obj: Dict, obj: Any, ttl_ms: int = 5000) -> None:
    """
    Add an object to the cache with specified TTL

    Args:
        request_obj: The request object to generate a key from
        obj: The object to cache
        ttl_ms: Time-to-live in milliseconds (default: 5000)
    """
    clear_cache_ttl()
    key = generateRequestID(request_obj)
    expiration = int(time.time() * 1000) + ttl_ms
    cache_obj[(key, expiration)] = obj


def get_cache(request_obj: Dict) -> Optional[Any]:
    """
    Retrieve an object from the cache if it exists

    Args:
        request_obj: The request object to generate a key from

    Returns:
        The cached object or None if not found
    """
    clear_cache_ttl()
    key = generateRequestID(request_obj)

    for item in list(cache_obj.keys()):
        if item[0] == key:
            return cache_obj[item]

    return None


def clear_cache() -> None:
    """
    Clear all items from the cache
    """
    cache_obj.clear()
