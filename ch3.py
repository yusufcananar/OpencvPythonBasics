import cv2

im = cv2.imread("Resources/human-paladin.jpg")
print(im.shape)
#Resize
im = cv2.resize(im, None ,fx=0.5, fy=0.5)
print(im.shape)

#Cropping
imCropped = im[30:180, 200:500]

cv2.imshow("image", im)
cv2.imshow("Cropped", imCropped)
cv2.waitKey(0)