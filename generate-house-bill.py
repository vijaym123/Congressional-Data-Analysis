import os
import json

directories = ["111","112","113"]
fw = open("cosponsorship2013/house_bills.txt","w")

billType = {}
billType["hconres"] = "HC"
billType["hjres"] = "HJ"
billType["hr"] = "HR"
billType["hres"] = "HE"
for congress in directories:
	for root, subFolders, files in os.walk(congress):
		if files:
			fr = open("./"+root+"/"+files[0],"r")
			jsonDump = json.loads(fr.read())
			try :
				if jsonDump["bill_type"] not in billType.keys():
					break
				elif jsonDump["subjects_top_term"].find("Private")>=0:
					private = str(1)
				else :
					private = str(0)
			except AttributeError:
				private = str(0)
			line = str(jsonDump["congress"])+","+billType[jsonDump["bill_type"]]+","+jsonDump["number"]+","+private+"\n"
			fw.write(line)