import json
import re
import xml.etree.ElementTree as ET

import simplekml

# all_files = os.listdir("./files")
# # print(all_files)
# kml = simplekml.Kml()
# for i in range(len(all_files)):

mytree = ET.parse('./new.kml')
myroot = mytree.getroot()

kad_number = ''
outerBoundaryIs = False


def in_dictionary(key, dict):
    return key in dict


coord = ''
Singulation = ''
Elevation = ''
resultArray = []
for x in myroot.iter():
    latitude = ''
    longitude = ''
    role = None

    if (x.tag == 'coordinates'):
        coordinateArray = x.text.split(sep=",")
        coord = {
            'lon': coordinateArray[0],
            'lat': coordinateArray[1]
        }
    if (in_dictionary('name', x.attrib) == True):
        attrib = x.attrib
        # if(x.tag=='coordinates'):
        # print(x.text)
        if (attrib['name'] == "Singulation(%)"):
            Singulation = x.text
        if (attrib['name'] == "Elevation(m)"):
            Elevation = x.text

    if (coord != '' and Singulation != '' and Elevation != ''):
        resultArray.append({
            'coordinates': coord,
            'singulation': Singulation,
            'elevation': Elevation,
        })
        coord = ''
        Singulation = ''
        Elevation = ''
file = open("data.json", "a", encoding="utf-8")
file.write(json.dumps(resultArray))
file.close()
# coordsArr = []
