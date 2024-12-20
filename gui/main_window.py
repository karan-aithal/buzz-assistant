from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from gui.button_handler import ButtonHandler
from gui.settings_dialog import SettingsDialog
from utils.signal_handler import signal_handler

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Desktop Assistant")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Notification Area
        self.notification_label = QLabel("Welcome to AI Desktop Assistant!")
        self.layout.addWidget(self.notification_label)

        # Add buttons
        self.record_button = QPushButton("Toggle Recording")
        self.settings_button = QPushButton("Open Settings")
        self.layout.addWidget(self.record_button)
        self.layout.addWidget(self.settings_button)

        # Button actions
        self.button_handler = ButtonHandler(self)
        self.record_button.clicked.connect(self.button_handler.toggle_recording)
        self.settings_button.clicked.connect(self.open_settings)

        # Connect notification signal
        signal_handler.notification.connect(self.update_notification)

    def open_settings(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.exec_()

    def update_notification(self, message):
        """Updates the notification label with a new message."""
        self.notification_label.setText(message)
