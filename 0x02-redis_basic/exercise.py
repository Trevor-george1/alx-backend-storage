#!/usr/bin/env python3
"""creates a class Cache"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> callable:
    """returns a callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorated function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper



class Cache:

    """defines a class Cache"""
    def __init__(self) -> None:
        """initialize the class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes data and stores in redis"""
        random_key = str(uuid.uuid4())
        self._redis.mset({random_key: data})
        return random_key
    
    def get(self, key: str,
            fn: Optional[callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value
    
    def get_str(self, key: str) -> str:
        """automatically parameters with correct 
        converson function"""
        value = self._redis.get(key)
        return value.decode("utf-8")
    
    def get_int(self, key: str) -> int:
        """conversion function"""
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
