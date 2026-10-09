import cv2
from ultralytics import YOLO

# Downloads the pretrained model on the first run.
model = YOLO("yolov8n.pt")

# 0 selects your default webcam.
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not camera.isOpened():
    raise SystemExit("Cannot open webcam. Check your camera permissions.")

print("Camera started. Press Q in the video window to stop.")

try:
    while True:
        success, frame = camera.read()

        if not success:
            print("Cannot read a frame from the webcam.")
            break

        results = model.track(
            frame,
            persist=True,
            tracker="botsort.yaml",
            conf=0.35,
            imgsz=320,
            verbose=False,
        )

        # Draws bounding boxes, object names, confidence and tracking IDs.
        annotated_frame = results[0].plot()

        cv2.imshow("CodeAlpha - Object Detection and Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    camera.release()
    cv2.destroyAllWindows()