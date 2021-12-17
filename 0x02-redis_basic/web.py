#!/usr/bin/env python3
""" count number of url requests. """
import requests
import redis
from functools import wraps


rds = redis.Redis()


def catch(method):
    """decorator function."""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ wrapper function"""
        key = "count:{}".format(args[0])
        if not rds.get(key):
            rds.incr(key)
            rds.expire(key, 10)
        else:
            rds.incr(key)
        return method(*args, **kwargs)
    return wrapper


@catch
def get_page(url: str) -> str:
    """request url and return html content."""
    return requests.get(url)
