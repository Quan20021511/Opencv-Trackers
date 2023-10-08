import cv2
import numpy as np

# Create tracker
tracker_types = {
    'csrt': cv2.legacy.TrackerCSRT_create,
    'kcf': cv2.legacy.TrackerKCF_create,
    'boosting': cv2.legacy.TrackerBoosting_create,
    'mil': cv2.legacy.TrackerMIL_create,
    'tld': cv2.legacy.TrackerTLD_create,
    'medianflow': cv2.legacy.TrackerMedianFlow_create,
    'mosse': cv2.legacy.TrackerMOSSE_create
}

trackers = cv2.legacy.MultiTracker_create()

# Load the video
cap = cv2.VideoCapture(r"YOUR VIDEO PATH")

# Check if video capture was successful
if not cap.isOpened():
    print("Error opening video capture")
    exit()

# Read the first frame
ret, frame = cap.read()

# Check if frame was read successfully
if not ret:
    print("Error reading frame from video capture")
    exit()

# List to store selected bounding boxes
selected_bboxes = []

# Select objects to track
num_objects = int(input("How many objects would you like to track? "))
for i in range(num_objects):
    bbox = cv2.selectROI('Frame', frame)
    selected_bboxes.append(bbox)

# Initialize trackers for selected objects
for bbox in selected_bboxes:
    tracker_type = input("Enter tracker type (csrt, kcf, boosting, mil, tld, medianflow, or mosse): ")
    tracker = tracker_types.get(tracker_type)
    if tracker:
        tracker = tracker()
        trackers.add(tracker, frame, bbox)
    else:
        print("Invalid tracker type. Please choose a valid tracker type.")

# Loop through frames
frame_number = 1
font = cv2.FONT_HERSHEY_SIMPLEX
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (int(cap.get(3)), int(cap.get(4))))

base_dir = r'YOUR RESULTS FOLDER PATH'
while True:
    # Read a new frame
    ret, frame = cap.read()

    # If the frame is not available, break the loop
    if not ret:
        break

    # Update tracker
    success, boxes = trackers.update(frame)

    # Save the boxes to a file
    np.savetxt(base_dir + '/frame_' + str(frame_number) + '.txt', boxes, fmt='%f')
    frame_number += 1

    # Draw bounding boxes on the frame
    n_objects = 0
    for box in boxes:
        n_objects += 1
        x, y, w, h = [int(i) for i in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 255, 205), 2)
        cv2.putText(frame, 'Object {}'.format(n_objects), (x, y - 5), font, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the current frame number and the number of tracked objects
    cv2.putText(frame, 'Frame: {}'.format(frame_number), (20, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, 'Tracked objects: {}'.format(n_objects), (20, 60), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the resulting frame and save to video file
    cv2.imshow('Frame', frame)
    out.write(frame)

    # Exit if the key 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
