from pymongo import MongoClient

client = MongoClient()
db = client.campus_crime

#first convert all lat/long to floats
cursor = db.campuses.find({})
for doc in cursor :
	doc["lat"] = float(doc["lat"])
	doc["long"] = float(doc["long"])

#cursor = db.campuses.find({"latitude":{$lt:16.0}})
#or {"latitude":{$gt:72.0}} or {"longitude":{$lt:-175.0}} or {"longitude":{$gt:-55.0}}

db.campuses.find().forEach( function(data) { 
	db.campuses.update({
        "_id": data._id,
    }, {
        "$set": {
            "lat": parseFloat(data.lat),
            "long": parseFloat(data.long)
        }
    });
	});