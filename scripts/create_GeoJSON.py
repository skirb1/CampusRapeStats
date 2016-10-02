from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime
campuses = db['campuses']

rape_stats = db['rape_stats2014']
geo_data = db['geo_data2014']

if geo_data.find({}).count() == 0 :
	geo_data.insert_one(
		{
			"type": "FeatureCollection",
			"features": []
		}
	)

cursor = db.rape_stats.find({})

for record_r in cursor :
	cursor_c = campuses.find({ "_id": record_r['campus_id'] })
	record_c = cursor_c[0]

	latitude = float(record_c["lat"])
	longitude = float(record_c["long"])

	#leave out schools that dont have lat/long
	if latitude == 0.0 or longitude == 0.0 :
		continue

	#leave out lat/long outside U.S. bounds (invalid data)
	if (latitude < 10.0 or latitude > 72.0 or longitude < -175.0 or longitude > -55.0) :
		continue

	school = record_c['school_name']
	campus = record_c['campus_name']

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

