import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(f"{Fore.RED}=== Website URL Scanner Black Falcon ==={Style.RESET_ALL}")

def get_user_agent():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def is_valid_extension(url):
    return re.search(r'\.(html|xhtml|php|js|css)$', url) or not re.search(r'\.\w+$', url)

def extract_links(base_url, domain, tags, all_links):
    extracted_links = []
    for tag in tags:
        attr = tag.get('href') or tag.get('src') or tag.get('action')
        if attr:
            full_url = urljoin(base_url, attr)
            if full_url not in all_links and domain in full_url and is_valid_extension(full_url):
                extracted_links.append(full_url)
                all_links.append(full_url)
    return extracted_links

def extract_links_from_script(scripts, domain, all_links):
    extracted_links = []
    for script in scripts:
        if script.string:
            urls_in_script = re.findall(r'(https?://\S+)', script.string)
            for url in urls_in_script:
                if url not in all_links and domain in url and is_valid_extension(url):
                    extracted_links.append(url)
                    all_links.append(url)
    return extracted_links

def find_secret_urls(website_url, domain, headers, all_links):
    try:
        response = requests.get(website_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"{Fore.RED}Erreur HTTP : {response.status_code} pour {website_url}{Style.RESET_ALL}")
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        tags = soup.find_all(['a', 'link', 'script', 'img', 'iframe', 'button', 'form'])
        extracted_links = extract_links(website_url, domain, tags, all_links)
        extracted_links += extract_links_from_script(soup.find_all('script'), domain, all_links)
        for link in extracted_links:
            print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Url trouvée : {Fore.BLUE}{link}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la récupération des liens : {e}{Style.RESET_ALL}")

def find_all_secret_urls(website_url, domain, headers):
    all_links = []
    find_secret_urls(website_url, domain, headers, all_links)
    visited_links = set()
    while True:
        new_links = [link for link in all_links if link not in visited_links]
        if not new_links:
            break
        for link in new_links:
            try:
                resp = requests.get(link, headers=headers, timeout=10)
                if resp.status_code == 200:
                    find_secret_urls(link, domain, headers, all_links)
                    visited_links.add(link)
            except:
                visited_links.add(link)
    print(f"{Fore.RED}Total de liens trouvés : {Fore.BLUE}{len(all_links)}{Style.RESET_ALL}")

def main():
    banner()
    user_agent = get_user_agent()
    headers = {"User-Agent": user_agent}
    print(f"{Fore.BLUE}User-Agent sélectionné : {Fore.RED}{user_agent}{Style.RESET_ALL}")
    website_url = input(f"{Fore.BLUE}Website Url -> {Style.RESET_ALL}").strip()
    if not website_url.startswith("http"):
        website_url = "https://" + website_url
    domain = urlparse(website_url).netloc
    print(f"""
 {Fore.BLUE}01{Fore.RED} Uniquement la page
 {Fore.BLUE}02{Fore.RED} Tout le site (profond)
    """)
    choice = input(f"{Fore.BLUE}Choix -> {Style.RESET_ALL}").strip()
    if choice in ['1', '01']:
        find_secret_urls(website_url, domain, headers, [])
    elif choice in ['2', '02']:
        find_all_secret_urls(website_url, domain, headers)
    else:
        print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()