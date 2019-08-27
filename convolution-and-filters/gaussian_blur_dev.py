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


def gausian_blur(img, size):
    k = pascal(size) # pascal vector of size=size
    k = (k*k.T)/((2**(size-1))**2) #the real kernel divided by size

    result = cv2.filter2D(img,-1,k)

    cv2.imwrite('gaussian-'+str(size)+'.png', result)



img = cv2.imread('baboon.png',0)
gausian_blur(img, 3)
gausian_blur(img, 5)
gausian_blur(img, 7)
gausian_blur(img, 9)
gausian_blur(img, 11)
