import cv2
img1=cv2.imread('lion.jpeg')
print(img1.shape)
img2=cv2.resize(img1,(512,512))
print(img2.shape)
img3=cv2.imread('nature.jpg')
print(img3.shape)
img4=cv2.resize(img3,(512,512))
print(img4.shape)


cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img3)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('lion_copy.png',img2)
cv2.imwrite('nature_copy.png',img4)

