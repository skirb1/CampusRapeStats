from pymongo import MongoClient
from openpyxl import load_workbook

files = ['Criminal_Offenses_Local_State_Police.xlsx',
			'Criminal_Offenses_Noncampus.xlsx',
			'Criminal_Offenses_On_campus.xlsx',
			'Criminal_Offenses_Public_Property.xlsx']

client = MongoClient()
db = client.campus_crime
campuses = db['campuses']
rape_stats = db['rape_stats2014']
year = 2014;

#clear rape_stats doc
rape_stats.remove({})

for file in files:
	wb = load_workbook(file)
	ws = wb.active

	#total
	for row in ws.iter_rows() :
		if type(row[0].value) is str :
			continue

		#get specific year
		total = int(row[6].value) + int(row[9].value)
		
		if row[0].value == year and total > 0 :
			print(row[2].value)
			campus_id = None

			#for 2014 only
			#rapes = int(row[7].value) + int(row[9].value)

			#add to campuses document
			cursor = db.campuses.find({"school_name" : row[2].value, "campus_name" : row[4].value})
			if cursor.count() == 0 :
				result = db.campuses.insert_one(
					{
						"school_id" : row[1].value,
						"school_name" : row[2].value,
						"campus_name" : row[4].value,
						"lat" : 0,
						"long" : 0,
					}
					)
				campus_id = result.inserted_id;
			elif cursor.count() == 1 :
				campus_id = cursor[0]['_id']

			#add/update rape_statsX document
			cursor = db.rape_stats.find({"school_name" : row[2].value, "campus_name" : row[4].value})
			if cursor.count() == 1 :
				#get previous numbers
				campus_id = cursor[0]['campus_id']

				#add to running total
				result = db.rape_stats.update(
						{ "campus_id" : campus_id },
						{ "$inc" : { "total_offenses" : total} }
					)

			#insert with campus_id corresponding to campus collection
			elif cursor.count() == 0 :
				result = db.rape_stats.insert_one(
					{
						"campus_id" : campus_id,
						"school_id" : row[1].value,
						"school_name" : row[2].value,
						"campus_name" : row[4].value,
						"size" : row[5].value,
						"total_offenses" : total,
					}
					)
				
