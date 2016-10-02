import urllib.request
import json
API_KEY = "AIzaSyAD6sagyNTYf7vfUgi4P5g1LXZgXmNO0UU"


import re


fo = open("campusLatLong.txt", "w")
with open('notfound.txt') as input_file:
	for i, line in enumerate(input_file):
		line = re.sub('[\n]', '', line)
		camName = line
		line = re.sub('[^0-9a-zA-Z]', '+', line)
		latitude = 0
		longitude = 0

		response = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + line + "&key=" + API_KEY)
		response_str = response.read().decode('utf-8')
		info = json.loads(response_str)
		if (not info["results"]):
			latitude = 0
			longitude = 0
		else: 
			latitude = info["results"][0]["geometry"]["location"]["lat"]
			longitude = info["results"][0]["geometry"]["location"]["lng"]
				

		fo.write(camName)
		fo.write(",")
		fo.write(str(latitude))
		fo.write(",")
		fo.write(str(longitude))
		fo.write("\n")
		print(line)

print ("{0} line(s) printed".format(i+1))
fo.close()