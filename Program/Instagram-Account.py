import instaloader
from colorama import Fore, Style, init
import time

init(autoreset=True)
# ... le reste du code ...

def print_banner():
    print(f"{Fore.RED}=== Instagram Account Black Falcon ==={Style.RESET_ALL}")

def safe_attr(obj, attr, default="None"):
    try:
        value = getattr(obj, attr)
        if value is None or (isinstance(value, str) and not value.strip()):
            return default
        return value
    except Exception:
        return default

def main():
    print_banner()
    username = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Instagram Username -> {Style.RESET_ALL}").strip()
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
        return

    print(f"""
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
{Fore.BLUE}Full Name       : {Fore.RED}{safe_attr(profile, 'full_name')}{Style.RESET_ALL}
{Fore.BLUE}Username        : {Fore.RED}{safe_attr(profile, 'username')}{Style.RESET_ALL}
{Fore.BLUE}Instagram Id    : {Fore.RED}{safe_attr(profile, 'userid')}{Style.RESET_ALL}
{Fore.BLUE}Biography       : {Fore.RED}{safe_attr(profile, 'biography')}{Style.RESET_ALL}
{Fore.BLUE}Profile Url     : {Fore.RED}https://instagram.com/{safe_attr(profile, 'username')}{Style.RESET_ALL}
{Fore.BLUE}Profile Photo   : {Fore.RED}{safe_attr(profile, 'profile_pic_url')}{Style.RESET_ALL}
{Fore.BLUE}Publications    : {Fore.RED}{safe_attr(profile, 'mediacount')}{Style.RESET_ALL}
{Fore.BLUE}Subscribers     : {Fore.RED}{safe_attr(profile, 'followers')}{Style.RESET_ALL}
{Fore.BLUE}Subscriptions   : {Fore.RED}{safe_attr(profile, 'followees')}{Style.RESET_ALL}
{Fore.BLUE}Verified        : {Fore.RED}{'True' if safe_attr(profile, 'is_verified', False) else 'False'}{Style.RESET_ALL}
{Fore.BLUE}Private Account : {Fore.RED}{'True' if safe_attr(profile, 'is_private', False) else 'False'}{Style.RESET_ALL}
{Fore.BLUE}Pro Account     : {Fore.RED}{'True' if safe_attr(profile, 'is_business_account', False) else 'False'}{Style.RESET_ALL}""")
    if safe_attr(profile, 'is_business_account', False):
        print(f"{Fore.BLUE}Category Pro    : {Fore.RED}{safe_attr(profile, 'business_category_name')}{Style.RESET_ALL}")

    print(f"{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    if not safe_attr(profile, 'is_private', True):
        try:
            posts = profile.get_posts()
            for i, post in enumerate(posts):
                print(f"""
{Fore.BLUE}Publication n°{i+1}{Style.RESET_ALL}
{Fore.BLUE}URL        : {Fore.RED}https://www.instagram.com/p/{safe_attr(post, 'shortcode')}/{Style.RESET_ALL}
{Fore.BLUE}Date       : {Fore.RED}{safe_attr(post, 'date')}{Style.RESET_ALL}
{Fore.BLUE}Likes      : {Fore.RED}{safe_attr(post, 'likes')}{Style.RESET_ALL}
{Fore.BLUE}Comments   : {Fore.RED}{safe_attr(post, 'comments')}{Style.RESET_ALL}
{Fore.BLUE}Legend     : {Fore.RED}{safe_attr(post, 'caption')}{Style.RESET_ALL}
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────""")
                if i == 4:
                    break
        except Exception as e:
            print(f"{Fore.RED}Erreur lors de la récupération des posts : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()