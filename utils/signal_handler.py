from PyQt5.QtCore import pyqtSignal, QObject

class SignalHandler(QObject):
    recording_started = pyqtSignal()
    recording_stopped = pyqtSignal()
    notification = pyqtSignal(str)  # Signal for sending notifications

signal_handler = SignalHandler()
