import json
import pprint
import glob
import os
import copy
import csv

main_roads = ["EDSA", "ESPAA", "COMMONWEALTH", "C5", "MARCOS HIGHWAY", "SLEX", "ORTIGAS", "ROXAS BLVD.", "QUEZON AVE."]

def roadMenu():
	i=0
	print("\nChoose Main Road:\n")
	for i in range(len(main_roads)):
		print("["+str(i)+"] "+main_roads[i])
	mr_choice = input("Choice: ")
	
	road_list = []
	i=0
	for i in range(len(road_names)):
		if road_names[i][:len(main_roads[int(mr_choice)])] == main_roads[int(mr_choice)]:
			road_list.append(copy.deepcopy(road_names[i]))
	
	i=0
	print("\nChoose Road:")
	for i in range(len(road_list)):
		print("["+str(i)+"] "+road_list[i])
	r_choice = input("Choice: ")

	return road_list[int(r_choice)]

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

def checkStatus(status):
	if status == "light":
		return 25
	elif status == "mod":
		return 50
	elif status == "heavy":
		return 75

def getData(data,file):
	temp_data = []
	i = 0
	for i in range(len(data)):
		if data[i]['line'] == road:
			
			if direction == "1":
				temp_data = [getDate(file)+" "+ getTime(data[i]["northbound"]["time_updated"])]
				temp_data.append(checkStatus(data[i]["northbound"]["status"]))
			else:
				temp_data = [getDate(file)+" "+ getTime(data[i]["southbound"]["time_updated"])]
				temp_data.append(checkStatus(data[i]["southbound"]["status"]))
			
			temp_data.append(1)
			temp_data.append(100)
	
	return temp_data

def getDate(file_name):
	date = file_name[len(directory)+15:len(directory)+15+9]
	year = date[1:5]
	month = date[5:7]
	day = date[7:]
	return (day+"/"+month+"/"+year)
	
def getTime(time):
	if time[len(time)-2:] == 'pm':
		if time[2] == ":":
			return (str(int(time[:2])+12)+time[2:5])
		else:
			return (str(int(time[0])+12)+time[1:4])
	elif time[len(time)-2:] == 'am' and time[:2] == '12':
		return ("00"+time[2:5])
	else:
		return (time[:len(time)-3])


#main()

final_data = [["30 Minutes","Lane 1 Flow (Veh/30 Minutes)","# Lane Points","% Observed"]]
test_data = []
train_data = []

# ../mmda-traffic-scrapped/out
directory = input("Enter directory: ")
file_names = glob.glob(directory + "/*.json")

road_names = getRoadNames(file_names[0])

print("\nDirection:\n[1] Northbound\n[2] Southbound")
direction = input("choice: ")

road = roadMenu()

for x in range(len(file_names)):
	if os.stat(file_names[x]).st_size != 0: #checks if file is empty
		data = copy.deepcopy(loadFile(file_names[x]))
		final_data.append(copy.deepcopy(getData(data,file_names[x])))

train_size = (len(final_data)-1) * 0.8
test_size = (len(final_data)-1) - int(train_size)

print(str(len(final_data))+"\n"+str(train_size)+"\n"+str(test_size))

i = 1
for i in range(int(train_size)+1):
	train_data.append(copy.deepcopy(final_data[i]))
i = int(train_size)+1
for i in range(test_size+1):
	test_data.append(copy.deepcopy(final_data[i]))
		
csv_filename = road.replace(" ","_").lower()
myFile = open('train.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(train_data)
myFile = open('test.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(test_data)
# pprint.pprint(final_data)