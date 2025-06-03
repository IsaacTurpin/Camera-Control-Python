# Camera-Control-Python
A program to connect to a camera and take photos at designated intervals, saving each file in a location of the users' choosing. Saved files will be named as the exact time the photo was taken, to the ms.

## How to run
* Press the run button in your selected IDE on the file named "main.py"
* Press the 'Select Folder' button and choose a location to save your images. (Please note you will not be able to press start until a folder is selected, a message box will appear to remind you of this if you try to press start before selecting a folder)
* Select your connected camera from the "Select Camera" dropdown, all connected cameras will show up here, so ensure you pick the correct one. (Please note you will not be able to press start until a camera is selected, a message box will appear to remind you of this if you try to press start before selecting a camera)
* Set your 'Time Delay' using the spinbox. This delay counts down in seconds. If you want a 5 second delay upon pressing the start button before images are captured and saved, set this number to 5. If you do not want any delay, set the number to 0.
* Press the button labelled 'Start' to begin capturing and saving images. A countdown timer from your specified 'Time Delay' will appear, counting down and displaying a message once acquisition has begun.
* Press the 'Stop' button when you wish to stop capturing and saving. You can then start again with the corresponding button to capture with the same settings.
* Optional - Press the 'Customise' button to change the background colour of the UI.
