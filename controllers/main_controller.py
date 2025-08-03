# controllers/main_controller.py

from views.main_view import MainWindow
from models.keylogger import start_logging, stop_logging
from models.encryption import decrypt_file

class MainController:
    def __init__(self, view):
        self.view = view
        self.session_password = None
        self.is_logging = False
        self.view.start_button.clicked.connect(self.start_keylogger)
        self.view.stop_button.clicked.connect(self.stop_keylogger)
        self.view.decrypt_button.clicked.connect(self.decrypt_log)

    def start_keylogger(self):

        if self.is_logging:
            return  # Already logging, do nothing
        password = self.view.prompt_password("Enter a session password to start keylogger:")
        if not password:
            self.view.show_error("Password is required to start.")
            return

        self.session_password = password
        start_logging(self.session_password)  # ✅ Pass the password
        self.view.status_label.setText("Keylogger started.")
        self.is_logging = True

    def stop_keylogger(self):
        
        if not self.is_logging:
            return
        password = self.view.prompt_password("Enter session password to stop keylogger:")
        if password != self.session_password:
            self.view.show_error("Incorrect password. Cannot stop keylogger.")
            return

        stop_logging(self.session_password)  # ✅ Use the session password
        self.view.status_label.setText("Keylogger stopped and log encrypted.")
        self.is_logging = False
    def decrypt_log(self):
        password = self.view.prompt_password("Enter password to decrypt log:")
        try:
            output_file = decrypt_file(password)
            self.view.status_label.setText(f"Decrypted to: {output_file}")
        except Exception as e:
            self.view.show_error(str(e))
    def force_stop_keylogger(self):
        from models.keylogger import force_stop
        force_stop()
        
