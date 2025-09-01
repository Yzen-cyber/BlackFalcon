import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

def main():
    print(f"{Fore.RED}=== Discord Server Info Black Falcon ==={Style.RESET_ALL}")
    invite = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Server Invitation -> {Style.RESET_ALL}").strip()
    try:
        invite_code = invite.split("/")[-1]
    except Exception:
        invite_code = invite

    try:
        response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
        if response.status_code == 200:
            api = response.json()
            inviter_info = api.get('inviter', {})
            server_info = api.get('guild', {})
            channel_info = api.get('channel', {})

            print(f"""
{Fore.RED}Invitation Information:
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────
{Fore.BLUE}Invitation         : {Fore.RED}{invite}{Style.RESET_ALL}
{Fore.BLUE}Type               : {Fore.RED}{api.get('type', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Code               : {Fore.RED}{api.get('code', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Expired            : {Fore.RED}{api.get('expires_at', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server ID          : {Fore.RED}{server_info.get('id', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Name        : {Fore.RED}{server_info.get('name', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Channel ID         : {Fore.RED}{channel_info.get('id', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Channel Name       : {Fore.RED}{channel_info.get('name', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Channel Type       : {Fore.RED}{channel_info.get('type', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Description : {Fore.RED}{server_info.get('description', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Icon        : {Fore.RED}{server_info.get('icon', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Features    : {Fore.RED}{' / '.join(server_info.get('features', [])) if server_info.get('features') else 'None'}{Style.RESET_ALL}
{Fore.BLUE}Server NSFW Level  : {Fore.RED}{server_info.get('nsfw_level', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server NSFW        : {Fore.RED}{server_info.get('nsfw', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Flags              : {Fore.RED}{api.get('flags', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Verification Level         : {Fore.RED}{server_info.get('verification_level', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Server Premium Subscription Count : {Fore.RED}{server_info.get('premium_subscription_count', 'None')}{Style.RESET_ALL}
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────
""")
            if inviter_info:
                print(f"""{Fore.RED}Inviter Information:
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────
{Fore.BLUE}ID            : {Fore.RED}{inviter_info.get('id', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Username      : {Fore.RED}{inviter_info.get('username', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Global Name   : {Fore.RED}{inviter_info.get('global_name', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Avatar        : {Fore.RED}{inviter_info.get('avatar', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Discriminator : {Fore.RED}{inviter_info.get('discriminator', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Public Flags  : {Fore.RED}{inviter_info.get('public_flags', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Flags         : {Fore.RED}{inviter_info.get('flags', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Banner        : {Fore.RED}{inviter_info.get('banner', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Accent Color  : {Fore.RED}{inviter_info.get('accent_color', 'None')}{Style.RESET_ALL}
{Fore.BLUE}Banner Color  : {Fore.RED}{inviter_info.get('banner_color', 'None')}{Style.RESET_ALL}
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────
""")
        else:
            print(f"{Fore.RED}Lien d'invitation invalide ou erreur API (code {response.status_code}).{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()