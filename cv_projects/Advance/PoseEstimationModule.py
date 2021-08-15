import  cv2
import mediapipe as mp

cap = cv2.VideoCapture("C:/Users/swastik/Desktop/python_project/cv_projects/Advance/PoseVideos1.mp4")
while True:
    success , img = cap.read()
    cv2.imshow('video',img)
    cv2.waitKey(1)