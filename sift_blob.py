# SIFT = Scale-Invariant Feature Transform
import cv2 as cv
import numpy as np

theImg = cv.imread('euro.jpg')
#theImg = cv.blur(theImg, (8, 8))
gray_img = cv.cvtColor(theImg, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kaypoints, discriptor = sift.detectAndCompute(gray_img, None)

theImg = cv.drawKeypoints(image=theImg, outImage=theImg, keypoints=kaypoints,
                         flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color=(255, 0, 0))


cv.imshow('keypoints', theImg)
print(len(kaypoints))
while(True):
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()