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

    if (x.tag == "{http://www.opengis.net/kml/2.2}value"):
        if ((len(re.findall('\d{10}:\d{2}:\d{3}:\d{4}', x.text)) > 0)):
            kad_number = x.text

    if(x.tag == "{http://www.opengis.net/kml/2.2}outerBoundaryIs"):
        outerBoundaryIs = True
        print(x.tag)


    if (x.tag == "{http://www.opengis.net/kml/2.2}coordinates" and outerBoundaryIs == True):
        res = x.text.replace(" ", "").split(sep="\n")
        coordsArr = []
        outerBoundaryIs = False
        print(x.text)

        for r in range(0, len(res), 1):
            if(r != 0 and r != len(res)-1):
               koord = res[r].split(sep=",")

               coordsArr.append({
                    "lat": koord[1],
                    "lon": koord[0]
                })
        # print(len(coordsArr))
        file = open("query.txt", "a", encoding="utf-8")
        # print("UPDATE bank_share set geo_points='{coords}' where kadastr_number='{kad_number}';\n".format(coords=coordsArr, kad_number=kad_number))
        file.write(
        "UPDATE bank_share set geo_points='{coords}' where kadastr_number='{kad_number}';\n".format(coords=json.dumps(coordsArr),
                                                                                                  kad_number=kad_number))
        file.close()
# coordsArr = []
