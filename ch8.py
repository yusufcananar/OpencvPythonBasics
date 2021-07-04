import cv2
import numpy as np

def viewIm(winname,src,delay=0, resize=True):
    if resize:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    else:
        pass
    cv2.imshow(winname, src)
    cv2.waitKey(delay)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(src):
    contours, hierarchy = cv2.findContours(src, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #cv2.drawContours(imCnt, cnt,-1,(255,200,250),3)

        if area > 0:
            cv2.drawContours(imCnt, cnt, -1, (100, 150, 150), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objectCorner = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objectCorner == 3:
                objectShape = 'Triangle'

            elif objectCorner == 4:
                aspectRatio = w/float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    objectShape = 'Square'
                else:
                    objectShape = 'Rectangle'

            elif objectCorner == 5:
                objectShape = 'Pentagon'

            elif objectCorner == 6:
                objectShape = 'Hexagon'

            elif objectCorner > 6:
                objectShape = 'Circle'

            else:
                objectShape = 'None'

            cv2.rectangle(imCnt, (x, y), (x + w, y + h), (255, 0, 120), 1)
            cv2.putText(imCnt, objectShape, (int(x+w/2 -10), int(y+h/2)),
                        cv2.FONT_HERSHEY_PLAIN, 0.5, (255,255,255),1)

kernel = np.ones((5,5))
path = "Resources/shapes.png"
im = cv2.imread(path)
imCnt = im.copy()
imGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGray, (5,5),0)
imCanny = cv2.Canny(imBlur,50,50)
imDilate = cv2.dilate(imCanny, kernel, iterations=1)

getContours(imCanny)

imStack = stackImages(1, ([im,imGray,imBlur],
                          [imCanny,imDilate,imCnt]))
viewIm("Stacked", imStack)