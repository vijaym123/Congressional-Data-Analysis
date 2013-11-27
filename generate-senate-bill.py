import os
import json

directories = ["111-S","112-S","113-S"]
fwSenateBill = open("cosponsorship2013/senate_bills.txt","w")
fwSenateCommittee = open("cosponsorship2013/senate_committees.txt","w")

billType = {}
billType["sconres"] = "SC"
billType["sjres"] = "SJ"
billType["s"] = "SN"
billType["sres"] = "SE"
billType["SP"] = "SP"

for congress in directories:
	for root, subFolders, files in os.walk(congress):
		if files:
			fr = open("./"+root+"/"+files[0],"r")
			jsonDump = json.loads(fr.read())
			try :
				if jsonDump["bill_type"] not in billType.keys():
					break
				elif jsonDump["subjects_top_term"].find("Private")>=0:
					#print "./"+root+"/"+files[0]
					private = str(1)
				else :
					private = str(0)
				if jsonDump["amendments"] != []:
					#print "./"+root+"/"+files[0]
					#print jsonDump["amendments"]
					jsonDump["bill_type"] = "SP"
			except AttributeError:
				private = str(0)
			houseCommittee = ""
			for i in jsonDump["committees"]:
				houseCommittee += i["committee"].replace(",","") + ","
			if houseCommittee == "":
				houseCommittee = "NA,"
			line = str(jsonDump["congress"])+","+billType[jsonDump["bill_type"]]+","+jsonDump["number"]+","+private+"\n"
			fwSenateBill.write(line)
			fwSenateCommittee.write(houseCommittee[:-1]+"\n")

fwSenateBill.close()
fwSenateCommittee.close()