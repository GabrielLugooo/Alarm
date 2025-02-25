
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
