from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
import os

class ErrorDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Error")
        self.setFixedSize(360, 180)

        layout = QVBoxLayout(self)

        # Icon and title
        icon_label = QLabel()
        icon_path = os.path.join("icons", "error.png")
        if os.path.exists(icon_path):
            icon_label.setPixmap(QPixmap(icon_path).scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            icon_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(icon_label)

        title_label = QLabel("An Error Occurred")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #b00020;")
        layout.addWidget(title_label)

        # Message
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(message_label)

        # OK button
        button = QPushButton("OK")
        ok_icon_path = os.path.join("icons", "okay.png")
        if os.path.exists(ok_icon_path):
            button.setIcon(QIcon(ok_icon_path))
        button.clicked.connect(self.accept)
        button.setFixedWidth(80)

        # Set font color to black
        button.setStyleSheet("""
            QPushButton {
                color: black;
                background-color: #ffcccc;
                border: none;
                padding: 8px;
                border-radius: 6px;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: #f4a9a9;
            }
        """)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(button)
        button_layout.addStretch()

        layout.addLayout(button_layout)
