from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox

class LLMSettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LLM Settings")
        self.setLayout(QVBoxLayout())

        # Model Selection
        self.model_label = QLabel("Select LLM Model:")
        self.model_select = QComboBox()
        self.model_select.addItems(["Local Model", "OpenAI GPT", "Anthropic Claude"])
        self.layout().addWidget(self.model_label)
        self.layout().addWidget(self.model_select)

        # API Key Input
        self.api_key_label = QLabel("API Key:")
        self.api_key_input = QLineEdit()
        self.layout().addWidget(self.api_key_label)
        self.layout().addWidget(self.api_key_input)

        # Save Button
        save_button = QPushButton("Save Settings")
        save_button.clicked.connect(self.save_settings)
        self.layout().addWidget(save_button)

    def save_settings(self):
        model = self.model_select.currentText()
        api_key = self.api_key_input.text()
        print(f"LLM Model: {model}, API Key: {api_key}")
        self.close()
