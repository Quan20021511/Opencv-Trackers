# Object Tracking with OpenCV

This project demonstrates object tracking using OpenCV, allowing you to select objects in a video stream and track their positions using different tracking algorithms.

<div align="center">
  <img src="https://github.com/Quan20021511/Digital_Clock/assets/129273695/07794c2d-b664-4a74-8365-38afcce1ddcb" width="400" alt="Object Tracking GIF 1">
  <img src="https://github.com/Quan20021511/Digital_Clock/assets/129273695/1c306dba-459c-41b4-bb8b-650614f42aa3" width="400" alt="Object Tracking GIF 2">
</div>


## Features

- **Multiple Tracking Algorithms:** Choose from various tracking algorithms including CSRT, KCF, Boosting, MIL, TLD, MedianFlow, and MOSSE.
- **User-Friendly Interface:** Select objects to track interactively by drawing bounding boxes on the video frame.
- **Results Logging:** Save tracked object positions to text files for further analysis.

## Prerequisites

Before running the code, ensure you have the following:
- [OpenCV](https://opencv.org/) (Open Source Computer Vision Library) installed.
- You can install these dependencies using pip:

```shell

pip install opencv-python numpy

```
- A video file for tracking (replace `"YOUR VIDEO PATH"` in the code with the actual video file path).

## Usage

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the repository's directory.

3. Run the Python script using the following command:

``` shell
python object_tracking.py

```

5. Follow the on-screen instructions to select objects for tracking and choose the tracking algorithm.

6. The script will display the video stream with tracked objects, and the tracking results will be saved to text files in the specified directory (replace `"YOUR RESULTS FILE PATH"` in the code with the desired directory path).

7. To exit the tracking application, press the 'q' key.

## Code Structure

- `object_tracking.py`: The main Python script for object tracking.
- `tracker_types`: A dictionary mapping tracker types to OpenCV tracker constructors.
- Other relevant code sections: Object selection, tracker initialization, frame processing, and results logging.

## Contributing

Contributions to this project are welcome! If you have suggestions for improvements or additional features, please create a pull request.

## Author

- [Nguyen Duc Quan](https://github.com/yourusername)

Enjoy object tracking with OpenCV!
