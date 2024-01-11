import cv2 as cv
import numpy as np

img = cv.imread('euro.jpg', cv.IMREAD_COLOR) # lire l'image en coleur
img = cv.resize(img, (600, 600))

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #bgr a une image niveux de gray
gray_blurred = cv.blur(gray_img, (5, 5)) #application d'un filtre blure

cv.imshow('blured image', gray_blurred)
cv.waitKey()
cv.destroyAllWindows()

