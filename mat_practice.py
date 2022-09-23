import matplotlib.pyplot as plt
import cv2

# Color print - RGB convert
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()


# Grey print
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.imshow(imgGray, cmap='gray')
plt.show()

# print two image together
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray)
plt.show()