import os
import json

directories = ["109", "110", "111", "112", "113"]

billType = dict()
billType["H.Con.Res."] = "HC"
billType["H.J.Res."] = "HJ"
billType["H.R."] = "HR"
billType["H.Res."] = "HE"

billType["S.Con.Res."] = "SC"
billType["S.J.Res."] = "SJ"
billType["S."] = "SN"
billType["S.Res."] = "SE"

category = [
    "cloture", "passage_part", "unknown", "passage", "passage_suspension", "procedural",
    "nomination", "other", "conviction", "amendment", "veto_override", "ratification"]

for congress in directories:
        fw = open("cosponsorship2013/" + congress + "_rollcall.txt", "w")
        fr = open(congress + "_votes.txt", "r")
        for line in fr:
                jsonDump = json.loads(line)
                row = ["0" for i in range(25)]
                if jsonDump["related_bill"]:
                        row[0] = billType[jsonDump["related_bill"]["bill_type_label"]] + str(
                            jsonDump["related_bill"]["number"])
                        if jsonDump["chamber"] == "house":
                                row[category.index(
                                    jsonDump["category"]) + 1] = "1"
                        elif jsonDump["chamber"] == "senate":
                                row[category.index(
                                    jsonDump["category"]) + 13] = "1"
                        else:
                                print congress
                        fw.write(",".join(row) + "\n")
        fw.close()
        fr.close()
