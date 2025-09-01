import hashlib
import base64
import os
import string
import random
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

def menu_algo():
    print(f"""{Fore.RED}=== Déchiffrement de Hash Black Falcon ==={Style.RESET_ALL}
{Fore.BLUE}Méthodes disponibles :
  1. BCRYPT (nécessite le module 'bcrypt')
  2. MD5
  3. SHA-1
  4. SHA-256
  5. PBKDF2 (SHA-256)
  6. Base64 Decode{Style.RESET_ALL}
""")

def check_password(choice, encrypted_password, password_test, salt=b"this_is_a_salt"):
    try:
        if choice == "1":
            import bcrypt
            return bcrypt.checkpw(password_test.encode('utf-8'), encrypted_password.encode('utf-8'))
        elif choice == "2":
            return hashlib.md5(password_test.encode('utf-8')).hexdigest() == encrypted_password
        elif choice == "3":
            return hashlib.sha1(password_test.encode('utf-8')).hexdigest() == encrypted_password
        elif choice == "4":
            return hashlib.sha256(password_test.encode('utf-8')).hexdigest() == encrypted_password
        elif choice == "5":
            return hashlib.pbkdf2_hmac('sha256', password_test.encode('utf-8'), salt, 100000).hex() == encrypted_password
        elif choice == "6":
            try:
                return base64.b64decode(encrypted_password.encode('utf-8')).decode('utf-8') == password_test
            except:
                return False
        else:
            return False
    except Exception:
        return False

def brute_force_random(choice, encrypted_password):
    try:
        threads_number = int(input(f"{Fore.BLUE}Nombre de threads (défaut 4) : {Style.RESET_ALL}") or "4")
        char_min = int(input(f"{Fore.BLUE}Longueur min du mot de passe : {Style.RESET_ALL}") or "4")
        char_max = int(input(f"{Fore.BLUE}Longueur max du mot de passe : {Style.RESET_ALL}") or "8")
    except:
        print(f"{Fore.RED}Entrée invalide.{Style.RESET_ALL}")
        return

    found = [False]
    salt = b"this_is_a_salt"
    all_chars = string.ascii_letters + string.digits + string.punctuation

    def worker():
        while not found[0]:
            pwd = ''.join(random.choices(all_chars, k=random.randint(char_min, char_max)))
            if check_password(choice, encrypted_password, pwd, salt):
                found[0] = True
                print(f"{Fore.RED}Mot de passe trouvé : {Fore.BLUE}{pwd}{Style.RESET_ALL}")

    print(f"{Fore.RED}Brute force en cours... (peut être long){Style.RESET_ALL}")
    with ThreadPoolExecutor(max_workers=threads_number) as executor:
        for _ in range(threads_number):
            executor.submit(worker)
        while not found[0]:
            time.sleep(0.1)

def brute_force_wordlist(choice, encrypted_password):
    wordlist_path = input(f"{Fore.BLUE}Chemin du fichier wordlist : {Style.RESET_ALL}").strip()
    if not os.path.isfile(wordlist_path):
        print(f"{Fore.RED}Fichier introuvable.{Style.RESET_ALL}")
        return
    salt = b"this_is_a_salt"
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pwd = line.strip()
            if check_password(choice, encrypted_password, pwd, salt):
                print(f"{Fore.RED}Mot de passe trouvé : {Fore.BLUE}{pwd}{Style.RESET_ALL}")
                return
    print(f"{Fore.RED}Aucun mot de passe trouvé dans la wordlist.{Style.RESET_ALL}")

def main():
    menu_algo()
    choice = input(f"{Fore.BLUE}Méthode (1-6) : {Style.RESET_ALL}").strip()
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
        return
    encrypted_password = input(f"{Fore.BLUE}Hash/mot de passe chiffré à décrypter : {Style.RESET_ALL}").strip()
    print(f"""{Fore.BLUE}
Méthode brute force :
  1. Caractères aléatoires
  2. Wordlist
{Style.RESET_ALL}""")
    method = input(f"{Fore.BLUE}Méthode (1-2) : {Style.RESET_ALL}").strip()
    if method == "1":
        brute_force_random(choice, encrypted_password)
    elif method == "2":
        brute_force_wordlist(choice, encrypted_password)
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()