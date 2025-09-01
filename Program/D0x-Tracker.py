import webbrowser
from colorama import Fore, Style, init
import time

init(autoreset=True)

SITES = {
    "01": ("Facebook.com", lambda s, n, f, t: f"https://www.facebook.com/search/top/?init=quick&q={s or n + ' ' + f}"),
    "02": ("Youtube.com", lambda s, n, f, t: f"https://www.youtube.com/results?search_query={s or n + '+' + f}"),
    "03": ("Twitter.com", lambda s, n, f, t: f"https://twitter.com/search?f=users&vertical=default&q={s or n + ' ' + f}"),
    "04": ("Tiktok.com", lambda s, n, f, t: f"https://www.tiktok.com/search?q={s or n + ' ' + f}"),
    "05": ("Peekyou.com", lambda s, n, f, t: f"https://www.peekyou.com/{s or n + '_' + f}"),
    "06": ("Tumblr.com", lambda s, n, f, t: f"https://www.tumblr.com/search/{s or n + ' ' + f}"),
    "07": ("PagesJaunes.fr", lambda s, n, f, t: f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={s or n + ' ' + f}"),
    "08": ("LinkedIn", lambda s, n, f, t: f"https://www.linkedin.com/search/results/all/?keywords={s or n + ' ' + f}"),
    "09": ("GitHub", lambda s, n, f, t: f"https://github.com/search?q={s or n + ' ' + f}"),
    "10": ("Instagram", lambda s, n, f, t: f"https://www.instagram.com/{s or n + f}"),
    "11": ("Reddit", lambda s, n, f, t: f"https://www.reddit.com/user/{s or n + f}"),
    "12": ("Snapchat", lambda s, n, f, t: f"https://www.snapchat.com/add/{s or n + f}"),
    "13": ("TikTok Hashtag", lambda s, n, f, t: f"https://www.tiktok.com/tag/{s or n + f}"),
    "14": ("Pinterest", lambda s, n, f, t: f"https://www.pinterest.com/search/people/?q={s or n + ' ' + f}"),
    "15": ("SoundCloud", lambda s, n, f, t: f"https://soundcloud.com/{s or n + f}"),
    "16": ("Quora", lambda s, n, f, t: f"https://www.quora.com/profile/{s or n + f}"),
    "17": ("About.me", lambda s, n, f, t: f"https://about.me/{s or n + f}"),
    "18": ("Flickr", lambda s, n, f, t: f"https://www.flickr.com/people/{s or n + f}"),
    "19": ("Keybase", lambda s, n, f, t: f"https://keybase.io/{s or n + f}"),
    "20": ("Telegram", lambda s, n, f, t: f"https://t.me/{s or n + f}"),
}

def main():
    print(f"{Fore.RED}=== Dox Tracker Black Falcon (Avancé) ==={Style.RESET_ALL}")
    print(f"""
 {Fore.BLUE}00{Fore.RED} Retour
 {Fore.BLUE}01{Fore.RED} Username
 {Fore.BLUE}02{Fore.RED} LastName, FirstName
 {Fore.BLUE}03{Fore.RED} Autre
""")
    search_type = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Type de recherche -> {Style.RESET_ALL}").strip()

    if search_type in ['00', '0']:
        return

    search = name = first_name = None
    if search_type in ['01', '1']:
        search = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Username -> {Style.RESET_ALL}").strip()
    elif search_type in ['02', '2']:
        name = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}LastName -> {Style.RESET_ALL}").strip()
        first_name = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}FirstName -> {Style.RESET_ALL}").strip()
    elif search_type in ['03', '3']:
        search = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Recherche -> {Style.RESET_ALL}").strip()
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
        return

    print(f"\n{Fore.RED}Sites disponibles :{Style.RESET_ALL}")
    for key, (site, _) in SITES.items():
        print(f" {Fore.BLUE}{key}{Fore.RED} {site}")

    while True:
        choice = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Site -> {Style.RESET_ALL}").strip()
        if choice in ['0', '00']:
            break
        if choice in SITES:
            url = SITES[choice][1](search, name, first_name, search_type)
            print(f"{Fore.BLUE}Ouverture : {Fore.RED}{url}{Style.RESET_ALL}")
            webbrowser.open(url)
        else:
            print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()