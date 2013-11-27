import os
import json

directories = ["111","112","113"]
fwHouseStatus = open("cosponsorship2013/house_status.txt","w")

billType = {}
billType["hconres"] = "HC"
billType["hjres"] = "HJ"
billType["hr"] = "HR"
billType["hres"] = "HE"

statusSet = {"REFERRED"}

statusSetVector = dict()
statusSetVector["PROV_KILL:VETO"] = [0,0,0,-1,0]	 
statusSetVector["PROV_KILL:SUSPENSIONFAILED"] = [0,0,0,0,0]	 
statusSetVector["PASSED:SIMPLERES"] = [1,0,0,0,0]	 
statusSetVector["PROV_KILL:PINGPONGFAIL"] = [0,0,0,0,0]	 
statusSetVector["CONFERENCE:PASSED:HOUSE"] = [1,0,0,0,0]
statusSetVector["ENACTED:SIGNED"]=[0,0,0,1,0]
statusSetVector["FAIL:SECOND:SENATE"] =[1,0,0,0,0]
statusSetVector["CONFERENCE:PASSED:SENATE"] =[0,1,0,0,0]	 
statusSetVector["PASS_BACK:SENATE"] = [0,1,0,0,0]
statusSetVector["PROV_KILL:CLOTUREFAILED"] = [0,0,0,0,0]
statusSetVector["REPORTED"]= [0,0,0,0,1]
statusSetVector["PASSED:CONCURRENTRES"] = [1,1,0,0,0]
statusSetVector["PASSED:BILL"] = [1,1,0,0,0]	 
statusSetVector["VETOED:OVERRIDE_FAIL_ORIGINATING:HOUSE"] = [0,0,0,-1,0]
statusSetVector["REFERRED"] = [0,0,0,0,0]
statusSetVector["FAIL:ORIGINATING:HOUSE"] = [0,0,0,0,0]
statusSetVector["PASS_OVER:HOUSE"] = [1,0,0,0,0]

for congress in directories:
	for root, subFolders, files in os.walk(congress):
		if files:
			fr = open("./"+root+"/"+files[0],"r")
			jsonDump = json.loads(fr.read())
			line = [0,0,0,0,0]
			for i in jsonDump["actions"]:
				try :
					statusSet.add(i["status"])
					line = [(line[x] or statusSetVector[i["status"]][x])  for x in range(5)]
				except :
					m = 1
			try :
				if jsonDump["summary"]["as"].upper().find("PUBLIC") >= 0:
					print "PUBLIC : ./"+root+"/"+files[0]
					line.append(1)
				else:
					line.append(0)
			except:
				print "Except : ./"+root+"/"+files[0]
				line.append(0)
			line = [str(line[x]) for x in range(6)]
			#print line
			fwHouseStatus.write(",".join(line)+"\n")

print "Status set :" , statusSet