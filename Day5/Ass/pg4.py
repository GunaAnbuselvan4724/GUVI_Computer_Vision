import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("Ass/sample.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges=cv2.Canny(img,50,100)

plt.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
plt.show()