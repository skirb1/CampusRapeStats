import json

with open('geo2014.json') as json_data:
	data = json.load(json_data)
	for element in data :
		del element["_id"]