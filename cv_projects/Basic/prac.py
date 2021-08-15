import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix


# img = cv2.imread('lena.png')
# cv2.imshow('Output',img)
# cv2.waitKey(0)



#for importing and displaying video

#cap = cv2.VideoCapture('test.mp4')
# while True:
#     success, img = cap.read()
#     cv2.imshow('video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


#for importing and displaying video from webcam

# cap = cv2.VideoCapture(0)
# widht id:3, height id:4, brightness id:10.
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
# while True:
#     success, img = cap.read()
#     imgcanny = cv2.Canny(img,90,90)
#     cv2.imshow('video', img)
#     cv2.imshow('Canny video', imgcanny)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



#functions of cv2

# img = cv2.imread('lena.png')
# kernel = np.ones((2,2),np.uint8)

# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray,(7,7),0)
# imgcanny = cv2.Canny(img,120,120)
# imgdilation = cv2.dilate(imgcanny,kernel,iterations=1)
# imgeroded = cv2.erode(imgdilation,kernel,iterations=1)

#cv2.imshow('Gray image',imggray)
#cv2.imshow('Blur image',imgblur)
#cv2.imshow('Canny image',imgcanny)
# cv2.imshow('Dilated image',imgdilation)
# cv2.imshow('Eroded image',imgeroded)
# cv2.waitKey(0)


#crop and resize

# img = cv2.imread('lambo.png')

# print(img.shape)

# imageresize = cv2.resize(img,(300,200))
# imagecrop = img[0:200,300:500]
# cv2.imshow('image',img)
# cv2.imshow('cropped image',imagecrop)
#cv2.imshow('resized image',imageresize)
# cv2.waitKey(0)



#shapes and text

# img = np.ones((512,512,3),np.uint8)

# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,300),(0,0,255),2)
# cv2.circle(img,(400,50),30,(255,255,0),2)

# cv2.putText(img,'SHapes and text',(300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),1)

# cv2.imshow('Image',img)
# cv2.waitKey(0)


#warp perspective 

# img = cv2.imread('cards.jpg')

# width, height = 250,350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgout = cv2.warpPerspective(img,matrix,(width,height))


# cv2.imshow('Image',img)
# cv2.imshow('Warp Image',imgout)
# cv2.waitKey(0)


#color detection

# def empty(a):
#     pass

# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
#                                                 None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank] * rows
#         hor_con = [imageBlank] * rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver

# cv2.namedWindow('TrackBars')
# cv2.resizeWindow('TrackBars',640,240)
# cv2.createTrackbar('Hue Min','TrackBars',0,179,empty)
# cv2.createTrackbar('Hue Max','TrackBars',179,179,empty)
# cv2.createTrackbar('Sat Min','TrackBars',0,255,empty)
# cv2.createTrackbar('Sat Max','TrackBars',255,255,empty)
# cv2.createTrackbar('Val Min','TrackBars',0,255,empty)
# cv2.createTrackbar('Val Max','TrackBars',255,255,empty)

# while True:
#     img = cv2.imread('lambo.png')

#     imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
#     h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
#     s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
#     s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
#     v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
#     v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
#     print(h_min,h_max,s_min,s_max,v_min,v_max)
#     lowerb = np.array([h_min,s_min,v_min])
#     upperb = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV, lowerb, upperb)
#     result = cv2.bitwise_and(img,img,mask=mask)

    # cv2.imshow('Original',img)
    # cv2.imshow('HSV',imgHSV)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('Result',result)

    # output = stackImages(0.6,([img,imgHSV],[mask,result]))
    # cv2.imshow('Color Extraction',output)

    # cv2.waitKey(1)



#shape detection

# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
#                                                 None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank] * rows
#         hor_con = [imageBlank] * rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#         ver = np.vstack(hor)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor = np.hstack(imgArray)
#         ver = hor
#     return ver

# def contour(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if area > 500:
#             cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
#             peri = cv2.arcLength(cnt,True)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             print(len(approx))
#             objCor = len(approx)
#             x,y,w,h = cv2.boundingRect(approx)
#             cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
#             if objCor == 3: objectType = 'Tri'
#             elif objCor == 4:
#                 aspRatio = w/float(h)
#                 if aspRatio > 0.95 and aspRatio < 1.05: objectType = 'Sqr'
#                 else: objectType = 'rect'
#             elif objCor > 4: objectType = 'Circle'
#             else: objectType = 'None'
#             cv2.putText(imgcontour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

# img = cv2.imread('shapes.png')
# imgcontour = img.copy()
# imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgblur = cv2.GaussianBlur(imggray,(7,7),1)
# imgcanny = cv2.Canny(imgblur,50,50)

# contour(imgcanny)

# imgblank = np.zeros_like(img)
# stack = stackImages(0.6,([img,imggray,imgblur],[imgcanny,imgcontour,imgblank]))
# cv2.imshow('Stack',stack)
# cv2.waitKey(0)



#face detection

# faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#     for (x,y,w,h) in faces:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         cv2.putText(img,'Face',(x+(w//2)-80,y+(h//2)+105),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#     cv2.imshow('Video',img)
#     if cv2.waitKey(1) and 0xFF == 27:
#         break