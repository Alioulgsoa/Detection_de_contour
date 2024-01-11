import cv2 as cv
import numpy as np

theimage = cv.imread('euro.jpg', 0) #le zero pour importer l'image au niveux de gray
theimage = cv.resize(theimage, (600, 600))

ret, thres = cv.threshold(theimage, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU) # OTSU Threshold

contours, hierarchy = cv.findContours(thres, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) #detection contoure

color_image = cv.cvtColor(theimage, cv.COLOR_GRAY2BGR) # parceque je veux traiter en cv2

theimage = cv.drawContours(color_image, contours, -1, (200, 0, 0), 3) #-1 pour pas remplire , 1 pour l'epesseur
print("the number of contours :" + str(len(contours)))

# put the number of contours in the image
cv.putText(theimage, "the number of contours :" + str(len(contours)), (20, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 1)

cv.imshow('theimage', theimage)
cv.waitKey()
cv.destroyAllWindows()
