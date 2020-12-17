import cv2
import numpy as np
from PIL import Image
img = cv2.imread("fillImage.png")
# img = cv2.imread("red_only.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# jpg_image_mat = np.array(img)
# print(jpg_image_mat.shape)
# pixel_value_to_replace = 0
# rows, cols, channels = jpg_image_mat.shape
# for i in range(rows):
#     for j in range(cols):
#         if(jpg_image_mat[i, j, 1] == pixel_value_to_replace):
#             jpg_image_mat[i, j, 1] = 255
#
# # # changing 255 to 0 in second channel
# # for i in range(rows):
# #     for j in range(cols):
# #         if(jpg_image_mat[i, j, 2] == pixel_value_to_replace):
# #             jpg_image_mat[i, j, 2] = 255

# saving new modified matrix in image format
# new_image = Image.fromarray(jpg_image_mat)
# new_image.save("new_square.jpg")

# define range of red color in HSV
lower_red = np.array([76,98,113])
# lower_red = np.array([112, 132, 102])
upper_red = np.array([120, 89, 253])
# upper_red = np.array([0, 0, 0])
# Threshold the HSV image    to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)
# print(mask)
red_only = cv2.bitwise_and(img, img, mask=mask)

# convert mask to 3-channel image to perform subtract
mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

res = cv2.subtract(hsv, mask)  # negative values become 0 -> black
res2 = cv2.subtract(img, hsv)  # negative values become 0 -> black
res3 = cv2.subtract(img, res)  # negative values become 0 -> black
# res4 = cv2.subtract(hsv, res3)  # negative values become 0 -> black
res4 = cv2.subtract(img, res2)  # negative values become 0 -> black

# res4_mask = cv2.subtract(hsv, res4)
# hsv_res5 = cv2.subtract(res4_mask, res4)
# hsv_res6 = cv2.subtract(hsv_res5, hsv_res4)
coordinates = np.argwhere(mask)



cv2.imshow("img.png", img)
cv2.imshow("hsv", hsv)
cv2.imshow("res", res)
cv2.imshow("res2", res2)
cv2.imshow("res3", res3)
cv2.imshow("res4", res4)
cv2.waitKey(0)