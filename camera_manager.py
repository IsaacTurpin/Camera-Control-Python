import cv2

class CameraManager:
    def __init__(self):
        self.available_cameras = self.detect_cameras()
        self.selected_camera_index = None
        self.camera = None

    def detect_cameras(self, max_cameras=5):
        cameras = []
        for i in range(max_cameras):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"Camera {i} detected.")
                cameras.append(i)
                cap.release()
        return cameras

    def select_camera(self, index):
        if self.camera:
            self.camera.release()
        self.selected_camera_index = index
        self.camera = cv2.VideoCapture(index)

    def get_camera(self):
        return self.camera