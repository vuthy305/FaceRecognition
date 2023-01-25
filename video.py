# import the opencv library
import cv2 as cv
import pipeline

def openCamera():

    # Declare variabe haar to stor the method haar to detect object (face)
    haar = cv.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
   
    # define a video capture object
    vid = cv.VideoCapture(0)
    # vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while(True):
        # Declare font for use
        font = cv.FONT_HERSHEY_SIMPLEX
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        # Convert frame to grayscale 
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Get the faces coordinate
        faces = haar.detectMultiScale(gray,1.3,5)
        # Loop Through face coordinate
        for x,y,w,h in faces:
            # Draw rectangle on face
            cv.rectangle(frame, (x,y), (x+w,y+h), (240,32,160),3)
        # Put text on the frame to show user about click q to quit the video detection
        cv.putText(frame, 'Please click on "q" to quit this video detection.', (10, 20), font, 0.5, (0, 255, 255), 1, cv.LINE_4)
        # Display the resulting frame
        cv.imshow('frame', frame)
        # Make the frame in the X = 350 , Y = 110
        cv.moveWindow('frame', 350 , 110)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv.waitKey(100) & 0xFF == ord('q') :
            break
  
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv.destroyAllWindows()
def takePhoto(fol_name,uname):
    # Declare variabe haar to stor the method haar to detect object (face)
    haar = cv.CascadeClassifier('Haarcascade/haarcascade_frontalface_default.xml')
   
    # Declare video count variable
    img = 0
    # define a video capture object
    vid = cv.VideoCapture(0)
    # vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    while(True):
        # Declare font for use
        font = cv.FONT_HERSHEY_SIMPLEX
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        # Convert frame to grayscale 
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Get the faces coordinate
        faces = haar.detectMultiScale(gray,1.3,5)
        # Loop Through face coordinate
        for x,y,w,h in faces:
            # Draw rectangle on face
            crop_face = gray[y:y+h,x:x+w]
            crop_face = cv.resize(crop_face, (100,100),cv.INTER_AREA)
            cv.rectangle(frame, (x,y), (x+w,y+h), (255,255,0),3)
            if img < 50:
                cv.imwrite(f"./Facedatabase/{fol_name}/{uname}"+str(img)+".jpg", crop_face)
            img+=1
        # Put text on the frame to show user about click q to quit the video detection
        cv.putText(frame, f"{img}", (10, 20), font, 1, (255, 255, 255), 2, cv.LINE_4)
        # Display the resulting frame
        cv.imshow('frame', frame)
        # Make the frame in the X = 350 , Y = 110
        cv.moveWindow('frame', 350 , 110)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv.waitKey(100) & 0xFF == ord('q') or img == 50:
            break
  
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv.destroyAllWindows()
    return True
def getAttendance():
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read() # bgr
        
        if ret == False:
            break
        
        # frame = np.array(frame)
        frame = pipeline.pipeline_model(frame,color='bgr')
        
        cv.imshow('Attendance',frame)
        if cv.waitKey(100) & 0xFF == ord('q'): # press q to exit  --#esc key (27), 
            break
            
    cv.destroyAllWindows()
    cap.release()