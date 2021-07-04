import cv2
import numpy as np

im = cv2.imread("Resources/human-paladin.jpg")
im = cv2.resize(im, None ,fx=0.5, fy=0.5)

kernel = np.ones((5,5), np.uint8)

# Convert to Grayscale image
imGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# Gaussian Blur
imBlur = cv2.GaussianBlur(imGray, (7,7), 0)
#Canny Edge
imCanny = cv2.Canny(im, 150,200)
#Dilation
imDilation = cv2.dilate(imCanny, kernel, iterations=1)
#Erosion
imErosion = cv2.erode(imDilation, kernel , iterations=1)

cv2.imshow("Gray", imGray)
cv2.imshow("Blur", imBlur)
cv2.imshow("Canny", imCanny)
cv2.imshow("Dilation", imDilation)
cv2.imshow("Erosion", imErosion)

cv2.waitKey(0)
cv2.destroyAllWindows()