import os
import json

directories = ["109","110","111","112","113"]

billType = dict()
billType["hconres"] = "HC"
billType["hjres"] = "HJ"
billType["hr"] = "HR"
billType["hres"] = "HE"
billType["sconres"] = "SC"
billType["sjres"] = "SJ"
billType["s"] = "SN"
billType["sres"] = "SE"
billType["H.Con.Res."] = "HC"
billType["H.J.Res."] = "HJ"
billType["H.R."] = "HR"
billType["H.Res."] = "HE"
billType["S.Con.Res."] = "SC"
billType["S.J.Res."] = "SJ"
billType["S."] = "SN"
billType["S.Res."] = "SE"

category = [ "cloture", "passage_part", "unknown", "passage", "passage_suspension", "procedural", 
			"nomination", "other", "conviction", "amendment", "veto_override", "ratification" ]

for congress in directories:
	dataDict = dict()
	sortedForm = []

	fw = open("cosponsorship2013/"+congress+"_rollcall_test.txt","w")

	for root, subFolders, files in os.walk(congress):
		if files:
			fr = open("./"+root+"/"+files[0],"r")
			jsonDump = json.loads(fr.read())
			sortedForm.append(billType[root.split("/")[1]]+jsonDump["number"])

	for root, subFolders, files in os.walk(congress+"-S"):
		if files:
			fr = open("./"+root+"/"+files[0],"r")
			jsonDump = json.loads(fr.read())
			sortedForm.append(billType[root.split("/")[1]]+jsonDump["number"])

	fr = open(congress+"_votes.txt","r")
	print congress
	lineCount = 0
	for line in fr:
		lineCount += 1
		jsonDump = json.loads(line)
		row = [0 for i in range(25)]
		if jsonDump["related_bill"]:
			row[0] = billType[jsonDump["related_bill"]["bill_type_label"]]+str(jsonDump["related_bill"]["number"])
			if jsonDump["chamber"] == "house" :
				row[category.index(jsonDump["category"])+1] = 1
			elif jsonDump["chamber"] == "senate" :
				row[category.index(jsonDump["category"])+13] = 1
			else :
				print congress
			if billType[jsonDump["related_bill"]["bill_type_label"]] == "HR" and str(jsonDump["related_bill"]["number"]) == "1973" and congress=="109":
				print lineCount, jsonDump["category"]
			if dataDict.has_key(row[0]):
				for i in range(len(row[1:])):
					if row[i+1]:
						dataDict[row[0]][i+1] = 1
			else :
				dataDict[row[0]] = row

	for bill in sortedForm:
		if dataDict.has_key(bill):
			row = [ str(i) for i in dataDict[bill]]
		else:
			row = [bill]
			row.extend(["0" for i in range(24)])
		fw.write(",".join(row)+"\n")
	fw.close()
	fr.close()