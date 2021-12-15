#!/usr/bin/env python3
""" Write strings to Redis """
from typing import Union
import redis
import uuid


class Cache:
    """ Cache class. """
    def __init__(self):
        self.___redis = redis.Redis()
        self.___redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store input data with random uuid4 key. """
        key = str(uuid.uuid4())
        self.___redis.set(key, data)
        return key
