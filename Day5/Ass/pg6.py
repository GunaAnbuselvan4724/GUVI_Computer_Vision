import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("Ass/sample.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges=cv2.Canny(img,50,100)

threshold,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
threshold,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
hist = cv2.calcHist(gray,[0],None,[256],[0,256])

plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
plt.show()