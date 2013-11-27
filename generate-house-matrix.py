import os
import json
import time
directories = ["111","112","113"]

for congress in directories:
	fw = open("cosponsorship2013/house_datematrices/"+congress+"_housedatematrix.txt","w")
	fwMembers = open("cosponsorship2013/house_members/"+congress+"_house.txt","w")	
	fwMatrix = open("cosponsorship2013/house_matrices/"+congress+"_housematrix.txt","w")
	dataMatrix = dict()
	members = dict()
	matrix = dict()
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
					matrix[jsonDump["sponsor"]["thomas_id"]] = dict()

				dataMatrix[jsonDump["sponsor"]["thomas_id"]]["v"+str(count)] = jsonDump["introduced_at"]
				matrix[jsonDump["sponsor"]["thomas_id"]]["v"+str(count)] = "1"

				for i in jsonDump["cosponsors"]:
					if not dataMatrix.has_key(i["thomas_id"]) :
						dataMatrix[i["thomas_id"]]=dict()
						members[i["thomas_id"]] = " ".join(i["name"].split(","))
						matrix[i["thomas_id"]] = dict()
					dataMatrix[i["thomas_id"]]["v"+str(count)] = i["sponsored_at"]
					

					if i["withdrawn_at"] and not(matrix[i["thomas_id"]].has_key("v"+str(count))):
						matrix[i["thomas_id"]]["v"+str(count)] = "5"
						#print "./"+root+"/"+files[0]
						#if time.mktime(time.strptime(i["withdrawn_at"],"%Y-%m-%d")) < time.mktime(time.strptime(i["sponsored_at"],"%Y-%m-%d")):
							#print "./"+root+"/"+files[0]
					#elif i["withdrawn_at"] and matrix[i["thomas_id"]].has_key("v"+str(count)) and matrix[i["thomas_id"]]["v"+str(count)] == 5:
						#matrix[i["thomas_id"]]["v"+str(count)] = "3"
						#print "./"+root+"/"+files[0]
					else :
						matrix[i["thomas_id"]]["v"+str(count)] = "2"

			except TypeError:
				print "./"+root+"/"+files[0]
				print count
	myList = ["v" + str(i) for i in range(1,count+1)]
	line = ",".join(myList)
	fw.write(line+"\n")
	for thomasId in dataMatrix:
		fwMembers.write(members[thomasId] +", "+ thomasId+"\n")
		myList = ["NA" for i in range(1,count+1)]
		for bill in dataMatrix[thomasId]:
			myList[int(bill[1:])-1] = dataMatrix[thomasId][bill]
		line = ",".join(myList)
		fw.write(line+"\n")

		myList = ["0" for i in range(1,count+1)]
		for bill in matrix[thomasId]:
			myList[int(bill[1:])-1] = matrix[thomasId][bill]
		line = ",".join(myList)
		fwMatrix.write(line+"\n")	
	fwMembers.close()
	fw.close()
	fwMatrix.close()