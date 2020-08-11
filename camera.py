import time
import cv2

class Camera:
    def __init__(self):
        self.vs = cv2.VideoCapture()
        self.detections = 0

        # Let camera warm up for 5 seconds.
        print("Starting camera...")
        time.sleep(5)

    def __del__(self):
        self.vs.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        readFrame = self.vs.grab()

        # Return bytes of frame.
        buf = cv2.imencode('.jpg', readFrame)[1].tostring()
        return buf