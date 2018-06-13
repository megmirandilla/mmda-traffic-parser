import json
import pprint
import glob

# import csv
 
# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]
 
# myFile = open('example2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)
     
# print("Writing complete")

# ../mmda-traffic-scrapped/out
directory = input("Enter directory: ")
file_names = glob.glob(directory + "/*.json")

# print("\nDirection:\n[1] Northbound\n[2] Southbound")
# direction = input("choice: ")

# road = input("Enter Road Name: ")

# with open(file_names[0]) as j:
# 	data = json.load(j)

# pprint.pprint(data)
