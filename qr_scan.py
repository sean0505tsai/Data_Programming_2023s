import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Create a video capture object
cap = cv2.VideoCapture(0)

# Loop over frames from the video stream
while True:
    # Capture a frame
    ret, frame = cap.read()

    # If the frame was not captured, exit the loop
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes in the grayscale image
    decoded_objects = decode(gray)

    # Loop over all detected QR codes
    for obj in decoded_objects:
        # Print the QR code data
        print("Data:", obj.data.decode())

        # Draw a rectangle around the QR code
        rect = obj.rect
        cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 255, 0), 3)

    # Display the frame with the detected QR codes
    cv2.imshow("QR Code Scanner", frame)

    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
