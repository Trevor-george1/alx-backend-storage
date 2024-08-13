#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """returns the new id """
    new_record = mongo_collection.insert_one(kwargs)
    return new_record.inserted_id
