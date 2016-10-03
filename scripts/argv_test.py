import sys
from pymongo import MongoClient

name = "test" + sys.argv[1]
print(name)

client = MongoClient()
db = client.campus_crime

test = db[name]

if test.count() > 0 :
	result = test.insert_one(
		{
			"school_id" : 0,
			"school_name" : 0,
			"campus_name" : 0,
			"size" : 0,
			"total_offenses" : 0,
		}
		)
	
else :
	result = test.insert_one(
		{
			"school_id" : 1,
			"school_name" : 2,
			"campus_name" : 4,
			"size" : 5,
			"total_offenses" : 6,
		}
		)