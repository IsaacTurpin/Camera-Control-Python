from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Style
from camera_manager import CameraManager


class Gui:
    def __init__(self):
        self.window = Tk()
        self.camera_manager = CameraManager()

        style = Style(self.window)
        style.configure('Custom.TMenubutton', font=('Consolas', 15), foreground='black')

        self.folder = None
        self.camera = None

        self.frame = Frame(self.window, bg="black", bd=5, relief=SUNKEN)
        self.frame.pack()

        self.select_folder_button = Button(self.frame, text="Select Folder", font=("Consolas", 25), width=15, command=self.select_folder)
        self.select_folder_button.pack(padx=10, pady=10)

        self.dropdown_label = Label(self.frame, text="Select Camera", font=("Consolas", 25), fg="white", bg="black")
        self.dropdown_label.pack()

        camera_options = self.camera_manager.available_cameras
        default_text = "Select Camera"
        self.camera_var = StringVar(value=default_text)
        self.camera_dropdown = ttk.OptionMenu(
            self.frame, self.camera_var, default_text, *camera_options, command=self.on_camera_selected, style='Custom.TMenubutton'
        )
        self.camera_dropdown.pack(padx=10, pady=10)

        self.start_button = Button(self.frame, text="Start", font=("Consolas", 25), width=15, command=self.on_start)
        self.start_button.pack(padx=10, pady=10)

        self.stop_button = Button(self.frame, text="Stop", font=("Consolas", 25), width=15, command=self.on_stop)
        self.stop_button.pack(padx=10, pady=10)

        self.window.mainloop()

    def select_folder(self):
        self.folder = filedialog.askdirectory(initialdir="C:\\", title="Select Folder")
        if self.folder:
            print(f"Selected folder: {self.folder}")
        else:
            print("No folder selected")

    def on_camera_selected(self, selected_camera):
        self.camera_manager.select_camera(int(selected_camera))
        print(f"Selected camera: {selected_camera}")

    def on_start(self):
        pass

    def on_stop(self):
        pass

# To run the GUI
if __name__ == "__main__":
    Gui()


