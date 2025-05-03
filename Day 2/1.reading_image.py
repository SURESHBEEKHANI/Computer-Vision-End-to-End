import cv2 

## Reading images

# img = cv2.imread("resources/lena.png")
# print(img.shape)
# cv2.imshow("Output", img)
# cv2.waitKey(0)

## reading videos


## reading videos

# Create a VideoCapture object to read from a video file (elon.mp4 in the 'resources' folder)
cap = cv2.VideoCapture("resources/elon.mp4")

# Start an infinite loop to read and display each frame of the video
while True:
    success, img = cap.read()  # Read a frame; 'success' is True if the frame is read correctly

    if not success:
        print("Failed to read frame or end of video reached.")
        break

    print(img.shape)           # Print the dimensions of the current frame (height, width, channels)
    cv2.imshow("Output", img)  # Display the frame in a window titled "Output"
    
    # Wait for 1 millisecond and exit loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()



## reading webcam


# cap = cv2.VideoCapture(0) # 0 is the default webcam
# This line (commented out) also initializes webcam capture, similar to the line below

# Initialize webcam video capture (0 = default system webcam)
cap = cv2.VideoCapture(0)

# Set the width of the video frame to 640 pixels
cap.set(3, 640)

# Set the height of the video frame to 480 pixels
cap.set(4, 480)

# Start an infinite loop to continuously capture frames from the webcam
while True:
    # Capture a single frame from the webcam
    # 'success' is a boolean indicating if the frame was read successfully
    # 'img' contains the image/frame itself
    success, img = cap.read()

    # If reading the frame failed, exit the loop and print an error
    if not success:
        print("Failed to grab frame")
        break

    # Print the dimensions of the image (height, width, number of channels)
    print(img.shape)

    # Show the captured frame in a window named "Output"
    cv2.imshow("Output", img)

    # Wait for 1 millisecond between frames
    # If the 'q' key is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop ends, release the webcam resource
cap.release()

# Close all OpenCV windows that were opened
cv2.destroyAllWindows()


