from pymongo import MongoClient
import sys

client = MongoClient()
db = client.campus_crime

name = sys.argv[1]
collection = db[name]

collection.drop()