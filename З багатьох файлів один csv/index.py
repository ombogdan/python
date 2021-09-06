import json

geozoneGroupList = []
with open('groupName.csv', encoding='utf8') as Fil:
    read = Fil.readlines()
    for rowq in read:
        geozoneGroupList.append(rowq)

with open('z.crash', encoding='utf8') as File:
    read = File.readlines()
    allJson = json.loads(read[1])
    for i in allJson['geozoneList']:
        geozoneGroupName = ''
        for l in range(len(geozoneGroupList)):
            res = geozoneGroupList[l].split(sep=";")
            if (str(i['group_id']) == str(res[0])):
                geozoneGroupName = res[1]
                print(res[1])
        file = open("result.csv", "a", encoding="utf-8")
        file.write(i['name'] + ";" + str(geozoneGroupName).replace("\n", '').replace("'", '') + ";" + str(i['square_real']) + "\n")
        file.close()
