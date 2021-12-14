#!/usr/bin/env python3
""" provide some stats about Nginx logs stored in MongoDB. """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Display number of logs, method documents and documents with method=Get
    and path=/status. """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(nginx_collection.count_documents({})))

    print("Methods:")
    for method in methods:
        doc_count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, doc_count))

    doc_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(doc_count))
