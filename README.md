# CodeAlpha Object Detection and Tracking

Task 4 of my Artificial Intelligence internship at CodeAlpha.

This Python project detects objects from a live webcam using a pretrained YOLOv8 model and tracks them across frames using BoT-SORT.

## Features

- Live webcam input through OpenCV
- Object detection using YOLOv8 Nano
- Bounding boxes, object labels and confidence scores
- Tracking IDs for detected objects
- Press Q in the video window to stop

## Technologies

Python, Ultralytics YOLO, OpenCV and BoT-SORT.

## Setup and Run

Open PowerShell in the project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe tracking.py
```

The pretrained model downloads automatically on the first run.
An internet connection is required for that download.

Close other applications using the webcam before running.
Click the video window and press Q to exit.

## How It Works

1. OpenCV captures webcam frames.
2. YOLO detects supported object categories in each frame.
3. BoT-SORT associates detections across frames and assigns tracking IDs.
4. The program displays the annotated frames.

## Task 4 Requirements Covered

- Webcam input using OpenCV
- Pretrained object detection model
- Bounding boxes around detected objects
- Multi-object tracking
- Live output with labels and tracking IDs

## Limitations

Performance depends on the computer, lighting and camera quality.
Tracking IDs can change if an object leaves the frame or tracking is lost.
The model detects its pretrained categories and cannot recognise every object.