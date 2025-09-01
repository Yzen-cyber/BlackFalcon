import webbrowser
from colorama import Fore, Style, init
import time

init(autoreset=True)

SITES = {
    "1": ("GunsLol", "https://guns.lol/"),
    "01": ("GunsLol", "https://guns.lol/"),
    "2": ("Github", "https://github.com/"),
    "02": ("Github", "https://github.com/"),
    "3": ("Telegram", "https://t.me/RedTigerTools"),
    "03": ("Telegram", "https://t.me/RedTigerTools"),
}

def main():
    print(f"{Fore.RED}=== Sites Black Falcon ==={Style.RESET_ALL}")
    print(f"""
 {Fore.BLUE}01{Fore.RED} GunsLol
 {Fore.BLUE}02{Fore.RED} Github
 {Fore.BLUE}03{Fore.RED} Telegram
""")
    choice = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Site -> {Style.RESET_ALL}").strip()
    if choice in SITES:
        name, url = SITES[choice]
        webbrowser.open_new_tab(url)
        print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Accès au site \"{Fore.BLUE}{url}{Fore.RED}\"{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()