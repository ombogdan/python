import os
import xml.etree.ElementTree as ET

import simplekml

all_files = os.listdir("./filexXML")
# print(all_files)
kml = simplekml.Kml()
for i in range(len(all_files)):
    mytree = ET.parse('./filexXML/{file}'.format(file=all_files[i]))
    myroot = mytree.getroot()
    coordsArr = []
    for x in myroot[3]:
        # for c in range(len(coordsStr)):
        #    arr = coordsStr[c].split(' ')
        #    coordsArr.append((float(arr[0]), float(arr[1])))
        latitude = ''
        longitude = ''
        role = None
        for key, value in x.attrib.items():
            if (key == 'latitude'):
                latitude = value
            if (key == 'longitude'):
                longitude = value
            if (key == 'oID'):
                if(value.find('RTCM-Ref')==0):
                    role = 'role'
        # if(role==None):
        #     print(latitude)
        if (role == None):
            # print('44444')
            coordsArr.append((float(longitude), float(latitude)))
            role = None
        # print(coordsArr)
        # exit(0)
        # for i in range(len(reader)):
        #     dataArray = str(reader[i]).split(';')
        # coordsStr = str(dataArray[3]).replace('POLYGON ((', '').replace('))', '').split(',')

    pol = kml.newpolygon()
    print(all_files[i].replace('.xml', ''))
    pol.name = all_files[i].replace('.xml', '')
    pol.outerboundaryis.coords = coordsArr
kml.save("Zones1.kml")