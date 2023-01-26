import cv2
import numpy as np
url = "Your IP Address"
cp = cv2.VideoCapture(url)

while True:
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitkey(1)

    if q == ord("q")
    break
cv2.destroyAllWindows()
