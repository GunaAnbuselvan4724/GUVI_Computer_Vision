import cv2
import matplotlib.pyplot as plt
 
img=cv2.imread("image2.jpg")
print(img.shape)
cv2.circle(img,(300,300),50,(250,0,0),10)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')
plt.show()
