import json
import math

# def loading_displaying_saving():
import numpy as np

# img = cv2.imread('2.png', 0)
# kernel = np.ones((5, 5), np.hsplit)
# erosion = cv2.erode(img, kernel, iterations=1)
# cv.imwrite('gray.jpg', img)


# 6524482200:03:052:0010
x_max = 3788457.22413668
x_min = 3787572.99214035
y_max = 5821412.21089381
y_min = 5820979.83161632

# 6524484000:05:001:0525
# x_max = 3820241.74586235
# x_min = 3819392.7599407
# y_max = 5817332.77901273
# y_min = 5816385.55007244

x_max_result = x_max + 9.554628536
x_min_result = x_min - 9.554628536
y_max_result = y_max + 9.554628536
y_min_result = y_min - 9.554628536
zoom = 3
w = (x_max_result - x_min_result) / 9.554628536 * zoom
h = (y_max_result - y_min_result) / 9.554628536 * zoom
url = 'https://m1.land.gov.ua/geowebcache/service/wms?tiled=true&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=kadastr&TILED=true&STYLES=&SRS=EPSG%3A900913&WIDTH={w}&HEIGHT={h}&CRS=EPSG%3A900913&BBOX={x_min_result}%2C{y_min_result}%2C{x_max_result}%2C{y_max_result}' \
    .format(x_max_result=x_max_result, x_min_result=x_min_result, y_max_result=y_max_result, y_min_result=y_min_result,
            h=np.math.ceil(h),
            w=np.math.ceil(w))
print(url)
arr = [[270, 7],

       [93, 135],

       [65, 135],

       [48, 118],

       [20, 55],

       [23, 42],

       [8, 33]]

coord = []

for i in range(len(arr)):
    x_mx = x_min + (arr[i][0] / zoom) * 9.554628536 - 9.554628536
    y_mx = y_min + (h / zoom * 9.554628536) - (arr[i][1] / zoom) * 9.554628536 - 9.554628536
    # print(x_mx, y_mx)
    x = x_mx
    y = y_mx

    lon = (x / 20037508.34) * 180
    lat = (y / 20037508.34) * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    coord.append({"lat": lat, "y": 0.0, "lon": lon, "x": 0.0, "z": 0.0})
print(json.dumps(coord, ensure_ascii=False))
