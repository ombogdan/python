﻿import json
import math
from datetime import time, datetime

import cv2
import numpy as np
from PIL import Image
startTime = datetime.now()
# 6524484000:05:001:0525
# x_max = 3820241.74586235
# x_min = 3819392.7599407
# y_max = 5817332.77901273
# y_min = 5816385.55007244

# 6524482200:03:052:0010
# x_max = 3788457.22413668
# x_min = 3787572.99214035
# y_max = 5821412.21089381
# y_min = 5820979.83161632

#test
x_max = 3780269.74851127
x_min = 3778558.22183336
y_max = 5818457.86423401
y_min = 5815799.1682824

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
image = Image.open("wms (19).png").convert('RGBA')
image.convert("RGBA")
canvas = Image.new('RGBA', image.size, (0, 0, 0, 0))  # Empty canvas colour (r,g,b,a)
canvas.paste(image, mask=image)  # Paste the image onto the canvas, using it's alpha channel as mask
canvas.save("canvastest.png", format="PNG")

# через багато перетворень виділяю чіткий контур на фото
img = cv2.imread("canvastest.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([158, 210, 24])
upper_red = np.array([0, 0, 0])
mask = cv2.inRange(hsv, lower_red, upper_red)
red_only = cv2.bitwise_and(img, img, mask=mask)

mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
res = cv2.subtract(hsv, mask)
res3 = cv2.subtract(img, res)
res4 = cv2.subtract(img, res3)
res5 = cv2.subtract(hsv, res4)
res6 = cv2.subtract(img, res5)
res7 = cv2.subtract(hsv, res6)
res9 = cv2.subtract(img, res5)

cv2.imwrite("res9.png", res9)
#

# роблю чорно білим і заливаю фігуру яка мені треба білим
image = cv2.imread('res9.png', 0)
# thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# cv2.fillPoly(image, cnts, [255, 255, 255])
# cv2.imwrite("fillImage.png", image)
x, y, w, h = cv2.boundingRect(image)
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.floodFill(image, None, (int(x + w / 2), int(y + h / 2)), 255)
cv2.imwrite("fillImage.png", image)
#

# тепер роблю так шоб з картінки брався тільки найбільший контур(може буть з прилеглими всякими)
# fillImage = cv2.imread('fillImage.png')
# gray = cv2.cvtColor(fillImage, cv2.COLOR_BGR2GRAY)
# ret, gray = cv2.threshold(gray, 127, 255, 0)
# gray2 = gray.copy()
# mask = np.zeros(gray.shape, np.uint8)
# contours, hier = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
#     if 0 < cv2.contourArea(cnt) < 2000000:
#         cv2.drawContours(fillImage, [cnt], 0, (0, 255, 0), 2)
#         cv2.drawContours(mask, [cnt], 0, 255, -1)
# cv2.imwrite("figureWithoutLines.png", mask)

# тоді я роблю ерозію шоб постирались лінії які прилягають до фігури
# figureWithoutLines = cv2.imread('figureWithoutLines.png', 0)
# kernel = np.ones((1, 1), np.uint8)
# erosion = cv2.erode(figureWithoutLines, kernel, iterations=1)
# dilation = cv2.dilate(figureWithoutLines,kernel,iterations = 1)
# cv2.imwrite("erosionImage.png", erosion)

# шукаю контур і накладаю білу лінію
# grayImage = cv2.imread('fillImage.png')
# imgGry = cv2.cvtColor(grayImage, cv2.COLOR_BGR2GRAY)
#
# ret, thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# angle = 0
# for i in range(len(contours)):
#     if (i != 0):
#         approx = cv2.approxPolyDP(contours[i], 0.01 * cv2.arcLength(contours[i], True), True)
#         cv2.drawContours(grayImage, [approx], 0, (255, 255, 255), 2)
#         # cv2.fillPoly(grayImage, pts = [approx], (255, 255, 255), 2)
#         cv2.fillPoly(grayImage, pts =[approx], color=(255,255,255))
#
#         print(approx)
#         x = approx.ravel()[0]
#         y = approx.ravel()[1] - 5
#         if (angle < len(approx)):
#             angle = len(approx)
#             print(angle)
#         c_list = []
#         for corner in approx:
#             x, y = corner.ravel()
#             c_list.append([int(x), int(y)])
#             # cv2.circle(grayImage, (x, y), 3, (0, 255, 0), -1)
#             # cv2.circle(img, (53,  87), 5, (0, 0, 255), -1)
#
# cv2.imwrite('addedWhiteLine.png', grayImage)
# # cv2.imshow('shapess.png', img)
# cv2.waitKey(0)


#
# замилення
filename = 'fillImage.png'
img = cv2.imread(filename)
kernel = np.ones((5, 5), np.float32) / 25
dst1 = cv2.filter2D(img, -1, kernel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayImage.png', dst1)

resultImage = cv2.imread('grayImage.png')
imgGry = cv2.cvtColor(resultImage, cv2.COLOR_BGR2GRAY)

ret, thrash = cv2.threshold(imgGry, 240, 255, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
angle = 0
# approxs = max(approx, key=len)
# print(approxs)додать фільтрацію треба по найбільшій площі а не кількості точок
for i in range(len(contours)):
    if (i != 0):
        approx = cv2.approxPolyDP(contours[i], 0.01 * cv2.arcLength(contours[i], True), True)
        # cv2.drawContours(addedWhiteLine, [approx], 0, (255, 255, 255), 3)

        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5
        if (angle < len(approx)):
            angle = len(approx)
        c_list = []
        coord = []
        for corner in approx:
            x, y = corner.ravel()
            c_list.append([int(x), int(y)])
            cv2.circle(resultImage, (x, y), 3, (0, 255, 0), -1)

            for i in range(len(corner)):

                x_mx = x_min + (corner[i][0] / zoom) * 9.554628536 - 9.554628536
                y_mx = y_min + (h / zoom * 9.554628536) - (corner[i][1] / zoom) * 9.554628536 - 9.554628536
                # print(x_mx, y_mx)
                x = x_mx
                y = y_mx

                lon = (x / 20037508.34) * 180
                lat = (y / 20037508.34) * 180
                lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
                coord.append({"lat": lat, "y": 0.0, "lon": lon, "x": 0.0, "z": 0.0})
        print(json.dumps(coord, ensure_ascii=False))



cv2.imshow('result.png', resultImage)
cv2.waitKey(0)



# # угли
# imgage = cv2.imread('grayImage.png')
# gray_img = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray_img,127,255,1)
#
# contours,h = cv2.findContours(thresh,1,2)
#
# # for cnt in contours:
# #     approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
# #     print(len(approx))
# #     cv2.drawContours(gray_img, [cnt], 0, (255, 0, 0), 2)
# #     # cv2.imshow('image', gray_img)
# #     cv2.waitKey(0)
#
# corner_img = np.float32(gray_img)
# # cv2.imshow('image', imgage)
# # cv2.waitKey(0)
# dst = cv2.cornerHarris(corner_img, 2, 3, 0.04)
# dst = cv2.dilate(dst, None)
# ret0, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
# dst = np.uint8(dst)
#
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
#
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv2.cornerSubPix(corner_img, np.float32(centroids), (5, 5), (-1, -1), criteria)
# # print(corners)
#
# for i in range(0, len(corners)):
#     print(corners[i])
# dst1[dst > 0.01 * dst.max()] = [0, 0, 255]
# coord = np.where(np.all(dst1 == (0, 0, 255), axis=-1))
# print(coord)
# # cv2.drawChessboardCorners(img, 23, corners)
# cv2.imshow('result.png', dst1)
# cv2.waitKey(0)
# # cv2.destroyAllWindows
