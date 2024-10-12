import cv2 as cv

video=cv.VideoCapture(0)
subtractor=cv.createBackgroundSubtractorMOG2(250,30)

while True:
    ret,frame=video.read()

    if ret:

        height, width = frame.shape[:2]                                      #this will resize the window to fit               
        new_width = 640
        new_height = int((new_width / width) * height)
        resized_frame = cv.resize(frame, (new_width, new_height))

        # Apply the background subtractor
        mask = subtractor.apply(resized_frame)

        # mask=subtractor.apply(frame)
        cv.imshow('Resized Frame', resized_frame)
        cv.imshow('Mask',mask)

        if cv.waitKey(5)==ord('q'):                                     #5 is showing the waiting time for each frame of the camera in milisecond
            break
    
video.release()
cv.destroyAllWindows()