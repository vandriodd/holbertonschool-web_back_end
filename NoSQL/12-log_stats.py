#!/usr/bin/env python3
"""
NoSQL - log_stats module
"""

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})
# methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


client.close()

print(f"{total_logs} logs")
print("Methods:")
# print()
