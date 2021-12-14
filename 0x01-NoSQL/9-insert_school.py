#!/usr/bin/env python3
""" insert to a collection """


def insert_school(mongo_collection, **kwargs):
    """ insert to kwargs to mongo_collection. """
    _id = mongo_collection.insert_one(kwargs)
    return _id.inserted_id
