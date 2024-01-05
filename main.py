# Edge detection -Canny

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


the_image = cv.imread('euro.jpg')
#resized_img = cv.resize(the_image, (100, 100))

canny_image = cv.Canny(the_image, 100, 200)


# show image with OpenCV
'''cv.imshow('canny image', canny_image)
cv.waitKey()
cv.destroyWindow()'''

#show image with matplotlib

plt.subplot(121), plt.imshow(the_image), plt.title('the Original Image')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(canny_image), plt.title('Detected Image')
plt.xticks([]), plt.yticks([])

plt.show()