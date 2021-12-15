#!/usr/bin/env python3
""" Write strings to Redis """
from typing import Union, Callable
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

    def get(self, key: str, **fn: Callable[[bytes], any]) -> any:
        """ reading from redis and recovering original type. """
        rtn = self.___redis.get(key)
        if fn is not None:
            fn_lst = list(fn.values())
            if fn_lst[0] is not None:
                rtn = fn_lst[0](rtn)
        return rtn

    def get_str(self, rtn: Union[str, bytes, int, float]) -> str:
        """ string parameterize. """
        return str(rtn)

    def get_int(self, rtn: Union[str, bytes, int, float]) -> int:
        """ int parameterize. """
        return int(rtn)
