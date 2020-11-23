from cv2 import cv2
import numpy as np


facecascade = cv2.CascadeClassifier(r"C:\python\pythonProject\opencv\data\haarcascade_frontalface_default.xml")



height = 400
width = 600
livecap = cv2.VideoCapture(0)
livecap.set(3, width)      
livecap.set(4, height)
livecap.set(10, 1000)
while True:
    success, img = livecap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(imgGray,1.1,4)

    for (x, y, w, h)  in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("live cam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break