#!/usr/bin/env python3
""" update all """


def update_topics(mongo_collection, name, topics):
    """ update name with topics. """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
