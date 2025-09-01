from colorama import Fore, Style, init
import requests

init(autoreset=True)

print(f"{Fore.RED}=== Subdomain Scanner Black Falcon ==={Style.RESET_ALL}")
domain = input(f"{Fore.BLUE}Domaine cible (ex: example.com) : {Style.RESET_ALL}").strip()
wordlist = input(f"{Fore.BLUE}Fichier wordlist de sous-domaines : {Style.RESET_ALL}").strip()

try:
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for sub in f:
            sub = sub.strip()
            url = f"http://{sub}.{domain}"
            try:
                r = requests.get(url, timeout=2)
                if r.status_code < 400:
                    print(f"{Fore.GREEN}Trouvé : {url}{Style.RESET_ALL}")
            except:
                pass
except FileNotFoundError:
    print(f"{Fore.RED}Wordlist introuvable.{Style.RESET_ALL}")

input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")