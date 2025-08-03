from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class PasswordDialog(QDialog):
    def __init__(self, prompt_text="Enter password", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Authentication Required")
        self.setFixedSize(400, 200)
        self.setStyleSheet("background-color: white; font-size: 16px;")

        self.password = None

        prompt_label = QLabel(prompt_text)
        prompt_label.setStyleSheet("color: black; font-weight: bold;")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("padding: 10px; color: black; border: 1px solid #ccc; border-radius: 5px;")

        self.ok_button = QPushButton("  OK")
        self.ok_button.setIcon(QIcon("icons/okay.png"))
        self.ok_button.setIconSize(QSize(24, 24))
        self.ok_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px 16px; border-radius: 8px;")
        self.ok_button.clicked.connect(self.accept)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #f44336; color: white; padding: 8px 16px; border-radius: 8px;")
        self.cancel_button.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout = QVBoxLayout()
        layout.addWidget(prompt_label)
        layout.addWidget(self.password_input)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_password(self):
        if self.exec() == QDialog.Accepted:
            return self.password_input.text(), True
        else:
            return "", False
