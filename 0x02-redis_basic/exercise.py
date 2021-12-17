#!/usr/bin/env python3
""" Write strings to Redis """
from typing import Union, Callable
import redis
import uuid


class Cache:
    """ Cache class. """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store input data with random uuid4 key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
