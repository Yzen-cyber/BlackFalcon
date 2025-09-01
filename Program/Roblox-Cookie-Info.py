import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

def main():
    print(f"{Fore.RED}=== Roblox Cookie Info Black Falcon ==={Style.RESET_ALL}")
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    headers = {"User-Agent": user_agent}
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}User-Agent sélectionné : {Fore.BLUE}{user_agent}{Style.RESET_ALL}")

    cookie = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Cookie ROBLOSECURITY : {Style.RESET_ALL}").strip()
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Récupération des informations...{Style.RESET_ALL}")

    try:
        response = requests.get(
            "https://www.roblox.com/mobileapi/userinfo",
            headers=headers,
            cookies={".ROBLOSECURITY": cookie},
            timeout=10
        )
        api = response.json()
        status = "Valide"
        username_roblox = api.get('UserName', "None")
        user_id_roblox = api.get("UserID", "None")
        robux_roblox = api.get("RobuxBalance", "None")
        premium_roblox = api.get("IsPremium", "None")
        avatar_roblox = api.get("ThumbnailUrl", "None")
        builders_club_roblox = api.get("IsAnyBuildersClubMember", "None")
    except Exception as e:
        status = "Invalide"
        username_roblox = "None"
        user_id_roblox = "None"
        robux_roblox = "None"
        premium_roblox = "None"
        avatar_roblox = "None"
        builders_club_roblox = "None"

    print(f"""
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
{Fore.BLUE}Status        : {Fore.RED}{status}{Style.RESET_ALL}
{Fore.BLUE}Username      : {Fore.RED}{username_roblox}{Style.RESET_ALL}
{Fore.BLUE}Id            : {Fore.RED}{user_id_roblox}{Style.RESET_ALL}
{Fore.BLUE}Robux         : {Fore.RED}{robux_roblox}{Style.RESET_ALL}
{Fore.BLUE}Premium       : {Fore.RED}{premium_roblox}{Style.RESET_ALL}
{Fore.BLUE}Builders Club : {Fore.RED}{builders_club_roblox}{Style.RESET_ALL}
{Fore.BLUE}Avatar        : {Fore.RED}{avatar_roblox}{Style.RESET_ALL}
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
""")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()