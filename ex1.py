import cv2
import matplotlib.pyplot as plt 

img=cv2.imread("image1.jpeg")
print(img.shape)
img=cv2.cvtcolor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')
plt.show()