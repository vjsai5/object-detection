from ultralytics import YOLO
import cv2
import threading


detector = YOLO("yolov8n.pt")


camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

current_frame = None
is_running = True


seen_ids = set()
object_total = 0


def read_camera():
    global current_frame, is_running
    while is_running:
        success, img = camera.read()
        if success:
            current_frame = img.copy()



threading.Thread(target=read_camera, daemon=True).start()


while True:
    if current_frame is None:
        continue

    
    display_frame = cv2.resize(current_frame, (640, 480))

   
    output = detector.track(display_frame, persist=True, conf=0.5, verbose=False)[0]

    
    result_frame = output.plot()

    if output.boxes is not None and output.boxes.id is not None:
        track_ids = output.boxes.id.int().tolist()
        categories = output.boxes.cls.int().tolist()

        for track_id, category in zip(track_ids, categories):
            name = detector.names[category]

            # Count only new objects
            if track_id not in seen_ids:
                seen_ids.add(track_id)
                object_total += 1

    
    cv2.putText(result_frame,
                f"Objects counted: {object_total}",
                (10, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (50, 50, 255),
                2)

    cv2.imshow("Live Tracking Counter", result_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        is_running = False
        break
    elif key == ord('r'):
        seen_ids.clear()
        object_total = 0


camera.release()
cv2.destroyAllWindows()
