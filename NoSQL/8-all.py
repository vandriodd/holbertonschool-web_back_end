#!/usr/bin/env python3
"""
NoSQL - all module
"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = mongo_collection.find()
    return documents
