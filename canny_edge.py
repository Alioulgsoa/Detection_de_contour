# Edge detection -Canny

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


the_image = cv.imread('euro.jpg')
#resized_img = cv.resize(the_image, (100, 100))
rgb_img = cv.cvtColor(the_image, cv.COLOR_BGR2RGB)  # convert BGR to RGB

canny_image = cv.Canny(rgb_img, 100, 200)

# show image with OpenCV
'''cv.imshow('canny image', canny_image)
cv.waitKey()
cv.destroyWindow()'''

#show image with matplotlib

plt.subplot(121), plt.imshow(rgb_img), plt.title('the Original Image')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(canny_image), plt.title('Detected Image')
plt.xticks([]), plt.yticks([])

plt.show()