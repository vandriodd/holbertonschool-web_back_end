#!/usr/bin/env python3
"""
NoSQL - schools_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """Function that returns the list of school having a specific topic"""
    schools = mongo_collection.find({"topic": topic})
    return schools
