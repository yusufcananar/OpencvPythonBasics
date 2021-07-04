import cv2
print("package imported..")

# Read and Show image
img = cv2.imread("Resources/human-paladin.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------

# Read and Show video or webcam feed
cap = cv2.VideoCapture(0) #"Resources/running.mp4"
cap.set(3,640)
cap.set(4,480)
cap.set(10,200)

while True:
    success, frame = cap.read()
    if success:
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Video capture is " + success)
        break
#-------------------------------------------------