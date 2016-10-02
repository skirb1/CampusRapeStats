from pymongo import MongoClient
import csv

client = MongoClient()
db = client.campus_crime
campuses = db['campuses']

with open("campusLatLong.csv") as csvfile :
	myreader = csv.reader(csvfile, delimiter=",")
	for row in myreader:

		cursor = db.campuses.find({"school_name" : row[0], "campus_name" : row[1]})
		if cursor.count() > 0:
			result = db.campuses.update(
				{"school_name" : row[0], "campus_name" : row[1]},
				{ "$set" : {"lat": row[2], "long":row[3]} }

			)
