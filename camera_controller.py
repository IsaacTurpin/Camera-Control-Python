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
        thresholds = [(6, 0.5), (5, 0.3), (1, 0.1), (0, 0.1)]  # (elapsed_time, interval)
        interval = 0.1  # Capture every 100 milliseconds
        elapsed_time = 0
        start_time = time.time()
        while self.running:
            frame = self.capture_frame()
            if frame is not None:
                self.process_file(folder, frame)

            time.sleep(interval)
            elapsed_time = time.time() - start_time

            for threshold, new_interval in thresholds:
                if elapsed_time > threshold:
                    interval = new_interval
                    break

    def stop_timed_capture(self):
        self.running = False
        if self.capture_thread:
            self.capture_thread.join()

    def process_file(self, folder, frame):
        now = time.localtime()
        ms = int((time.time() % 1) * 1000)
        filename = (f"{now.tm_hour:02d}h{now.tm_min:02d}m{now.tm_sec:02d}s{ms:02d}ms "
                    f"{now.tm_mday:02d}{now.tm_mon:02d}{now.tm_year}.jpg")
        filepath = os.path.join(folder, filename)
        cv2.imwrite(filepath, frame)


