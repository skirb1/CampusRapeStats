from geopy.geocoders import Nominatim
from pymongo import MongoClient
import pymongo

file = open("notfound.txt", "w")

client = MongoClient()
db = client.campus_crime

geolocator = Nominatim()

#iterate through campuses
cursor = db.campuses.find({ "lat": 0, "long": 0}).sort('total_offenses',pymongo.DESCENDING)

for record in cursor :
	school = record["school_name"]
	campus = record["campus_name"]

	'''
	full_name = school + " " + campus
	location = geolocator.geocode(full_name, exactly_one = True)
	if(location != None) :
		print(full_name)
		
		result = db.campuses.update(
			{"school_name" : school, "campus_name": campus},
			{"$set" : { "lat" : location.latitude, "long" : location.longitude }}
			)

	else :
	'''
	file.write(school + "," + campus + "\n")


file.close()