#!/usr/bin/env python3
""" aggregate and sort. """


def top_students(mongo_collection):
    """ calculate average score and sort by their avg score. """
    return mongo_collection.aggregate([
        {"$project": {'name': '$name', 'topics': '$topics',
                      'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}])
