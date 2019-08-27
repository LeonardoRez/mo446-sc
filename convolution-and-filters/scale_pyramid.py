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

    original = img.copy()
    
    result = [] # result list of images
    result.append(original)

    while(len(original) >= 8):

        # apply gaussian filter
        original = cv2.filter2D(original, -1, kernel)
        # removes every odd row and column
        original = original[::2,::2]
        result.append(original)

    return result

