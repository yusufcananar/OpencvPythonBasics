import cv2
import numpy as np

im = np.zeros((512,512,3))
print(im.shape)
#im[200:, :100] = 255,0,0

cv2.line(im, (0,0), (im.shape[1],im.shape[0]), (0,255,255),3)
cv2.rectangle(im, (0,0), (250,350), (255,0,0),1)
cv2.circle(im, (400,50),30,(0,0,255), 5)
cv2.putText(im, "OPENCV ", (300, 200), cv2.FONT_HERSHEY_PLAIN,
            2, (0,150,0),1)
cv2.imshow("Image", im)
cv2.waitKey(0)