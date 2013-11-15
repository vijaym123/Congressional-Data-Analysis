import os
import json

directories = ["111","112","113"]

for congress in directories:
	fw = open("cosponsorship2013/house_datematrices/"+congress+"_housedatematrix.txt","w")
	fwMembers = open("cosponsorship2013/house_members/"+congress+"_house.txt","w")	
	dataMatrix = dict()
	members = dict()
	count = 0
	for root, subFolders, files in os.walk(congress):
		if files:
			try :
				count += 1
				fr = open("./"+root+"/"+files[0],"r")
				jsonDump = json.loads(fr.read())
				if not dataMatrix.has_key(jsonDump["sponsor"]["thomas_id"]) :
					dataMatrix[jsonDump["sponsor"]["thomas_id"]]=dict()
					members[jsonDump["sponsor"]["thomas_id"]] = " ".join(jsonDump["sponsor"]["name"].split(","))
				dataMatrix[jsonDump["sponsor"]["thomas_id"]]["v"+str(count)] = jsonDump["introduced_at"]

				for i in jsonDump["cosponsors"]:
					if not dataMatrix.has_key(i["thomas_id"]) :
						dataMatrix[i["thomas_id"]]=dict()
						members[i["thomas_id"]] = " ".join(i["name"].split(","))
					dataMatrix[i["thomas_id"]]["v"+str(count)] = i["sponsored_at"]
			except TypeError:
				print "./"+root+"/"+files[0]
	myList = ["v" + str(i) for i in range(1,count+1)]
	line = ",".join(myList)
	fw.write(line+"\n")
	for thomasId in dataMatrix:
		fwMembers.write(members[thomasId] +", "+ thomasId+"\n")
		myList = ["NA" for i in range(1,count+1)]
		for bill in dataMatrix[thomasId]:
			myList[int(bill[1:])-1] = dataMatrix[thomasId][bill]
		line = line = ",".join(myList)
		fw.write(line+"\n")
	fwMembers.close()
	fw.close()