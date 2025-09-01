import webbrowser
from colorama import Fore, Style, init
import time

init(autoreset=True)

def main():
    print(f"{Fore.RED}=== Info Black Falcon ==={Style.RESET_ALL}\n")
    print(f"""{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 {Fore.BLUE}Nom du Tool     : {Fore.RED}Black Falcon
 {Fore.BLUE}Type du Tool    : {Fore.RED}OSINT / Pentest / Utilitaires
 {Fore.BLUE}Version         : {Fore.RED}1.0
 {Fore.BLUE}Copyright       : {Fore.RED}© Black Falcon
 {Fore.BLUE}Coding          : {Fore.RED}Python 3.x
 {Fore.BLUE}Langue          : {Fore.RED}Français
 {Fore.BLUE}Créateur        : {Fore.RED}Enzo
 {Fore.BLUE}Plateforme      : {Fore.RED}Windows
 {Fore.BLUE}GunsLol   [W]   : {Fore.RED}https://guns.lol/
 {Fore.BLUE}GitHub    [W]   : {Fore.RED}https://github.com/
 {Fore.BLUE}Telegram  [W]   : {Fore.RED}https://t.me/RedTigerTools
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")
    license_read = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Ouvrir le fichier 'LICENSE' ? (y/n) -> {Style.RESET_ALL}")
    if license_read.lower() in ['y', 'yes', 'o', 'oui']:
        webbrowser.open_new_tab("LICENSE")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()