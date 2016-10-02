from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime

db.geo_data2014.drop()