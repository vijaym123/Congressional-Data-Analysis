import json
import urllib
import time

congressList = [111,112,113]

for congress in congressList:
    filename = str(congress)+"_votes.txt"
    jsonDump = {}
    offset=0
    f = open(filename,"w")
    test = urllib.urlopen("http://www.govtrack.us/api/v2/vote/?congress="+str(congress)+"&"+"offset="+str(offset)+"&limit=600")
    jsonDump = json.loads(test.read())
    total_count = jsonDump["meta"]["total_count"]
    while offset <= int(total_count):
        offset += 1
        print jsonDump["meta"]["offset"], jsonDump["meta"]["total_count"]
        for obj in jsonDump['objects']:
            f.write(json.dumps(obj))
        test = urllib.urlopen("http://www.govtrack.us/api/v2/vote/?congress="+str(congress)+"&"+"offset="+str(offset))
        while True:
            try :
                jsonDump = json.loads(test.read())
                break
            except :
                print "sleeping"
                time.sleep(60*10)
                test = urllib.urlopen("http://www.govtrack.us/api/v2/vote/?congress="+str(congress)+"&"+"offset="+str(offset))
    f.close()