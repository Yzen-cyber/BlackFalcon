import os
import sys
import subprocess

requirements = [
    "auto-py-to-exe",
    "bcrypt",
    "beautifulsoup4",
    "browser-cookie3",
    "colorama",
    "cryptography",
    "customtkinter",
    "deep-translator",
    "discord",
    "dnspython",
    "exifread",
    "GPUtil",
    "instaloader",
    "keyboard",
    "opencv-python",
    "phonenumbers",
    "piexif",
    "pillow",
    "psutil",
    "pyautogui",
    "pycryptodome",
    "pyinstaller",
    "pyqt5",
    "pyqtwebengine",
    "pywin32",
    "pyzipper",
    "rarfile",
    "requests",
    "screeninfo",
    "selenium",
    "setuptools",
    "urllib3",
    "whois"
]

def install_requirements():
    python_exec = sys.executable
    for req in requirements:
        try:
            subprocess.check_call([python_exec, "-m", "pip", "install", req])
            print(f"[OK] {req} installé.")
        except subprocess.CalledProcessError:
            print(f"[ERREUR] Impossible d'installer {req}.")

if __name__ == "__main__":
    print("=== Installation des dépendances BlackFalcon ===\n")
    install_requirements()
    print("\nInstallation terminée !")
    input("Appuyez sur Entrée pour quitter.")