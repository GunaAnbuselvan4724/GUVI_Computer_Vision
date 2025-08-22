import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("Ass/sample.jpg")

h,w = img.shape[:2]
m=cv2.rectangle(img,(50,50),(100,100),(255,0,0),2)
plt.imshow(cv2.cvtColor(m,cv2.COLOR_BGR2RGB))
plt.show()