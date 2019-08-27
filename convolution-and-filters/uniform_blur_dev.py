import numpy as np
import cv2

def blur(img, size):
    result = img.copy()
    
    # our kernel is full of ones, because its an average
    kernel = np.ones((size,size),dtype='uint8')
    
    x1 = int(size/2)
    y1 = int(size/2)
    M,N = img.shape
    
    for y in range(M):
        for x in range(N):
            soma = 0
            q = 0
            for i in range(-x1,x1+1):
                for j in range(-y1,y1+1):
                    # we are not padding... just ignoring out of range pixels 
                    if (y-i<0) or (y-i>=M) or (x-j<0) or (x-j>=N):
                        continue
                    soma += kernel[i,j] * img[y-i,x-j]
                    q+=1
            # result pixel is sum of values of neighbourhood divided by theyr quantity 
            result[y,x] = int(soma/q)

    cv2.imwrite('blur-'+str(size)+'.png',result)












img = cv2.imread('baboon.png', 0)
blur(img, 3)
blur(img, 5)
blur(img, 7)
blur(img, 9)
blur(img, 11)

