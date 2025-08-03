from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QSizePolicy, QDialog, QLineEdit, QMessageBox, QHBoxLayout
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize, Qt
from utils.auth import verify_system_password

from views.password_dialog import PasswordDialog
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Keylogger by Ashutosh")
        self.setFixedSize(800, 600)

        self.setStyleSheet("background-color: white;")

        self.status_label = QLabel("Status: Not started")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 30px; color: #333;")

        button_style = """
            QPushButton {
                background-color: #ADD8E6;
                color: black;
                font-size: 30px;
                padding: 12px;
                border-radius: 12px;
            }
            QPushButton:hover {
                background-color: #87CEFA;
            }
        """

        self.start_button = QPushButton(" Start Keylogger")
        self.start_button.setIcon(QIcon("icons/start.png"))
        self.start_button.setIconSize(QSize(70, 100))
        self.start_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.start_button.setStyleSheet(button_style)

        self.stop_button = QPushButton(" Stop Keylogger")
        self.stop_button.setIcon(QIcon("icons/stop.png"))
        self.stop_button.setIconSize(QSize(70, 100))
        self.stop_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.stop_button.setStyleSheet(button_style)

        self.decrypt_button = QPushButton(" Decrypt Log")
        self.decrypt_button.setIcon(QIcon("icons/decrypt.png"))
        self.decrypt_button.setIconSize(QSize(70, 100))
        self.decrypt_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.decrypt_button.setStyleSheet(button_style)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addStretch()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.decrypt_button)
        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def prompt_password(self, prompt_text):
        dialog = PasswordDialog(prompt_text, self)
        password, ok = dialog.get_password()
        return password if ok else None

    def prompt_and_authenticate(self, prompt_text):
        password, ok = PasswordDialog(prompt_text, self).get_password()
        if ok:
            if verify_system_password(password):
                return True
            else:
                self.show_error("Authentication Failed", "Incorrect password.")
                return False
        return False
