import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

def main():
    print(f"{Fore.RED}=== Roblox User Info Black Falcon ==={Style.RESET_ALL}")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    headers = {"User-Agent": user_agent}
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}User-Agent sélectionné : {Fore.BLUE}{user_agent}{Style.RESET_ALL}")

    username_input = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Nom d'utilisateur Roblox : {Style.RESET_ALL}").strip()
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Recherche de l'ID utilisateur...{Style.RESET_ALL}")

    try:
        response = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            headers=headers,
            json={
                "usernames": [username_input],
                "excludeBannedUsers": "true"
            },
            timeout=10
        )
        data = response.json()
        if not data.get("data") or not data["data"]:
            print(f"{Fore.RED}Aucun utilisateur trouvé pour ce nom.{Style.RESET_ALL}")
            input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
            return

        user_id = data['data'][0]['id']

        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}", headers=headers, timeout=10)
        api = response.json()

        userid = api.get('id', "None")
        display_name = api.get('displayName', "None")
        username = api.get('name', "None")
        description = api.get('description', "None")
        created_at = api.get('created', "None")
        is_banned = api.get('isBanned', "None")
        external_app_display_name = api.get('externalAppDisplayName', "None")
        has_verified_badge = api.get('hasVerifiedBadge', "None")

        print(f"""
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
{Fore.BLUE}Username       : {Fore.RED}{username}{Style.RESET_ALL}
{Fore.BLUE}Id             : {Fore.RED}{userid}{Style.RESET_ALL}
{Fore.BLUE}Display Name   : {Fore.RED}{display_name}{Style.RESET_ALL}
{Fore.BLUE}Description    : {Fore.RED}{description}{Style.RESET_ALL}
{Fore.BLUE}Created        : {Fore.RED}{created_at}{Style.RESET_ALL}
{Fore.BLUE}Banned         : {Fore.RED}{is_banned}{Style.RESET_ALL}
{Fore.BLUE}External Name  : {Fore.RED}{external_app_display_name}{Style.RESET_ALL}
{Fore.BLUE}Verified Badge : {Fore.RED}{has_verified_badge}{Style.RESET_ALL}
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
""")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la récupération des infos : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()