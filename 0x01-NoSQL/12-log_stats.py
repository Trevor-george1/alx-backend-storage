#!/usr/bin/env python3
"""script that provides  stats about Nginx logs stored in MOngoDB"""

import pymongo
from pymongo import MongoClient

def provide_stats(mongo_collection):
    """provide stats about Nginx logs"""
    logs = mongo_collection.estimated_document_count()
    print(f"{logs} logs")


    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    number_of_docs = mongo_collection.count_documents(
        {"method" : "GET", "path": "/status"})
    print(f"{number_of_docs} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    provide_stats(nginx_collection)