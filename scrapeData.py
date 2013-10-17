import json
import urllib

congress = 111
jsonDump = {}
filename = str(congress)+"_house_bills.txt"
offset=0

f = open(filename,"w")
test = urllib.urlopen("http://www.govtrack.us/api/v2/bill?congress="+str(congress)+"&"+"offset="+str(offset))
jsonDump = json.loads(test.read())
	
while (jsonDump["objects"]):
	offset += 1
	print jsonDump["meta"]["offset"], jsonDump["meta"]["total_count"]
	for obj in jsonDump['objects']:
		f.write(str(congress)+","+obj["bill_type"]+","+str(obj["id"])+","+str(obj["sliplawpubpriv"])+"\n")
	test = urllib.urlopen("http://www.govtrack.us/api/v2/bill?congress="+str(congress)+"&"+"offset="+str(offset))
	jsonDump = json.loads(test.read())	
f.close

	