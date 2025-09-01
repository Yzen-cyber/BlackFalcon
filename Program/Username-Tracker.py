import requests
from bs4 import BeautifulSoup
import re
import time
from colorama import Fore, Style, init

init(autoreset=True)

SITES = {
    "Steam": "https://steamcommunity.com/id/{username}",
    "Telegram": "https://t.me/{username}",
    "TikTok": "https://www.tiktok.com/@{username}",
    "Instagram": "https://www.instagram.com/{username}",
    "Paypal": "https://www.paypal.com/paypalme/{username}",
    "GitHub": "https://github.com/{username}",
    "Pinterest": "https://www.pinterest.com/{username}",
    "Snapchat": "https://www.snapchat.com/add/{username}",
    "Blogger": "https://{username}.blogspot.com",
    "Tumblr": "https://{username}.tumblr.com",
    "SoundCloud": "https://soundcloud.com/{username}",
    "DeviantArt": "https://www.deviantart.com/{username}",
    "About.me": "https://about.me/{username}",
    "Flickr": "https://www.flickr.com/people/{username}",
    "Keybase": "https://keybase.io/{username}",
    "Last.fm": "https://www.last.fm/user/{username}",
    "Behance": "https://www.behance.net/{username}",
    "Quora": "https://www.quora.com/profile/{username}",
    "Patreon": "https://www.patreon.com/{username}",
    "Myspace": "https://myspace.com/{username}",
    "Kaggle": "https://www.kaggle.com/{username}",
    "Periscope": "https://www.pscp.tv/{username}",
    "Disqus": "https://disqus.com/by/{username}",
    "Mastodon": "https://mastodon.social/@{username}",
    "GitLab": "https://gitlab.com/{username}",
    "LiveJournal": "https://{username}.livejournal.com",
    "CodeWars": "https://www.codewars.com/users/{username}",
    "Gumroad": "https://gumroad.com/{username}",
    "Spotify": "https://open.spotify.com/user/{username}",
    "Weebly": "https://{username}.weebly.com",
    "YouTube": "https://www.youtube.com/@{username}",
    "ProductHunt": "https://www.producthunt.com/@{username}",
    "Mix": "https://mix.com/{username}",
    "Facebook": "https://www.facebook.com/{username}",
    "Strava": "https://www.strava.com/athletes/{username}",
    "Linktree": "https://linktr.ee/{username}",
    "Xbox": "https://www.xboxgamertag.com/search/{username}",
    "Vimeo": "https://vimeo.com/{username}",
    "Twitch": "https://www.twitch.tv/{username}",
    "Goodreads": "https://www.goodreads.com/{username}",
    "VK": "https://vk.com/{username}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{username}",
    "Dribbble": "https://dribbble.com/{username}",
    "AngelList": "https://angel.co/{username}",
    "500px": "https://500px.com/{username}",
    "LinkedIn": "https://www.linkedin.com/in/{username}",
    "Weibo": "https://weibo.com/{username}",
    "OKCupid": "https://www.okcupid.com/profile/{username}",
    "Meetup": "https://www.meetup.com/members/{username}",
    "CodePen": "https://codepen.io/{username}",
    "StackOverflow": "https://stackoverflow.com/users/{username}",
    "HackerRank": "https://www.hackerrank.com/{username}",
    "Xing": "https://www.xing.com/profile/{username}",
    "Deezer": "https://www.deezer.com/en/user/{username}",
    "Snapfish": "https://www.snapfish.com/{username}",
    "Ravelry": "https://www.ravelry.com/people/{username}",
    "ReverbNation": "https://www.reverbnation.com/{username}",
    "Vine": "https://vine.co/u/{username}",
    "Foursquare": "https://foursquare.com/user/{username}",
    "Ello": "https://ello.co/{username}",
    "Hootsuite": "https://hootsuite.com/{username}",
    "Prezi": "https://prezi.com/{username}",
    "Groupon": "https://www.groupon.com/profile/{username}",
    "Liveleak": "https://www.liveleak.com/c/{username}",
    "Joomla": "https://www.joomla.org/user/{username}",
    "StackExchange": "https://stackexchange.com/users/{username}",
    "Taringa": "https://www.taringa.net/{username}",
    "Shopify": "https://{username}.myshopify.com",
    "8tracks": "https://8tracks.com/{username}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{username}",
    "OpenSea": "https://opensea.io/{username}",
    "Trello": "https://trello.com/{username}",
    "Fiverr": "https://www.fiverr.com/{username}",
    "Badoo": "https://badoo.com/profile/{username}",
    "Rumble": "https://rumble.com/user/{username}",
    "Wix": "https://www.wix.com/website/{username}",
    "allmylinks": "https://allmylinks.com/{username}",
    "Medium": "https://medium.com/@{username}",
    "Reddit": "https://reddit.com/user/{username}",
    "Twitter": "https://x.com/{username}",
    "Fosstodon": "https://fosstodon.org/@{username}",
    "Bugcrowd": "https://bugcrowd.com/{username}",
    "HackerOne": "https://hackerone.com/{username}",
    "HackTheBox": "https://app.hackthebox.com/profile/{username}",
    "Apple Developer": "https://developer.apple.com/forums/profile/{username}",
    "Apple Discussions": "https://discussions.apple.com/profile/{username}",
    "Hacker News": "https://news.ycombinator.com/user?id={username}",
    "Bitbucket": "https://bitbucket.org/{username}",
    "Slack": "https://{username}.slack.com",
    "Slide Share": "https://www.slideshare.net/{username}",
    "Wattpad": "https://www.wattpad.com/user/{username}",
    "Codecademy": "https://www.codecademy.com/profiles/{username}",
    "Gravatar": "https://gravatar.com/{username}",
    "Dev To": "https://dev.to/{username}",
    "Kaskus": "https://www.kaskus.co.id/profile/@{username}",
    "Crunchbase": "https://www.crunchbase.com/person/{username}"
}

def main():
    print(f"{Fore.RED}=== Username Tracker Black Falcon ==={Style.RESET_ALL}")
    username = input(f"{Fore.BLUE}Pseudo à rechercher : {Style.RESET_ALL}").strip()
    found = []
    not_found = []
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    total = len(SITES)
    print(f"{Fore.RED}Recherche sur {Fore.BLUE}{total}{Fore.RED} sites...{Style.RESET_ALL}")
    for site, url_template in SITES.items():
        url = url_template.format(username=username)
        try:
            resp = session.get(url, headers=headers, timeout=5)
            if resp.status_code == 200 and username.lower() in resp.text.lower():
                found.append((site, url))
                print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Trouvé sur {Fore.BLUE}{site}{Fore.RED} : {Fore.BLUE}{url}{Style.RESET_ALL}")
            else:
                not_found.append((site, url))
        except Exception as e:
            not_found.append((site, url))
    print(f"\n{Fore.RED}Résumé :{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Total trouvés : {Fore.RED}{len(found)}{Style.RESET_ALL}")
    for site, url in found:
        print(f"{Fore.BLUE}- {site} : {Fore.RED}{url}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Total non trouvés : {Fore.RED}{len(not_found)}{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()