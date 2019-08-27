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
    k = (k*k.T)/((2**(size-1))**2) #the real kernel divided by sum of all lenghts

    result = cv2.filter2D(img,-1,k)

    return result


