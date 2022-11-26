import cv2
import sys
  
# define a video capture object, replace port number with video path to play video
vid = cv2.VideoCapture(0)

# For saving video feed uncomment below
# Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# Check if camera is available at port
if not vid.isOpened():
    print("Camera not detected")

else:
    print("Camera Detected")
    while(True):
        
        # Capture the video frame-by-frame and check if it is returned properly (ret True)
        ret, frame = vid.read()

        if ret is False:
            print("Frame not returned properly. Exiting ....")
            break

        else:
        # Display the resulting frame after desired filtration
            filter = cv2.cvtColor(frame,5)
            cv2.imshow('Live Feed', frame)
        
        # Press "q" to end the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()