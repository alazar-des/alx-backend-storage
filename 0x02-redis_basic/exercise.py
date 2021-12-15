#!/usr/bin/env python3
""" Write strings to Redis """
from typing import Union, Callable
import redis
import uuid
import wrapt


class Cache:
    """ Cache class. """
    def __init__(self):
        self.___redis = redis.Redis()
        self.___redis.flushdb()

    def count_calls(method):
        """ decorator function. """
        def wrapper(self, data: Union[str, bytes, int, float]) -> str:
            """ wrapper function. """
            self.___redis.incrby(method.__qualname__, 1)
            method(self, data)
        wrapper.__name__ = method.__name__
        wrapper.__doc__ = method.__doc__
        wrapper.__qualname__ = method.__qualname__
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store input data with random uuid4 key. """
        key = str(uuid.uuid4())
        self.___redis.set(key, data)
        return key

    def get(self, key: str, **fn: Callable[[bytes], any]) -> any:
        """ reading from redis and recovering original type. """
        rtn = self.___redis.get(key)
        if fn is not None:
            fn_lst = list(fn.values())
            if fn_lst and fn_lst[0] is not None:
                rtn = fn_lst[0](rtn)
        return rtn

    def get_str(self, rtn: Union[str, bytes, int, float]) -> str:
        """ string parameterize. """
        return str(rtn)
