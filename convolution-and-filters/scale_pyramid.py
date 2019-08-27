import numpy as np
import cv2

def pascal(n):
    k = np.zeros((n,n))
    k[0,0] = 1
    for x in range(1,n):
        k[x,0] = k[x-1,0]
        for y in range(1,x+1):
            k[x,y] = k[x-1,y-1] + k[x-1,y]
    return np.array([k[n-1]])

def gaussian_pyramid(img):
    v = pascal(5) # paschal vector for size 5 = [1,4,6,4,1]
    kernel = (v*v.T)/(16**2) # kernel for gaussian filter

    result = img.copy()

    while(len(result) >= 8):

        result = cv2.filter2D(result, -1, kernel)
        result = result[::2,::2]
        cv2.imwrite('pyramid-'+str(len(result))+'.png',result)


img = cv2.imread('baboon.png', 0)
gaussian_pyramid(img)
