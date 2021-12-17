#!/usr/bin/env python3
""" Write strings to Redis """
from typing import Union, Callable
import redis
import uuid
from functools import wraps


class Cache:
    """ Cache class. """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable[[any], any]) -> Callable[[any], any]:
        """ decorator function. """
        @wraps(method)
        def wrapper(self, *args, **kwargs) -> Callable[[any], any]:
            """ wrapper function. """
            self._redis.incr(method.__qualname__)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable[[any], any]):
        """ store input and output of a method. """
        @wraps(method)
        def wraper(self, *args, **kwargs) -> Callable[[any], any]:
            """ wrapper function. """
            in_key = "{}:inputs".format(method.__qualname__)
            self._redis.rpush(in_key, str(args))
            out_key = "{}:outputs".format(method.__qualname__)
            output = method(self, *args, **kwargs)
            self._redis.rpush(out_key, output)
            return output
        return wraper

    @call_history
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
