import json
import pprint
import glob
import os
import copy
#------------------------------
# import csv
 
# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]
 
# myFile = open('example2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)
     
# print("Writing complete")
#----------------------------

def getRoadNames(file):
	with open(file) as j:
		data = json.load(j)
	roads = []
	i=0
	for i in range(len(data)):
		roads.append(data[i]["line"])

	return roads

def loadFile(file):
	with open(file) as j:
		file_data = json.load(j)
	return file_data

def getData(data):
	temp_data = []
	i = 0
	for i in range(len(data)):
		if data[i]['line'] == road:
			
			if direction == "1":
				temp_data = ["date",data[i]["northbound"]["time_updated"]]
				if data[i]["northbound"]["status"] == "light":
					temp_data.append(25)
				elif data[i]["northbound"]["status"] == "mod":
					temp_data.append(50)
				elif data[i]["northbound"]["status"] == "heavy":
					temp_data.append(75)
				temp_data.append(1)
				temp_data.append(100)
			else:
				temp_data = ["date",data[i]["southbound"]["time_updated"]]
				if data[i]["southbound"]["status"] == "light":
					temp_data.append(25)
				elif data[i]["southbound"]["status"] == "mod":
					temp_data.append(50)
				elif data[i]["southbound"]["status"] == "heavy":
					temp_data.append(75)
				temp_data.append(1)
				temp_data.append(100)

	final_data.append(copy.deepcopy(temp_data))


final_data = [["30 Minutes","Lane 1 Flow (Veh/5 Minutes)","# Lane Points,% Observed"]]

# ../mmda-traffic-scrapped/out
# directory = input("Enter directory: ")
file_names = glob.glob("../mmda-traffic-scrapped/out" + "/*.json")

road_names = getRoadNames(file_names[0])
# print(road_names)

print("\nDirection:\n[1] Northbound\n[2] Southbound")
direction = input("choice: ")

road = input("Enter Road Name: ")

if road in road_names:
	print("yes")

for x in range(len(file_names)):
	if os.stat(file_names[x]).st_size != 0: #checks if file is empty
		data = copy.deepcopy(loadFile(file_names[x]))
		getData(data)
		break;
	
print(final_data)