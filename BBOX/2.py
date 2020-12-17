import cv2
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image
image = Image.open("wms (5).png").convert('RGBA')
image.convert("RGBA")
canvas = Image.new('RGBA', image.size, (0,0,0,0)) # Empty canvas colour (r,g,b,a)
canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
canvas.save("wms5captcha.png", format="PNG")

from scipy.spatial import distance

sample_img = cv2.imread("wms5captcha_result.png",  cv2.IMREAD_UNCHANGED)

# convert to black and white color space
sample_img_grey = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('image', sample_img_grey)
# cv2.waitKey(0)
contours, hierarchy = cv2.findContours(sample_img_grey, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow('image', sample_img_grey)
# find center of image and draw it (blue circle)
image_center = np.asarray(sample_img_grey.shape) / 2
image_center = tuple(image_center.astype('int32'))
# cv2.circle(sample_img, image_center, 1, (255, 100, 0), )

buildings = []
max_counturs = max(contours, key=len)
# for contour in max_counturs:
    # find center of each contour
M = cv2.moments(max_counturs)
perimeter = cv2.contourArea(max_counturs)
print(perimeter)
if(M["m00"]>0):
    center_X = int(M["m10"] / M["m00"])
    center_Y = int(M["m01"] / M["m00"])
    contour_center = (center_X, center_Y)
# calculate distance to image_center
    distances_to_center = (distance.euclidean(image_center, contour_center))

# save to a list of dictionaries
    buildings.append({'contour': max_counturs, 'center': contour_center, 'distance_to_center': distances_to_center})

# draw each contour (red)
    cv2.drawContours(sample_img, [max_counturs], 0, (255, 0, 0), 1)
    M = cv2.moments(max_counturs)
    print(M)
    rect = cv2.minAreaRect(max_counturs)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(max_counturs)
    # cv2.fillPoly(sample_img, pts =[max_counturs], color=(255,255,255))
    # cv2.drawContours(sample_img_grey, [box], 0, (255, 255, 255), 1)
    # cv2.waitKey(0)


    # draw center of contour (green)
    # cv2.circle(sample_img, contour_center, 3, (100, 255, 0), 2)

    # sort the buildings
    sorted_buildings = sorted(buildings, key=lambda i: i['distance_to_center'])

    # find contour of closest building to center and draw it (blue)
    center_building_contour = sorted_buildings[0]['contour']
    cv2.drawContours(sample_img, [center_building_contour], 0, (0, 255, 0), 2)

cv2.imshow("Image5.png", sample_img)
# cv2.imshow("Image3.png", mask)
cv2.waitKey(0)