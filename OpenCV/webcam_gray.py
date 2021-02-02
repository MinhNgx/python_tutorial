#Webcam_gray
import cv2

camera_id = 0
video = cv2.VideoCapture(camera_id) #Open camera

while(True):
    ret, frame = video.read()
    if ret: #If frame is read correctly, it will be True
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Webcam gray image", frame)
    if cv2.waitKey(1) == ord('q'): #Check if press Q then quit
        break
video.release() #Exit video
cv2.destroyAllWindows() #Close windows
