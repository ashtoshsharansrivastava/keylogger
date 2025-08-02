# utils/auth.py

import subprocess

def verify_system_password(password):
    try:
        # Run a harmless command with sudo
        proc = subprocess.run(
            ['sudo', '-S', 'echo', 'Authenticated'],
            input=password + '\n',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Debug info (optional)
        print("RETURN CODE:", proc.returncode)
        print("STDERR:", proc.stderr)

        return proc.returncode == 0
    except Exception as e:
        print("Error verifying password:", e)
        return False
