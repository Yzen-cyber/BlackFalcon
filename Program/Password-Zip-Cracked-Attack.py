import os
import sys
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import pyzipper
    import rarfile
except ImportError as e:
    print(f"{Fore.RED}Module manquant : {e}. Installez-le avec pip avant d'utiliser ce script.{Style.RESET_ALL}")
    sys.exit(1)

def choose_file():
    print(f"{Fore.RED}=== Password Zip Cracked Attack Black Falcon ==={Style.RESET_ALL}")
    path = input(f"{Fore.BLUE}Chemin du fichier .zip ou .rar à attaquer : {Style.RESET_ALL}").strip()
    if not os.path.isfile(path):
        print(f"{Fore.RED}Fichier introuvable.{Style.RESET_ALL}")
        sys.exit(1)
    return path

def count_encrypted_files(file):
    count = 0
    try:
        if file.lower().endswith('.zip'):
            with pyzipper.AESZipFile(file) as archive:
                for filename in archive.namelist():
                    try:
                        archive.extract(filename, pwd=b'wrongpassword')
                    except RuntimeError:
                        count += 1
        elif file.lower().endswith('.rar'):
            with rarfile.RarFile(file) as archive:
                for filename in archive.namelist():
                    try:
                        archive.extract(filename, pwd='wrongpassword')
                    except rarfile.BadPassword:
                        count += 1
    except Exception:
        pass
    return count

def check_password(file, password_test):
    try:
        if file.lower().endswith('.zip'):
            with pyzipper.AESZipFile(file) as archive:
                for filename in archive.namelist():
                    try:
                        archive.extract(filename, pwd=password_test.encode())
                        print(f"{Fore.RED}Mot de passe trouvé : {Fore.BLUE}{password_test}{Style.RESET_ALL}")
                        return True
                    except:
                        pass
        elif file.lower().endswith('.rar'):
            with rarfile.RarFile(file) as archive:
                for filename in archive.namelist():
                    try:
                        archive.extract(filename, pwd=password_test.encode())
                        print(f"{Fore.RED}Mot de passe trouvé : {Fore.BLUE}{password_test}{Style.RESET_ALL}")
                        return True
                    except:
                        pass
    except Exception:
        pass
    return False

def random_character_attack(file, count):
    try:
        threads_number = int(input(f"{Fore.BLUE}Nombre de threads (défaut 4) : {Style.RESET_ALL}") or "4")
        char_min = int(input(f"{Fore.BLUE}Longueur min du mot de passe : {Style.RESET_ALL}") or "4")
        char_max = int(input(f"{Fore.BLUE}Longueur max du mot de passe : {Style.RESET_ALL}") or "8")
    except:
        print(f"{Fore.RED}Entrée invalide.{Style.RESET_ALL}")
        return

    found = [False]
    all_chars = string.ascii_letters + string.digits + string.punctuation

    def worker():
        while not found[0]:
            pwd = ''.join(random.choices(all_chars, k=random.randint(char_min, char_max)))
            if check_password(file, pwd):
                found[0] = True

    print(f"{Fore.RED}Brute force en cours... (peut être long){Style.RESET_ALL}")
    with ThreadPoolExecutor(max_workers=threads_number) as executor:
        for _ in range(threads_number):
            executor.submit(worker)
        while not found[0]:
            time.sleep(0.1)

def wordlist_attack(file):
    wordlist_path = input(f"{Fore.BLUE}Chemin du fichier wordlist : {Style.RESET_ALL}").strip()
    if not os.path.isfile(wordlist_path):
        print(f"{Fore.RED}Fichier wordlist introuvable.{Style.RESET_ALL}")
        return
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pwd = line.strip()
            if check_password(file, pwd):
                return
    print(f"{Fore.RED}Aucun mot de passe trouvé dans la wordlist.{Style.RESET_ALL}")

def main():
    file = choose_file()
    count = count_encrypted_files(file)
    print(f"{Fore.RED}Nombre de fichiers protégés par mot de passe : {Fore.BLUE}{count}{Style.RESET_ALL}")
    if count == 0:
        print(f"{Fore.RED}Aucun fichier protégé par mot de passe détecté.{Style.RESET_ALL}")
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
        return

    print(f"""
{Fore.RED}Méthodes disponibles :
  1. Brute force caractères aléatoires
  2. Wordlist
{Style.RESET_ALL}""")
    method = input(f"{Fore.BLUE}Méthode (1-2) : {Style.RESET_ALL}").strip()
    if method == "1":
        random_character_attack(file, count)
    elif method == "2":
        wordlist_attack(file)
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()