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
            # result pixel is sum of values of neighbourhood divided by their quantity 
            result[y,x] = int(soma/q)
    return result
