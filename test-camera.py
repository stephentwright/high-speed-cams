import cv2
from picamera2 import Picamera2

#set up the camera (this will need to be done several times)
cam=Picamera2()
cam.preview_configuration.main.size=(640,360)
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

while True:
    frame = cam.capture_array()
    cv2.imshow("cam",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()





