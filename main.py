# pip install opencv-python
import cv2
capt = cv2.VideoCapture(0)
#checking for webcam validityb
if  capt.isOpened()  == False:
    raise IOError("Webcam can't open")
while True:
    ret, frame = capt.read()
    