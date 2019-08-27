import numpy as np
import cv2

def constant_padding(img, kernel, constant):
    ps = len(kernel)-1 # padding size

    ns = (img.shape[0]+ps,img.shape[1]+ps) # image + padding size in all borders
    # creates result image bigger than original full of constant values
    result = np.ones(ns)*constant
    p = int(ps/2)
    result[p:-p,p:-p] = img[:,:] # put the original image on the middle 

    cv2.imwrite('constant_padding.png', result)


img = cv2.imread('baboon.png', 0)
kernel = np.arange(11*11).reshape((11,11))
constant_padding(img,kernel, 0)
