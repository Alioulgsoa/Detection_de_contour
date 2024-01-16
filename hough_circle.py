import cv2 as cv
import numpy as np

img = cv.imread('euro.jpg', cv.IMREAD_COLOR) # lire l'image en coleur
img = cv.resize(img, (600, 600))

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #bgr a une image niveux de gray
gray_blurred = cv.blur(gray_img, (8, 8)) #application d'un filtre blure

#detection des circle avec le Hough
detected_circles = cv.HoughCircles(gray_blurred, cv.HOUGH_GRADIENT, dp=2.2, minDist=100, param1=200, param2=100, minRadius=0, maxRadius=0 )

#tracer les circles
if detected_circles is not None:
    detected_circles = np.int16(np.around(detected_circles))
    for i in detected_circles[0, :]:
        a, b, r = i[0], i[1], i[2]
        cv.circle(img, (a, b), r, (0, 255, 0), 2)
        cv.circle(img, (a, b), 1, (0, 0, 255), 3)

    cv.imshow('detected_circles', img)
    cv.waitKey()
    cv.destroyAllWindows()



'''cv.imshow('blured image', gray_blurred)
cv.waitKey()
cv.destroyAllWindows()'''

