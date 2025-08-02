### models/encryption.py

from cryptography.fernet import Fernet
import base64
import hashlib


def get_fernet(password: str):
    key = hashlib.sha256(password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))


def encrypt_file(input_file, output_file, password):
    fernet = get_fernet(password)
    with open(input_file, "rb") as f_input:
        data = f_input.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, "wb") as f_output:
        f_output.write(encrypted)


def decrypt_file(password):
    encrypted_file = "encrypted_log.txt"
    decrypted_file = "decrypted_log.txt"
    fernet = get_fernet(password)

    try:
        with open(encrypted_file, "rb") as f_input:
            encrypted_data = f_input.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(decrypted_file, "wb") as f_output:
            f_output.write(decrypted_data)
        return decrypted_file
    except FileNotFoundError:
        raise FileNotFoundError("Encrypted log not found. Please start and stop keylogger first.")
    except Exception:
        raise ValueError("Decryption failed. Incorrect password.")
