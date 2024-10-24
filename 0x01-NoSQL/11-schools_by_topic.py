#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ returning lists """
    list_school = mongo_collection.find({"topics": topic})
    return list(list_school)
