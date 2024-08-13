#!/usr/bin/env python3
""" function that changes all topics of a school document based on the name:"""


def update_topics(mongo_collection, name, topics):
    """updates a coolection"""
    new_value = {'$set': {"topics": topics}}
    return mongo_collection.update_many({"name" : name}, new_value)
