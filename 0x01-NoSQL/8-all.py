#!/usr/bin/env python3
""" pymongo """


def list_all(mongo_collection):
    """ return all documents. """
    return mongo_collection.find()
