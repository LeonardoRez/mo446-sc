def constant_padding(img, kernel, constant):
    ps = len(kernel)-1 # padding size

    ns = (img.shape[0]+ps,img.shape[1]+ps) # image + padding size in all borders
    # creates result image bigger than original full of constant values
    result = np.ones(ns)*constant

    p = int(ps/2) # takes padding lengh for each border (they're all the same length
    result[p:-p,p:-p] = img[:,:] # put the original image on the middle 
    
    return result
