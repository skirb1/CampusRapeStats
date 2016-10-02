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

	#leave out schools that dont have lat/long
	if record_c['lat'] == 0 or record_c['long'] == 0 :
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
	    				"coordinates": [ float(record_c['long']), float(record_c['lat'])]
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

