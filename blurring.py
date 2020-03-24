import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('lena.jpg')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))#blurring algo
gblur=cv2.GaussianBlur(img,(5,5),0)#gaussian blur algo(removes high freq noises)
median=cv2.medianBlur(img,5)
bilateral=cv2.bilateralFilter(img,9,75,75)#highly used to keep edges sharp removes edge noises

titles=['image','2dconvolution','blur',"gblur",'median','bilateral']
images=[img,dst,blur,gblur,median,bilateral]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()