import json
import pprint
import os
# with open('jhernandez-traffic-status-20180531140300.json') as j:
# 	data = json.load(j)

# pprint.pprint(data)

directory = input("Enter directory: ")

file_names = os.listdir(directory)