from pymongo import MongoClient
import sys

client = MongoClient()
db = client.campus_crime

campuses = db['campuses']
year = sys.argv[1]

totals_name = "totals" + year
geo_name = "geo_data" + year

totals_data = db[totals_name]
geo_data = db[geo_name]

if geo_data.find({}).count() == 0 :
	geo_data.insert_one(
		{
			"type": "FeatureCollection",
			"features": []
		}
	)

cursor = totals_data.find({})

for record_r in cursor :
	school = record_r['school_name']
	campus = record_r['campus_name']

	cursor_c = campuses.find({ "school_name": school, "campus_name": campus })
	if cursor_c.count() == 0 :
		continue

	record_c = cursor_c[0]

	latitude = float(record_c["lat"])
	longitude = float(record_c["long"])

	#leave out schools that dont have lat/long
	if latitude == 0.0 or longitude == 0.0 :
		continue

	#leave out lat/long outside U.S. bounds (invalid data)
	if (latitude < 17.0 or latitude > 72.0 or longitude < -175.0 or longitude > -55.0) :
		continue

	
	#feature already exists
	if geo_data.find({"properties": {"school_name": school, "campus_name": campus} }).count() > 0 :
		continue

	#feature missing, insert data
	else :
		geo_data.update(
			{ "type" : "FeatureCollection"},
			{ "$push" : { "features" :
				{
					"type": "Feature",
					"geometry": {
	    				"type": "Point",
	    				"coordinates": [ longitude, latitude ]
	  				},
	  				"properties": {
	    				"school_name": school,
	    				"campus_name": campus,
	    				"size": record_r['size'],
	    				"total_offenses": record_r['total_offenses']
	  				}
				}
			}}
		)

