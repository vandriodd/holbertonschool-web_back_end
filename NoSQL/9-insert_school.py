#!/usr/bin/env python3
"""
NoSQL - insert_school module
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
