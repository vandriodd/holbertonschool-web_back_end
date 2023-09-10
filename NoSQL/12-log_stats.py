#!/usr/bin/env python3
"""
NoSQL - log_stats module
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx

    logs = collection.count_documents({})
    print(f"{logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_methods = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_methods}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    client.close()
