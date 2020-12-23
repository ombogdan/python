import json
import os

import shapefile

all_files = os.listdir("./АГРО-ТРЕЙДЕР ПП/Більмачівка/")
files_dbf = filter(lambda x: x.endswith('.dbf'), all_files)
result = []
for dbf in files_dbf:
    new_directory = dbf.replace('.dbf', "").replace("№", "").replace(" ", '')
    # os.mkdir("./newDirectory/")
    sf = shapefile.Reader("./АГРО-ТРЕЙДЕР ПП/Більмачівка/" + dbf, encoding='ISO8859-1')
    # header = ("lon" + "," + "lat" + "," + "val\n")
    k = []
    z = ''
    dict = {}
    dict["name"] = new_directory

    with shapefile.Reader("./АГРО-ТРЕЙДЕР ПП/Більмачівка/" + dbf, encoding='ISO8859-1') as shp:
        analysis_list = []

        for i in range(len(shp)):
            analysis = {}

            shapes = sf.shape(i)
            points_lon = shapes.points[0][0]
            points_lat = shapes.points[0][1]
            fields = sf.record(i)
            print(fields)

            shape = ("lat=" + str(points_lat) + "," + "lon=" + str(points_lon) + ";" + str(fields[5]) + ";" +
                     str(fields[6]) + ";" + str(fields[7]) + ";" + str(fields[8]) + ";" + str(fields[9]) + ";" +
                     str(fields[10]) + ";" + str(fields[11]) + ";" + 'null' + ";" + 'null' + ";" + 'null' + ";" +
                     'null' + ";" + 'null' + ";" + 'null' + ";" + 'null' + ";" + 'null' + ";" + 'null' + ";" + 'null' + ";" + 'null')
            # z = z + x
            analysis["lat"] = str(points_lat)
            analysis["lon"] = str(points_lon)
            analysis["k"] = str(fields[4])
            analysis["no3"] = str(fields[5])
            analysis["org"] = str(fields[6])
            analysis["p"] = str(fields[7])
            analysis["ph"] = str(fields[8])
            analysis["s"] = str(fields[9])
            analysis["zn"] = str(fields[10])
            analysis["ca"] = None
            analysis["mg"] = None
            analysis["na"] = None
            analysis["mn"] = None
            analysis["cu"] = None
            analysis["b"] = None
            analysis["fe"] = None
            analysis["ss"] = None
            analysis["bs"] = None
            analysis["cec"] = None
            analysis["al"] = None
            analysis_list.append(analysis)

    dict["analysis"] = analysis_list

    result.append(dict)
file = open("C:/Users/omelc/Desktop/shapes.txt", "w")
file.write(json.dumps(result))
