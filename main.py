### main.py

from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainController
from views.main_view import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    controller = MainController(view)
    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()