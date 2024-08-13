#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Returns an empty if no document in the collection"""
    if not mongo_collection:
        return []
    records = mongo_collection.find()
    
    return [docs for docs in records]
