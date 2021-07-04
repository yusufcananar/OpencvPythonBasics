import cv2
import numpy as np

def viewIm(winname,src,delay=0, resize=True):
    if resize:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    else:
        pass
    cv2.imshow(winname, src)
    cv2.waitKey(delay)

im = cv2.imread("Resources/casino.jpg")
width, height = 250,350
pts1 = np.float32([[454,326],[561,283],[690,365], [780,313]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imRes = cv2.warpPerspective(im, matrix, (width,height))


viewIm("Image", im, resize=False)
viewIm("Result", imRes)