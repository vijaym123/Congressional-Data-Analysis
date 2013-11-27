import os
import json

directories = ["111","112","113"]
fwHouseBill = open("cosponsorship2013/house_bills.txt","w")
fwHouseCommittee = open("cosponsorship2013/house_committees.txt","w")

billType = {}
billType["hconres"] = "HC"
billType["hjres"] = "HJ"
billType["hr"] = "HR"
billType["hres"] = "HE"
billType["HZ"] = "HZ"

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
				if jsonDump["amendments"] != []:
					#print "./"+root+"/"+files[0]
					#print jsonDump["amendments"]
					jsonDump["bill_type"]="HZ"
			except AttributeError:
				private = str(0)
			houseCommittee = ""
			for i in jsonDump["committees"]:
				houseCommittee += i["committee"].replace(",","") + ","
			if houseCommittee == "":
				houseCommittee = "NA,"
			line = str(jsonDump["congress"])+","+billType[jsonDump["bill_type"]]+","+jsonDump["number"]+","+private+"\n"
			fwHouseBill.write(line)
			fwHouseCommittee.write(houseCommittee[:-1]+"\n")

fwHouseBill.close()
fwHouseCommittee.close()