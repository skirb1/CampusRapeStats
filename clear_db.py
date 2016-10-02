from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime

#clear rape_stats doc
result = db.rape_stats.delete_many({})
print(result.deleted_count)

result = db.campuses.delete_many({})
print(result.deleted_count)

db.rape_stats.drop()