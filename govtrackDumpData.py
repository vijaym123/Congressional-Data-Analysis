import json
import urllib
import time

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
		f.write(json.dumps(obj))
	test = urllib.urlopen("http://www.govtrack.us/api/v2/bill?congress="+str(congress)+"&"+"offset="+str(offset))	
	jsonDump = json.loads(test.read())	
	if offset%5000 == 0:
		print "sleeping"
		time.sleep(60*10)
f.close()