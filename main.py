import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from utils.signal_handler import signal_handler

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Handle signal interruptions (e.g., Ctrl+C)
    def handle_exit():
        print("Shutting down gracefully...")
        sys.exit(0)

    signal_handler.recording_stopped.connect(handle_exit)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
