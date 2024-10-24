#!/usr/bin/env python3

"""
Python function that inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ inserting """
    return mongo_collection.insert(kwargs)
