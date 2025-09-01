import requests
import webbrowser
from colorama import Fore, Style, init
import time

init(autoreset=True)

def main():
    print(f"{Fore.RED}=== Discord Bot Invite To ID Black Falcon ==={Style.RESET_ALL}")
    try:
        bot_id = int(input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}ID du bot Discord : {Style.RESET_ALL}"))
    except Exception:
        print(f"{Fore.RED}ID invalide.{Style.RESET_ALL}")
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
        return

    invite_url = f'https://discord.com/oauth2/authorize?client_id={bot_id}&scope=bot&permissions=8'
    try:
        response = requests.get(invite_url)
        print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Invite URL : {Fore.BLUE}{invite_url}{Fore.RED} (status: {response.status_code}){Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la vérification de l'URL : {e}{Style.RESET_ALL}")

    choice = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Ouvrir dans le navigateur ? (y/n) : {Style.RESET_ALL}").strip().lower()
    if choice in ['y', 'yes', 'o', 'oui']:
        webbrowser.open_new_tab(invite_url)
        print(f"{Fore.RED}Lien ouvert dans le navigateur.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Lien non ouvert.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()