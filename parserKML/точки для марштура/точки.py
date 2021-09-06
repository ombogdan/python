import json
import os
import re
import xml.etree.ElementTree as ET

import simplekml

# all_files = os.listdir("./files")
# # print(all_files)
# kml = simplekml.Kml()
# for i in range(len(all_files)):

mytree = ET.parse('./doc.kml')
myroot = mytree.getroot()

kad_number = ''
outerBoundaryIs = False
for x in myroot.iter():
    latitude = ''
    longitude = ''
    role = None
    if(x.tag == "{http://www.opengis.net/kml/2.2}coordinates"):
        outerBoundaryIs = True
        pointArray = x.text.replace(" ", "").replace("0\n", "").split(sep=",")
        resultArray = []
        pointObject = {}
        lat = False
        lon = False
        name = 1
        print(pointArray)
        for i in range(0, len(pointArray), 1):

            if(i%2==0):
                lon = True
                pointObject['lon'] = pointArray[i]
            else:
                lat = True
                pointObject['lat'] = pointArray[i]

            if lat == True and lon == True:
                lat = False
                lon = False
                pointObject['name'] = ""+str(name)
                name = name+1
                resultArray.append(pointObject)
                pointObject = {}


        print(resultArray)
        file = open("result.json", "w", encoding="utf-8")
        # print("UPDATE bank_share set geo_points='{coords}' where kadastr_number='{kad_number}';\n".format(coords=coordsArr, kad_number=kad_number))
        file.write(json.dumps(resultArray))
        file.close()
# coordsArr = []
