# Edge detection -Canny

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


the_image = cv.imread('euro.jpg')
#resized_img = cv.resize(the_image, (100, 100))

canny_image = cv.Canny(the_image, 100, 200)


#
cv.imshow('canny image', canny_image)
cv.waitKey()
cv.destroyWindow()
