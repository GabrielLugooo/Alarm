<img align="center" src="https://i.imgur.com/ZgHWFhw.png" alt="gabriellugo" />

# ALARMA

<a href="https://github.com/GabrielLugooo/Alarm/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Alarma%20Español-000000" alt="Alarma Español" /></a>
<a href="https://github.com/GabrielLugooo/Alarm" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Alarma%20Inglés-green" alt="Alarma Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo proporcionar una alarma sencilla y efectiva en Python con una interfaz gráfica utilizando PySide6.

Los usuarios pueden configurar un temporizador en minutos y segundos mediante una interfaz intuitiva con spin boxes. Una vez que el tiempo establecido se agota, la alarma reproduce un archivo de audio y muestra una notificación emergente.

Además, el proyecto busca mejorar la comprensión del manejo del tiempo en Python, la creación de interfaces gráficas modernas y la interacción con el sistema de archivos para obtener rutas de archivos de manera dinámica.

### Habilidades Aprendidas

1. Manejo del tiempo con la biblioteca `time`.
2. Uso de `playsound` para reproducir archivos de audio.
3. Interacción con el sistema de archivos mediante `os.path`.
4. Creación de interfaces gráficas con `PySide6`.
5. Implementación de notificaciones emergentes en aplicaciones de escritorio.
6. Captura de entrada del usuario con widgets interactivos (spin boxes y botones).
7. Conversión de datos entre tipos (`int` para minutos y segundos).
8. Creación de funciones en Python.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/PySide6-000000?logo=pyside6&logoSize=auto)
![Static Badge](https://img.shields.io/badge/time-000000?logo=time&logoSize=auto)
![Static Badge](https://img.shields.io/badge/playsound-000000?logo=playsound&logoSize=auto)
![Static Badge](https://img.shields.io/badge/os-000000?logo=os&logoSize=auto)

- Python
- Biblioteca `time`
- Biblioteca `playsound`
- Biblioteca `os`
- `PySide6` para la interfaz gráfica
- Sistema de notificaciones de PySide6

### Proyecto

#### Vista Previa

<img align="center" src="https://i.imgur.com/o080jKM.jpeg" alt="Alarm1" />
<img align="center" src="https://i.imgur.com/Ws12WOW.jpeg" alt="Alarm2" />

#### Código con Comentarios (Español)

```python
#Alarm

# Intalar pip install PySide6
# Importamos las librerías necesarias de PySide6
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton, QSystemTrayIcon
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtGui import QIcon
import os # Importamos la librería os
import sys # Importamos la librería sys

class AlarmApp(QWidget):
    def __init__(self):
        """ Inicializa la interfaz gráfica de la alarma """
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Alarm")
        self.setGeometry(100, 100, 300, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Etiqueta para la indicación del usuario
        self.label = QLabel("Selecciona el tiempo de la alarma:")
        layout.addWidget(self.label)

        # SpinBox para seleccionar minutos
        self.min_spin = QSpinBox()
        self.min_spin.setRange(0, 59)
        self.min_spin.setSuffix(" min")
        layout.addWidget(self.min_spin)

        # SpinBox para seleccionar segundos
        self.sec_spin = QSpinBox()
        self.sec_spin.setRange(0, 59)
        self.sec_spin.setSuffix(" sec")
        layout.addWidget(self.sec_spin)

        # Botón para iniciar la alarma
        self.start_button = QPushButton("Iniciar Alarma")
        self.start_button.clicked.connect(self.start_alarm)
        layout.addWidget(self.start_button)

        # Configurar el layout en la ventana principal
        self.setLayout(layout)

        # Inicializar el temporizador
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.trigger_alarm)

        # Inicializar reproductor multimedia
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)

        # Crear el icono de la bandeja del sistema
        self.tray_icon = QSystemTrayIcon(self)
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")  # Asegurate de que "icon.png" existe
        self.tray_icon.setIcon(QIcon(icon_path))
        self.tray_icon.setVisible(True)  # Hacer que el ícono sea visible en la bandeja

    def start_alarm(self):
        """ Inicia la cuenta regresiva para la alarma """
        minutes = self.min_spin.value()
        seconds = self.sec_spin.value()
        total_milliseconds = (minutes * 60 + seconds) * 1000

        # Iniciar el temporizador con el tiempo establecido
        self.timer.start(total_milliseconds)
        self.label.setText(f"La alarma sonará en {minutes} min y {seconds} sec.")

    def trigger_alarm(self):
        """ Detiene el temporizador y activa la alarma cuando el tiempo se cumple """
        self.timer.stop()  # Detener el temporizador
        sound_path = os.path.join(os.path.dirname(__file__), "alarma_python.mp3")

        # Reproducir sonido usando QMediaPlayer
        self.player.setSource(QUrl.fromLocalFile(sound_path))
        self.audio_output.setVolume(1.0)
        self.player.play()

        self.show_notification()  # Mostrar notificación emergente

    def show_notification(self):
        """ Muestra una notificación emergente cuando suena la alarma """
        self.tray_icon.showMessage("Alarma", "¡Es hora! La alarma ha sonado.", QSystemTrayIcon.Information, 3000)

if __name__ == "__main__":
    # Crear la aplicación Qt
    app = QApplication(sys.argv)
    window = AlarmApp()
    window.show()
    sys.exit(app.exec())
```

### Limitaciones

La Alarma es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
