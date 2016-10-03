from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime

print(db.collection_names())
print("posts" in db.collection_names()) 
