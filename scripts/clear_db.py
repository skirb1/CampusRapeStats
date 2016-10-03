from pymongo import MongoClient
python sys

client = MongoClient()
db = client.campus_crime

name = "rape_stats" + sys.argv[1]
rape_stats = db[name]

db.rape_stats.drop()