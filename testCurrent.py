import os
import json

directories = ["111", "112"]

for congress in directories:
	fw = open(congress+"_house_bills.txt","r")
	line = fw.readline()
	while line:
		jsonDump = json.loads(line)
		if jsonDump["current_status"].find(",")!=-1:
			print jsonDump["current_status"],jsonDump["congress"],jsonDump["bill_type"],jsonDump["number"]
		line = fw.readline()
