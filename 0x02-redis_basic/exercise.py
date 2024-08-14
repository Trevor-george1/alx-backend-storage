#!/usr/bin/env python3
"""creates a class Cache"""

import redis
import uuid


class Cache():

    """defines a class Cache"""
    def __init__(self) -> None:
        """initialize the class cache"""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: any) -> str:
        """store method that takes data and stores in redis"""
        random_key = str(uuid.uuid4())
        self._redis.mset({random_key: data})
        return random_key
