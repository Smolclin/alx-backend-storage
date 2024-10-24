#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    no_logs = nginx_collection.count_documents({})
    print(f'{no_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')
