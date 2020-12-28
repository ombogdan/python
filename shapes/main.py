import json
import os

import shapefile
dir = "3/Shape точки 28.12.2020/Shape_3/"
all_files = os.listdir(dir)
files_dbf = filter(lambda x: x.endswith('.dbf'), all_files)
result = []
for dbf in files_dbf:
    # print(dbf)
    new_directory = dbf.replace('.dbf', "").replace("№", "").replace(" ", '')
    sf = shapefile.Reader(dir+ dbf, encoding='ISO8859-1')

    k = []
    z = ''
    name = None
    analysis_list = []

    with shapefile.Reader(dir + dbf, encoding='ISO8859-1') as shp:
        # print(dbf)
        fields_0 = sf.fields[1:]
        field_names = [field[0] for field in fields_0]

        for i in range(len(shp)):
            print(dbf)
            shapes = sf.shape(i)
            fields = sf.record(i)

            if (name != fields[1]):
                # print("!=")
                dict = {}
                dict["name"] = fields[13]
                dict["analysis"] = []
                result.append(dict)

            res = result[-1]
            # print(fields[7])

            if (shapes.shapeType != 5):
                analysis = {}
                points_lon = shapes.points[0][0]
                points_lat = shapes.points[0][1]

                analysis["lat"] = str(points_lat)
                analysis["lon"] = str(points_lon)

                analysis["k"] = str(fields[6])
                analysis["no3"] = str(fields[3])
                analysis["org"] = str(fields[2])
                analysis["p"] = str(fields[5])
                analysis["ph"] = str(fields[1])
                analysis["s"] = str(fields[12])
                analysis["zn"] = None
                analysis["ca"] = str(fields[7])
                analysis["mg"] = str(fields[8])
                analysis["na"] = str(fields[9])
                analysis["mn"] = None
                analysis["cu"] = None
                analysis["b"] = None
                analysis["fe"] = None
                analysis["ss"] = str(fields[11])
                analysis["bs"] = str(fields[4])
                analysis["cec"] = str(fields[10])
                analysis["al"] = None
                analysis["cl"] = None

                dict["analysis"].append(analysis)
            else:
                print('+==========================================================+')
                analysis = {}
                analysis["coordinates"] = []
                coordinate = shapes.points

                for c in range(len(coordinate)):
                    coordinates = {}
                    coordinates["lon"] = coordinate[c][0]
                    coordinates["lat"] = coordinate[c][1]
                    analysis["coordinates"].append(coordinates)

                # print(coordinates)
                points_lon = ""
                points_lat = ""
                analysis["lat"] = str(points_lat)
                analysis["lon"] = str(points_lon)
                # print(str(fields[22]))
                analysis["k"] = str(fields[9])
                analysis["no3"] = str(fields[6])
                analysis["org"] = str(fields[5])
                analysis["p"] = str(fields[8])
                analysis["ph"] = str(fields[4])
                analysis["s"] = str(fields[15])
                analysis["zn"] = str(fields[17])
                analysis["ca"] = str(fields[10])
                analysis["mg"] = str(fields[11])
                analysis["na"] = str(fields[12])
                analysis["mn"] = str(fields[19])
                analysis["cu"] = str(fields[16])
                analysis["b"] = str(fields[20])
                analysis["fe"] = str(fields[18])
                analysis["ss"] = str(fields[14])
                analysis["bs"] = str(fields[7])
                analysis["cec"] = str(fields[13])
                analysis["al"] = str(fields[21])
                analysis["cl"] = str(fields[22])

                dict["analysis"].append(analysis)

            name = fields[13]

    # print(json.dumps(result))

file = open("ivannucha.json", "w")
file.write(json.dumps(result))
