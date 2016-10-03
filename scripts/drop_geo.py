from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime

db.geo_data2013.drop()
db.geo_data2012.drop()
db.geo_data2011.drop()
