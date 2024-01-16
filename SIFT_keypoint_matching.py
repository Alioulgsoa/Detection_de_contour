import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img1 = cv.imread("euro_normal.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("euro_pivo90.jpg", cv.IMREAD_GRAYSCALE)

#initialisation de sift algorithme
sift = cv.SIFT.create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)


bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

#trouver les bon descripteur
good= []  #tableau vide
for m, n, in matches:
    if m.distance < 0.55*n.distance:
        good.append([m])

img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=cv.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3), plt.show()


