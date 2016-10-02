from pymongo import MongoClient
from openpxl import Workbook

files = ['Criminal_Offenses_Local_State_Police.xlsx']
			#'Criminal_Offenses_Noncampus/xlsx',
			#'Criminal_Offenses_On_campus.xlsx',
			#'Criminal_Offenses_Public_Property.xlsx']

client = MongoClient()
db = client.campus_crime
campuses = db['campuses']
rape_stats = db['rape_stats']

for file in files:
	wb = load_workbook(file)
	ws = wb.active

	#total
	for row in ws.iter_rows(min_row=2) :
		if(row['A'] == 2014) :
			print(row['B'])

