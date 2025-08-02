from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QSizePolicy, QDialog, QLineEdit, QMessageBox, QHBoxLayout
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize, Qt
from utils.auth import verify_system_password

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

    def prompt_and_authenticate(self, prompt_text="Enter your system password:"):
            password, ok = QDialog.getText(
            self, "Authentication Required",
            prompt_text,
            QLineEdit.Password
        )
            if ok:
                if verify_system_password(password):
                    return True
                else:
                    QMessageBox.critical(self, "Authentication Failed", "Incorrect password.")
                    return False
            return False
    def prompt_password(self, prompt_text):
        dialog = QDialog(self)
        dialog.setWindowTitle("🔐 Password Required")
        dialog.setFixedSize(400, 200)
        dialog.setStyleSheet("background-color: #f0f8ff;")

        layout = QVBoxLayout()

        # Styled prompt label
        label = QLabel(prompt_text)
        label.setFont(QFont("Arial", 14))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #333333; margin-bottom: 10px;")
        layout.addWidget(label)

        # Password input
        password_input = QLineEdit()
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setFont(QFont("Arial", 14))
        password_input.setAlignment(Qt.AlignCenter)
        password_input.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: white;
                border: 2px solid #87CEFA;
                border-radius: 8px;
                padding: 6px;
            }
            QLineEdit:focus {
                border-color: #4682B4;
            }
        """)
        layout.addWidget(password_input)

        # Button area
        button_layout = QHBoxLayout()
        ok_button = QPushButton("✅ OK")
        ok_button.setFont(QFont("Arial", 12))
        ok_button.setStyleSheet("""
            QPushButton {
                background-color: #87CEFA;
                color: white;
                padding: 6px 12px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #4682B4;
            }
        """)
        ok_button.clicked.connect(dialog.accept)
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            return password_input.text()
        return None
    def show_error(self, message):
        error_box = QMessageBox(self)
        error_box.setWindowTitle("❌ Error")
        error_box.setText(message)
        error_box.setIcon(QMessageBox.Critical)

        # Custom font and text styling
        font = QFont("Arial", 12)
        error_box.setFont(font)

        # Custom stylesheet for dialog
        error_box.setStyleSheet("""
            QMessageBox {
                background-color: #ffe6e6;
            }
            QLabel {
                color: #b30000;a
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton {
                background-color: #ff4d4d;
                color: white;
                padding: 6px 12px;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e60000;
            }
        """)

        error_box.exec()