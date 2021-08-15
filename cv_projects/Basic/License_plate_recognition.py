import cv2
import numpy as np
import os 

os.chdir('C://Users//swastik//Desktop//python_project//cv_projects')

numberPlateCascade = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
minArea = 200
count = 0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = numberPlateCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
            cv2.putText(img,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
            plateimg = img[y:y+h,x:x+w]
            cv2.imshow("Number Plate",plateimg)

    cv2.imshow('Video',img)
    if cv2.waitKey(1) and 0xFF == ord('s'):
        cv2.imwrite('License Plate'+str(count)+'.jpg',plateimg)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,'Scan Saved',(150,265),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('Result',img)
        cv2.waitKey(500)
        count +=1
        