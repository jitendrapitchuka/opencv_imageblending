import cv2
#import numpy as np
img=cv2.imread('nature3.jpg')
img2=cv2.imread('messi5.jpg')
#print(img.shape)#returns a tuple of no of rows,coloumns,and channels



img=cv2.resize(img,(500,500))
img2=cv2.resize(img2,(500,500))

#dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,.8,img2,.2,0,)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()