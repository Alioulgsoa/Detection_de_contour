import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

theImage = cv2.imread('euro.jpg')
#theImage = cv2.resize(theImage, (600, 500)) #si je veux resizer l'image

gray_img = cv2.cvtColor(theImage, cv2.COLOR_BGR2GRAY)
rgb_img = cv2.cvtColor(theImage, cv2.COLOR_BGR2RGB)

thres = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
output = theImage.copy()

cv2.drawContours(output, cnts, -1, (40, 50, 200), 3)
text = "{} objects found".format(len(cnts))
cv2.putText(output, text, (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


plt.subplot(221), plt.imshow(rgb_img), plt.title("original image")
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(gray_img, cmap='Greys_r'), plt.title("gray image")
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(thres, cmap='Greys_r'), plt.title("threshold image")
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(output), plt.title(text)
plt.xticks([]), plt.yticks([])

plt.show()