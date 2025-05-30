import cv2
import time
import threading

class CameraController:
    def __init__(self, camera_manager):
        self.camera_manager = camera_manager
        self.capture_thread = None
        self.running = False

    def capture_frame(self):
        camera = self.camera_manager.get_camera()
        if camera is not None and camera.isOpened():
            ret, frame = camera.read()
            if ret:
                return frame
            else:
                print("Failed to capture frame.")
                return None
        else:
            print("Camera is not opened.")
            return None

    def start_timed_capture(self, duration=10):
        self.running = True
        self.capture_thread = threading.Thread(target=self._timed_capture, args=(duration,))
        self.capture_thread.start()

    def _timed_capture(self, duration):
        start_time = time.time()
        elapsed_time = 0
        interval = 0.2 # Capture every 200 milliseconds
        while self.running and (time.time() - start_time < duration):
            frame = self.capture_frame()
            if frame is not None:
                # Process the frame (e.g., save it, display it, etc.)
                print("Frame captured at", time.time())
            time.sleep(interval)
            elapsed_time = time.time() - start_time
            if elapsed_time > 1:
                interval = 0.5 # Adjust interval after 1 second to capture less frequently

    def stop_timed_capture(self):
        self.running = False
        if self.capture_thread:
            self.capture_thread.join()


