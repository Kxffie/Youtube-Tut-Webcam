import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('username.png', cv2.IMREAD_UNCHANGED)

segmentor = SelfiSegmentation()

maxThreshold = 1
thresholdNormal = 0.5
minThreshold = 0

green = (0,255,0)
blue = (255,0,0)
setColor = green

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, (0, 255, 0), threshold=thresholdNormal)
    
    gray_scale = cv2.cvtColor(imgOut, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        overlay_resize = cv2.resize(overlay, (w, 50))
        imgOut = cvzone.overlayPNG(imgOut, overlay_resize, (x, y - 120))
    
    cv2.imshow("Video", imgOut)
    key = cv2.waitKeyEx(1)
    
    if key == 2424832:
        if thresholdNormal > minThreshold:
            thresholdNormal -= 0.05
    elif key == 2555904:
        if thresholdNormal < maxThreshold:
            thresholdNormal += 0.05
    elif key == 2490368:
        if setColor == green:
            setColor = blue
        else:
            setColor = green
    elif key == 27:
        break