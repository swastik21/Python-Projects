import cv2
import time
import mediapipe as mp
import HandTrackingModule as htm



cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw = False)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow('Video',img)
    cv2.waitKey(1)