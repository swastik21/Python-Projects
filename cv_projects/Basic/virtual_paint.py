import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#widht id:3, height id:4, brightness id:10.
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

mycolors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]
mycolorvalues= [[51,152,255],
                [255,0,255],
                [0,255,0]]

mypoints = [] #[x,y,colorid]
def findColor(img,myColor,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in myColor:
        lowerb = np.array(color[0:3])
        upperb = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lowerb, upperb)
        x,y = contour(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newpoints

def drawOnCanvas(myPoints,myColorValues):
    for pt in myPoints:
        cv2.circle(imgResult,(pt[0],pt[1]),10,myColorValues[pt[2]],cv2.FILLED)


def contour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y
            

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findColor(img,mycolors,mycolorvalues)
    if len(newpoints) !=0:
        for pt in newpoints:
            mypoints.append(pt)
    if len(mypoints) !=0:
        drawOnCanvas(mypoints,mycolorvalues)
    cv2.imshow('video', imgResult)
    if cv2.waitKey(1) & 0xFF == 27:
        break
