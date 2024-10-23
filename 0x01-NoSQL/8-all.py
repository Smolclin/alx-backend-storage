#!/usr/bin/env python3

""" 
Python function that lists documents
"""

def list_all(mongo_collection):
    """ lists python documents """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return[]

     return documents
