# derivative mask to x axis 
kx = np.array([[0,0,0],[1,0,-1],[0,0,0]])
result_x = cv2.filter2D(img, -1, kx)

#derivative mask to y axis
ky = np.array([[0,1,0],[0,0,0],[0,-1,0]])
result_y = cv2.filter2D(img, -1, ky)

