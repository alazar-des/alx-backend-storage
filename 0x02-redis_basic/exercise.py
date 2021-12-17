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

    def count_calls(method):
        """ decorator function. """
        def wrapper(self, data):
            """ wrapper function. """
            self._redis.incrby(method.__qualname__, 1)
            method(self, data)
        wrapper.__name__ = method.__name__
        wrapper.__doc__ = method.__doc__
        wrapper.__qualname__ = method.__qualname__
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store input data with random uuid4 key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, **fn):
        """ Reading from Redis and recovering original type. """
        b_val = self._redis.get(key)
        if b_val is not None and fn:
            fn_lst = list(fn.values())
            if fn_lst[0] is not None:
                b_val = fn_lst[0](b_val)
        return b_val

    def get_str(self):
        """ parameterize to string. """
        pass

    def get_int(self):
        """ parameterize to int """
        pass
