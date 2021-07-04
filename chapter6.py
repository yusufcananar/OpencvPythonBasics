import cv2
import numpy as np

def viewIm(winname,src,delay=0, resize=True):
    if resize:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    else:
        pass
    cv2.imshow(winname, src)
    cv2.waitKey(delay)

im = cv2.imread("Resources/human-paladin.jpg")

imHor = np.hstack((im,im))
imVer = np.vstack((im,im))


viewIm("Horizontal", imHor)
viewIm("Vertical", imVer)