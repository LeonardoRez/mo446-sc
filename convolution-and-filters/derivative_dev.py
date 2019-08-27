import numpy as np
import cv2 

img = cv2.imread('baboon.png', 0)

kx = np.array([[0,0,0],[1,0,-1],[0,0,0]])

result_x = cv2.filter2D(img, -1, kx)

ky = np.array([[0,1,0],[0,0,0],[0,-1,0]])

result_y = cv2.filter2D(img, -1, ky)

cv2.imwrite('derivative_x.png',result_x)
cv2.imwrite('derivative_y.png',result_y)
