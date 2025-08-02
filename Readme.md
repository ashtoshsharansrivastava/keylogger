# Keylogger App by Ashutosh

This is a secure, password-protected keylogger application with a modern PySide6 (Qt for Python) interface. The program follows the Model-View-Controller (MVC) architecture and includes encrypted logging, session password management, and a GUI-based control panel for ease of use.

---

## 🔐 Features

- **Secure start/stop** of keylogging using a user-defined session password
- **AES Encryption** of logs with the `cryptography` library
- **Password-protected log decryption**
- **Modern GUI** with intuitive icon-based buttons (Start, Stop, Decrypt)
- **System password authentication** on Linux (using `sudo -v`)
- **Styled dialogs** for password input and error reporting
- **Proper MVC architecture** for easy maintainability
- **No leftover plaintext logs** after encryption

---

## 🧩 Requirements

Make sure you have Python 3.10+ installed.

### 1. Clone the Repository

```bash
git clone https://github.com/ashtoshsharansrivastava/keylogger.git
cd keylogger
2. Set Up a Virtual Environment (Recommended)
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or
.venv\Scripts\activate      # Windows
3. Install Required Python Packages
Install manually:

bash
Copy
Edit
pip install PySide6 cryptography pynput
Or, if requirements.txt is present:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ How to Use
1. Launch the Application
bash
Copy
Edit
python main.py
2. Start Keylogger
Click the “Start” button

Enter a session password when prompted

Keylogger will start capturing keystrokes

Log file (logs/session_log.txt) will be created

3. Stop Keylogger
Click the “Stop” button

Enter the same session password

The log will be encrypted and saved as logs/session_log_encrypted

The plaintext log is automatically deleted for security

4. Decrypt the Log
Click “Decrypt” button

Enter the correct session password used earlier

If correct, the decrypted log will be saved and shown

🧱 Project Structure
pgsql
Copy
Edit
Keylogger/
├── main.py                         # App entry point
├── controllers/
│   └── main_controller.py         # Connects view to model
├── models/
│   ├── keylogger.py               # Keylogging and session handling
│   └── encryption.py              # AES encryption and decryption
├── views/
│   └── main_view.py               # PySide6 GUI interface
├── utils/
│   └── auth.py                    # System password authentication
├── icons/
│   ├── start.png
│   ├── stop.png
│   └── decrypt.png
├── logs/
│   ├── session_log.txt            # Temporary plaintext log
│   └── session_log_encrypted      # Final encrypted log
└── README.md
💡 Ubuntu Note (Important!)
If you are on Ubuntu, the keylogger will not work under Wayland due to security restrictions on keyboard event access. You must switch to X11:

How to switch from Wayland to X11:
Log out of your Ubuntu session.

On the login screen, click the gear icon.

Select "Ubuntu on X11".

Log back in and run the app.

⚠️ Security & Ethical Disclaimer
This software is strictly for educational and ethical research purposes only.

Logs are encrypted

Plaintext logs are not retained

Unauthorized use of this software to capture keystrokes without consent is illegal and unethical

You are fully responsible for any misuse

👨‍💻 Author
Ashutosh Sharan Srivastava
GitHub: ashtoshsharansrivastava
If you encounter bugs or have suggestions, please open an issue in the repository.

yaml
Copy
Edit

---

Let me know if you'd also like me to generate:

- `.gitignore`
- `requirements.txt`
- Sample encrypted log or test decryption
- Screenshot preview section for the README  







Ask ChatGPT
