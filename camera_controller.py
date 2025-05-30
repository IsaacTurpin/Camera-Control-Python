import os

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

    def start_timed_capture(self, folder):
        self.running = True
        self.capture_thread = threading.Thread(target=self._timed_capture, args=(folder,))
        self.capture_thread.start()

    def _timed_capture(self, folder):
        interval = 0.1  # Capture every 100 milliseconds
        elapsed_time = 0
        start_time = time.time()
        while self.running:
            frame = self.capture_frame()
            if frame is not None:
                # Process the frame (e.g., save it, display it, etc.)
                self.process_file(folder, frame)
                print("Frame captured at", time.time())
            time.sleep(interval)
            elapsed_time = time.time() - start_time
            if elapsed_time > 1:
                interval = 0.1
            if elapsed_time > 2:
                interval = 0.2
            if elapsed_time > 3:
                interval = 0.3
            if elapsed_time > 5:
                interval = 0.5

    def stop_timed_capture(self):
        self.running = False
        if self.capture_thread:
            self.capture_thread.join()

    def process_file(self, folder, frame):
        timestamp = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        ms = int((time.time() % 1) * 1000)
        filename = f"{timestamp}_{ms:03d}.jpg"
        filepath = os.path.join(folder, filename)
        cv2.imwrite(filepath, frame)
        print(f"Saved: {filepath}")


