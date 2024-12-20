from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton

class ChatTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)

        # Input area
        input_layout = QHBoxLayout()
        self.chat_input = QLineEdit()
        self.chat_input.setPlaceholderText("Type your command...")
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_command)
        input_layout.addWidget(self.chat_input)
        input_layout.addWidget(send_button)
        layout.addLayout(input_layout)

        self.setLayout(layout)

    def send_command(self):
        command = self.chat_input.text().strip()
        if command:
            self.chat_display.append(f"You: {command}")
            # Placeholder for response
            self.chat_display.append("Assistant: Processing your request...")
            self.chat_input.clear()
