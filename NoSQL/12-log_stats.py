#!/usr/bin/env python3
"""
NoSQL - log_stats module
"""

from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.logs
collection = db.nginx

logs = collection.count_documents({})
print(f"{logs} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count_methods = {method: collection.count_documents({"method": method})}
print("Methods:")
for method, count in count_methods.items():
    print(f"\tmethod {method}: {count}")

status = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status} status check")

client.close()
