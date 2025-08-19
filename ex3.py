import cv2
import matplotlib.pyplot as plt
img=cv2.imread("image3.jpg")
blur=cv2.blur(img,(5,5))
gaussian=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img,5)
plt.imshow(cv2.cvtColor(median,blur,gaussian,cv2.COLOR_BGR2RGB))
plt.show()