import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re
import concurrent.futures
from colorama import Fore, Style, init
import time

init(autoreset=True)

def banner():
    print(f"""{Fore.RED}
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗      █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██║ ██╔╝██║██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██████╔╝█████╔╝██║███████╗█████╔╝ ██║██╔██╗ ██║██║  ███╗    ███████║   ██║      ██║   ███████║██║     █████╔╝ 
██╔═══╝ ██╔═██╗██║╚════██║██╔═██╗ ██║██║╚██╗██║██║   ██║    ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
██║     ██║  ██╗██║███████║██║  ██╗██║██║ ╚████║╚██████╔╝    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Style.RESET_ALL}""")

def get_user_agent():
    # Liste simple d'user-agents, tu peux l'étendre
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
    ]
    import random
    return random.choice(agents)

def fetch_and_inline_css_js(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')

    # CSS
    css_links = soup.find_all('link', rel='stylesheet')
    css_urls = [urljoin(base_url, link['href']) for link in css_links if link.get('href')]
    all_css = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        css_responses = executor.map(lambda url: requests.get(url, timeout=5), css_urls)
        for css_response in css_responses:
            if css_response.status_code == 200:
                all_css.append(css_response.text)
    if all_css:
        style_tag = soup.new_tag('style')
        style_tag.string = "\n".join(all_css)
        soup.head.append(style_tag)
        for link in css_links:
            link.decompose()

    # JS
    script_links = soup.find_all('script', src=True)
    js_urls = [urljoin(base_url, script['src']) for script in script_links if script.get('src')]
    all_js = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        js_responses = executor.map(lambda url: requests.get(url, timeout=5), js_urls)
        for js_response in js_responses:
            if js_response.status_code == 200:
                all_js.append(js_response.text)
    if all_js:
        script_tag = soup.new_tag('script')
        script_tag.string = "\n".join(all_js)
        soup.body.append(script_tag)
        for script in script_links:
            script.decompose()

    return soup.prettify()

def main():
    banner()
    user_agent = get_user_agent()
    headers = {"User-Agent": user_agent}
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}User-Agent sélectionné : {Fore.BLUE}{user_agent}{Style.RESET_ALL}")

    website_url = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}URL du site à cloner : {Style.RESET_ALL}").strip()
    if not website_url.startswith("http"):
        website_url = "https://" + website_url

    try:
        print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Récupération du HTML...{Style.RESET_ALL}")
        session = requests.Session()
        response = session.get(website_url, headers=headers, timeout=10)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            file_name = re.sub(r'[\\/:*?"<>|]', '-', soup.title.string if soup.title else 'Phishing')
            output_dir = os.path.join(os.getcwd(), "1-Output", "PhishingAttack")
            os.makedirs(output_dir, exist_ok=True)
            file_html = os.path.join(output_dir, f"{file_name}.html")

            print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Récupération et intégration CSS/JS...{Style.RESET_ALL}")
            final_html = fetch_and_inline_css_js(html_content, website_url)

            with open(file_html, 'w', encoding='utf-8') as file:
                file.write(final_html)
            print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Succès. Le fichier est dans : {Fore.BLUE}{file_html}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Erreur HTTP : {response.status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()