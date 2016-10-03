import sys
from pymongo import MongoClient

print(sys.argv[1])

name = "totals" + sys.argv[1]
print(name)

year = sys.argv[1]
client = MongoClient()
db = client.campus_crime

collection_name = "totals" + year;
rape_stats = db[collection_name]

result = db.rape_stats.insert_one(
	{
		"school_id" : 1,
		"school_name" : 2,
		"campus_name" : 4,
		"size" : 5,
		"total_offenses" : 6,
	}
	)