import cv2
img=cv2.imread('lena.jpg',1)
img=cv2.line(img,(0,0),(255,255),(0,0,255),5)
img=cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),5)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),5)
img=cv2.circle(img,(447,63),(63),(0,255,0),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'opencv',(10,500),font,5,(255,255,255),10,cv2.LINE_8)
cv2.imshow('image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

