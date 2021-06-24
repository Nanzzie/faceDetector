import cv2

faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#img = cv2.imread('resources/faces.jpg')
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayImg, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('webcam:', img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
