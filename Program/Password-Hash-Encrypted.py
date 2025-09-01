import hashlib
import base64
try:
    import bcrypt
except ImportError:
    bcrypt = None
from hashlib import pbkdf2_hmac
from colorama import Fore, Style, init

init(autoreset=True)

def menu_algo():
    print(f"""{Fore.RED}=== Chiffrement de mot de passe Black Falcon ==={Style.RESET_ALL}
{Fore.BLUE}Méthodes disponibles :
  1. BCRYPT
  2. MD5
  3. SHA-1
  4. SHA-256
  5. PBKDF2 (SHA-256)
  6. Base64 Encode{Style.RESET_ALL}
""")

def encrypt_password(choice, password):
    try:
        if choice == "1":
            if not bcrypt:
                print(f"{Fore.RED}Le module bcrypt n'est pas installé.{Style.RESET_ALL}")
                return None
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        elif choice == "2":
            return hashlib.md5(password.encode('utf-8')).hexdigest()
        elif choice == "3":
            return hashlib.sha1(password.encode('utf-8')).hexdigest()
        elif choice == "4":
            return hashlib.sha256(password.encode('utf-8')).hexdigest()
        elif choice == "5":
            return pbkdf2_hmac('sha256', password.encode('utf-8'), b"this_is_a_salt", 100000).hex()
        elif choice == "6":
            return base64.b64encode(password.encode('utf-8')).decode('utf-8')
        else:
            return None
    except Exception as e:
        print(f"{Fore.RED}Erreur lors du chiffrement : {e}{Style.RESET_ALL}")
        return None

def main():
    menu_algo()
    choice = input(f"{Fore.BLUE}Méthode (1-6) : {Style.RESET_ALL}").strip()
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
        return
    password = input(f"{Fore.BLUE}Mot de passe à chiffrer : {Style.RESET_ALL}").strip()
    encrypted_password = encrypt_password(choice, password)
    if encrypted_password:
        print(f"{Fore.RED}Mot de passe chiffré : {Fore.BLUE}{encrypted_password}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Erreur lors du chiffrement.{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()