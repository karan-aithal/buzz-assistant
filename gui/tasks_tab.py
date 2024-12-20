from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
import pyautogui

class TasksTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        open_browser_button = QPushButton("Open Browser")
        open_browser_button.clicked.connect(self.open_browser)
        layout.addWidget(open_browser_button)

        self.setLayout(layout)

    def open_browser(self):
        try:
            pyautogui.hotkey("ctrl", "t")  # Example of browser interaction
            print("Opened a new browser tab.")
        except Exception as e:
            print(f"Error opening browser: {e}")
