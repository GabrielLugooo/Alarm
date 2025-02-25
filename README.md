<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# WORM

<a href="https://github.com/GabrielLugooo/Alarm" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Alarm-000000" alt="English Alarm" /></a>
<a href="https://github.com/GabrielLugooo/Alarm/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Alarm-green" alt="Spanish Alarm" /></a>

### Objective

This project aims to provide a simple and effective alarm in Python with a graphical interface using PySide6.

Users can set a timer in minutes and seconds through an intuitive interface with spin boxes. Once the set time expires, the alarm plays an audio file and displays a popup notification.

Additionally, the project helps improve the understanding of time management in Python, the creation of modern graphical interfaces, and interacting with the file system to dynamically obtain file paths.

### Skills Learned

1. Time handling using the `time` library.
2. Using `playsound` to play audio files.
3. File system interaction via `os.path`.
4. Creating graphical interfaces with `PySide6`.
5. Implementing popup notifications in desktop applications.
6. Capturing user input with interactive widgets (spin boxes and buttons).
7. Data type conversion (`int` for minutes and seconds).
8. Creating functions in Python.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python
- `time` library
- `playsound` library
- `os` library
- `PySide6` for the graphical interface
- PySide6 notification system

### Project

#### Preview

<img align="center" src="https://i.imgur.com/o080jKM.jpeg" alt="Alarm1" />
<img align="center" src="https://i.imgur.com/Ws12WOW.jpeg" alt="Alarm2" />

#### Code with Comments (English)

```python
#Alarm

# Install pip install PySide6
# Import the necessary libraries from PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QSystemTrayIcon
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QIcon
import os # Import the os library
import sys # Import the sys library

class AlarmApp(QWidget):
def __init__(self):
""" Initializes the graphical interface of the alarm """
super().__init__()

# Configuration of the main window
self.setWindowTitle("Alarm")
self.setGeometry(100, 100, 300, 200)

# Main layout
layout = QVBoxLayout()

# Label for user input
self.label = QLabel("Select alarm time:")
layout.addWidget(self.label)

# SpinBox for selecting minutes
self.min_spin = QSpinBox()
self.min_spin.setRange(0, 59)
self.min_spin.setSuffix(" min")
layout.addWidget(self.min_spin)

# SpinBox for selecting seconds
self.sec_spin = QSpinBox()
self.sec_spin.setRange(0, 59)
self.sec_spin.setSuffix(" sec")
layout.addWidget(self.sec_spin)

# Button for starting the alarm
self.start_button = QPushButton("Start Alarm")
 self.start_button.clicked.connect(self.start_alarm)
 layout.addWidget(self.start_button)

 # Configure the layout in the main window
 self.setLayout(layout)

 # Initialize the timer
 self.timer = QTimer(self)
 self.timer.timeout.connect(self.trigger_alarm)

 # Initialize media player
 self.player = QMediaPlayer(self)
 self.audio_output = QAudioOutput(self)
 self.player.setAudioOutput(self.audio_output)

 # Create system tray icon
 self.tray_icon = QSystemTrayIcon(self)
 icon_path = os.path.join(os.path.dirname(__file__), "icon.png") # Make sure "icon.png" exists
self.tray_icon.setIcon(QIcon(icon_path))
self.tray_icon.setVisible(True) # Make the icon visible in the tray

def start_alarm(self):
""" Start the countdown for the alarm """
minutes = self.min_spin.value()
seconds = self.sec_spin.value()
total_milliseconds = (minutes * 60 + seconds) * 1000

# Start the timer with the set time
self.timer.start(total_milliseconds)
self.label.setText(f"The alarm will sound in {minutes} min and {seconds} sec.")

def trigger_alarm(self):
""" Stop the timer and trigger the alarm when the time is up """
self.timer.stop() # Stop the timer
sound_path = os.path.join(os.path.dirname(__file__), "alarma_python.mp3")

# Play sound using QMediaPlayer
self.player.setSource(QUrl.fromLocalFile(sound_path))
self.audio_output.setVolume(1.0)
self.player.play()

self.show_notification() # Show popup notification

def show_notification(self):
""" Show a popup notification when the alarm sounds """
self.tray_icon.showMessage("Alarm", "It's time! The alarm has sounded.", QSystemTrayIcon.Information, 3000)

if __name__ == "__main__":
# Create the Qt application
app = QApplication(sys.argv)
window = AlarmApp()
window.show()
sys.exit(app.exec())
```

### Limitations

Alarm it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
