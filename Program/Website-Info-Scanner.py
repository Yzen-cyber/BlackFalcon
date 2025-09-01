import socket
import ssl
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import concurrent.futures
from colorama import Fore, Style, init
import time

init(autoreset=True)

def banner():
    print(f"{Fore.RED}=== Website Info Scan Black Falcon ==={Style.RESET_ALL}")

def get_user_agent():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def resolve_url(url):
    if not urlparse(url).scheme:
        url = "https://" + url
    return url

def get_domain(url):
    return urlparse(url).netloc

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.BLUE}IP : {Fore.RED}{ip}{Style.RESET_ALL}")
        return ip
    except Exception as e:
        print(f"{Fore.RED}Impossible de résoudre le domaine : {e}{Style.RESET_ALL}")
        return None

def ip_type(ip):
    if ':' in ip:
        t = "ipv6"
    elif '.' in ip:
        t = "ipv4"
    else:
        t = "Inconnu"
    print(f"{Fore.BLUE}Type IP : {Fore.RED}{t}{Style.RESET_ALL}")

def is_secure(url):
    print(f"{Fore.BLUE}HTTPS : {Fore.RED}{str(url.startswith('https://'))}{Style.RESET_ALL}")

def website_status(url, headers):
    try:
        status_code = requests.get(url, timeout=5, headers=headers, verify=False).status_code
        print(f"{Fore.BLUE}Status Code : {Fore.RED}{status_code}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la requête : {e}{Style.RESET_ALL}")

def ip_info(ip):
    try:
        api = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
        for key in ['country', 'regionName', 'city', 'zip', 'org', 'as']:
            if key in api:
                print(f"{Fore.BLUE}{key.capitalize()} : {Fore.RED}{api[key]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la requête GeoIP : {e}{Style.RESET_ALL}")

def reverse_dns(ip):
    try:
        dns = socket.gethostbyaddr(ip)[0]
        print(f"{Fore.BLUE}Reverse DNS : {Fore.RED}{dns}{Style.RESET_ALL}")
    except:
        print(f"{Fore.BLUE}Reverse DNS : {Fore.RED}Non résolu{Style.RESET_ALL}")

def scan_ports(ip):
    ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }
    print(f"{Fore.BLUE}Scan des ports courants...{Style.RESET_ALL}")
    def scan(port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                if sock.connect_ex((ip, port)) == 0:
                    print(f"{Fore.RED}Port {port} ouvert | Protocole : {Fore.BLUE}{port_protocol_map.get(port, 'Inconnu')}{Style.RESET_ALL}")
        except:
            pass
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan, ports)

def http_headers(url, headers):
    try:
        resp = requests.get(url, timeout=5, headers=headers, verify=False)
        for header, value in resp.headers.items():
            print(f"{Fore.BLUE}Header : {Fore.RED}{header}{Fore.BLUE} → {Fore.RED}{value}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la récupération des headers : {e}{Style.RESET_ALL}")

def ssl_certificate(url):
    try:
        hostname = urlparse(url).hostname
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
            sock.settimeout(5)
            sock.connect((hostname, 443))
            cert = sock.getpeercert()
        print(f"{Fore.BLUE}Certificat SSL :{Style.RESET_ALL}")
        for key, value in cert.items():
            print(f"{Fore.RED}{key}{Fore.BLUE} : {Fore.RED}{value}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur SSL : {e}{Style.RESET_ALL}")

def security_headers(url, headers):
    wanted = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
    try:
        resp = requests.get(url, timeout=5, headers=headers, verify=False)
        for header in wanted:
            if header in resp.headers:
                print(f"{Fore.BLUE}Header sécurité présent : {Fore.RED}{header}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Header sécurité manquant : {Fore.BLUE}{header}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur headers sécurité : {e}{Style.RESET_ALL}")

def analyze_cookies(url, headers):
    try:
        resp = requests.get(url, timeout=5, headers=headers, verify=False)
        for cookie in resp.cookies:
            secure = 'Secure' if cookie.secure else 'Not Secure'
            httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'
            print(f"{Fore.BLUE}Cookie : {Fore.RED}{cookie.name}{Fore.BLUE} | Secure : {Fore.RED}{secure}{Fore.BLUE} | HttpOnly : {Fore.RED}{httponly}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur cookies : {e}{Style.RESET_ALL}")

def detect_technologies(url, headers):
    try:
        resp = requests.get(url, timeout=5, headers=headers, verify=False)
        soup = BeautifulSoup(resp.content, 'html.parser')
        techs = []
        if 'x-powered-by' in resp.headers:
            techs.append(f"X-Powered-By: {resp.headers['x-powered-by']}")
        if 'server' in resp.headers:
            techs.append(f"Server: {resp.headers['server']}")
        for script in soup.find_all('script', src=True):
            if 'jquery' in script['src']:
                techs.append("jQuery")
            if 'bootstrap' in script['src']:
                techs.append("Bootstrap")
        for tech in techs:
            print(f"{Fore.BLUE}Technologie détectée : {Fore.RED}{tech}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur détection techno : {e}{Style.RESET_ALL}")

def main():
    banner()
    user_agent = get_user_agent()
    headers = {"User-Agent": user_agent}
    print(f"{Fore.BLUE}User-Agent : {Fore.RED}{user_agent}{Style.RESET_ALL}")
    url = input(f"{Fore.BLUE}URL du site à scanner : {Style.RESET_ALL}").strip()
    url = resolve_url(url)
    print(f"{Fore.BLUE}Scan en cours...{Style.RESET_ALL}")
    domain = get_domain(url)
    ip = get_ip(domain)
    if not ip:
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
        return
    ip_type(ip)
    is_secure(url)
    website_status(url, headers)
    ip_info(ip)
    reverse_dns(ip)
    scan_ports(ip)
    http_headers(url, headers)
    ssl_certificate(url)
    security_headers(url, headers)
    analyze_cookies(url, headers)
    detect_technologies(url, headers)
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()