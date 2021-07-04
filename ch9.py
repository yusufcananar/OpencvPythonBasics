import cv2


def viewIm(winname,src,delay=0, resize=True):
    if resize:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    else:
        pass
    cv2.imshow(winname, src)
    cv2.waitKey(delay)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
im = cv2.imread('Resources/human-paladin.jpg')

imGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(im, (x,y), (x+w, y+h), (122,255,255), 1)

viewIm("original", im)





