import cv2

def findfill(image):
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(cnts)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cv2.fillPoly(image, cnts, [255,255,0])
    cv2.imshow("findFill5.png", image)
    cv2.waitKey(0)

def me(image):
    x,y,w,h = cv2.boundingRect(image)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.floodFill(image,None,(int(x+w/2),int(y+h/2)),255)
    cv2.imshow("findFill5.png", image)
    cv2.waitKey(0)
    return image

image = cv2.imread('dilationImage.png', 0)
# cv2.imshow("imageOr", image)
# findfill(image)
me(image)