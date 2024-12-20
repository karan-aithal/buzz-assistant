from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from utils.db import save_settings, load_settings
from utils.signal_handler import signal_handler

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setLayout(QVBoxLayout())

        # Reset Chat History
        self.reset_chat_button = QPushButton("Reset Chat History")
        self.reset_chat_button.clicked.connect(self.reset_chat_history)
        self.layout().addWidget(self.reset_chat_button)

        # Just Text Model Toggle
        self.just_text_model_checkbox = QCheckBox("Enable Just Text Model")
        self.just_text_model_checkbox.setChecked(load_settings("just_text_model", False))
        self.layout().addWidget(self.just_text_model_checkbox)

        # Profile Management
        self.profile_label = QLabel("Profile:")
        self.profile_input = QLineEdit()
        self.profile_input.setText(load_settings("profile", "Default"))
        self.layout().addWidget(self.profile_label)
        self.layout().addWidget(self.profile_input)
        self.save_profile_button = QPushButton("Save Profile")
        self.save_profile_button.clicked.connect(self.save_profile)
        self.layout().addWidget(self.save_profile_button)

        # Predefined Agents Toggle
        self.predefined_agents_checkbox = QCheckBox("Enable Predefined Agents (Good Results, Long Response Time)")
        self.predefined_agents_checkbox.setChecked(load_settings("predefined_agents", False))
        self.layout().addWidget(self.predefined_agents_checkbox)

        # Auto Stop Recording
        self.auto_stop_checkbox = QCheckBox("Enable Auto Stop Recording")
        self.auto_stop_checkbox.setChecked(load_settings("auto_stop_recording", False))
        self.layout().addWidget(self.auto_stop_checkbox)

        # Wake Word Configuration
        self.wakeword_label = QLabel("Wakeword - Pvporcupine API Key")
        self.wakeword_input = QLineEdit()
        self.wakeword_input.setText(load_settings("wakeword_api_key", ""))
        self.layout().addWidget(self.wakeword_label)
        self.layout().addWidget(self.wakeword_input)

        self.wakeword_checkbox = QCheckBox("Enable Wake Word")
        self.wakeword_checkbox.setChecked(load_settings("wakeword_enabled", False))
        self.layout().addWidget(self.wakeword_checkbox)

        # Screen Input for Wake Word Mode
        self.screen_input_checkbox = QCheckBox("Enable Screen Input for Wake Word Mode")
        self.screen_input_checkbox.setChecked(load_settings("screen_input_enabled", False))
        self.layout().addWidget(self.screen_input_checkbox)

        # Continuous Conversations
        self.continuous_conversations_checkbox = QCheckBox("Enable Continuous Conversations")
        self.continuous_conversations_checkbox.setChecked(load_settings("continuous_conversations", False))
        self.layout().addWidget(self.continuous_conversations_checkbox)

        # Save Button
        self.save_button = QPushButton("Save Settings")
        self.save_button.clicked.connect(self.save_settings)
        self.layout().addWidget(self.save_button)

    def reset_chat_history(self):
        """Resets chat history."""
        save_settings("chat_history", [])
        signal_handler.notification.emit("Chat history reset.")

    def save_profile(self):
        """Saves the active profile."""
        profile = self.profile_input.text()
        save_settings("profile", profile)
        signal_handler.notification.emit(f"Profile saved: {profile}")

    def save_settings(self):
        """Saves all settings."""
        save_settings("just_text_model", self.just_text_model_checkbox.isChecked())
        save_settings("predefined_agents", self.predefined_agents_checkbox.isChecked())
        save_settings("auto_stop_recording", self.auto_stop_checkbox.isChecked())
        save_settings("wakeword_api_key", self.wakeword_input.text())
        save_settings("wakeword_enabled", self.wakeword_checkbox.isChecked())
        save_settings("screen_input_enabled", self.screen_input_checkbox.isChecked())
        save_settings("continuous_conversations", self.continuous_conversations_checkbox.isChecked())
        signal_handler.notification.emit("Settings saved successfully.")
        self.close()
