import cv2
import numpy as np
img=cv2.imread("lena.jpg")
lr1=cv2.pyrDown(img)
lr2=cv2.pyrDown(lr1)
hr1=cv2.pyrUp(lr2)

cv2.imshow('image',img)
cv2.imshow('pyrdown 1 image',lr1)
cv2.imshow('pyrdown 2 image',lr2)
cv2.imshow('pyrup',hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()