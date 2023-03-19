import numpy as np
import cv2

casc_class = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(casc_class)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera, dumb ass bitch")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive camera, retard boy")
        break
   
    # Frame operations come from below
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  

    # Display the resulting frame
    cv2.imshow('frame', frame)
    #quit on q
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
