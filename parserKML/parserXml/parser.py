import os
import xml.etree.ElementTree as ET

import simplekml
import gpxpy.gpx
all_files = os.listdir("./files")
# print(all_files)
kml = simplekml.Kml()
for i in range(len(all_files)):
    gpx_file = open('./files/{file}'.format(file=all_files[i]))

    gpx = gpxpy.parse(gpx_file)

    coordsArr = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
                latitude = ''
                longitude = ''
                coordsArr.append((float(point.longitude), float(point.latitude)))

        # print(coordsArr)
        # exit(0)
        # for i in range(len(reader)):
        #     dataArray = str(reader[i]).split(';')
        # coordsStr = str(dataArray[3]).replace('POLYGON ((', '').replace('))', '').split(',')
    pol = kml.newpolygon()
    # print(all_files[i].replace('.xml', ''))
    pol.name = all_files[i].replace('.gpx', '')
    pol.outerboundaryis.coords = coordsArr

kml.save("Zones.kml")
