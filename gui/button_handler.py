from PyQt5.QtCore import QObject
from gui.recorder import AudioRecorder
from utils.signal_handler import signal_handler
import threading
import pyautogui

class ButtonHandler(QObject):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.audio_recorder = AudioRecorder()

        self.recording_thread = None

    def toggle_recording(self):
        self.audio_recorder.toggle_recording()

    # def start_recording(self):
    #     print("Starting recording...")
    #     self.recording = True
    #     signal_handler.recording_started.emit()

    #     self.recording_thread = threading.Thread(target=self.mock_recording)
    #     self.recording_thread.start()

    # def stop_recording(self):
    #     print("Stopping recording...")
    #     self.recording = False
    #     signal_handler.recording_stopped.emit()

    # def mock_recording(self):
    #     while self.recording:
    #         pyautogui.screenshot().save("screenshot.png")
