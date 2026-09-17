import copy
classDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
a=copy.deepcopy(classDict["class"]["student"]["name"])
print(a)
classDict["class"]["student"]["marks"]["physics"]=89
classDict["averageMike"]=(classDict["class"]["student"]["marks"]["physics"]+classDict["class"]["student"]["marks"]["history"])/2
classDict["class"]["student"]=[classDict["class"]["student"]]

Ted = {"name" : "Ted",
    "marks": {
        "physics": 34,
        "history": 99
    }
}
classDict["class"]["student"].append(Ted)
classDict["averageTed"]=(classDict["class"]["student"][1]["marks"]["physics"]+classDict["class"]["student"][1]["marks"]["history"])/2

b=0
for i in range(len(classDict["class"]["student"])):
    b=b+(classDict["class"]["student"][i]["marks"]["physics"]+classDict["class"]["student"][i]["marks"]["history"])/2
b=b/(len(classDict["class"]["student"]))
classDict["class"]["average_grade"]=b
print(classDict)


