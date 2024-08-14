#!/usr/bin/env python3
"""creates a class Cache"""

import redis
import uuid
from typing import Union


class Cache():

    """defines a class Cache"""
    def __init__(self) -> None:
        """initialize the class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes data and stores in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set({random_key: data})
        return random_key
