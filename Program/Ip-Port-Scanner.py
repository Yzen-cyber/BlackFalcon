import socket
import concurrent.futures
import requests
from colorama import Fore, Style, init
import time

init(autoreset=True)

def infos_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        return {
            "Pays": data.get("country", "Inconnu"),
            "Ville": data.get("city", "Inconnue"),
            "Organisation": data.get("org", "Inconnu"),
            "ASN": data.get("as", "Inconnu"),
            "Région": data.get("regionName", "Inconnue"),
            "Code postal": data.get("zip", "Inconnu"),
            "Fuseau horaire": data.get("timezone", "Inconnue"),
            "Latitude": data.get("lat", "Inconnu"),
            "Longitude": data.get("lon", "Inconnu")
        }
    except:
        return {}

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Non résolu"

def identify_protocol(port):
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 135: "MS RPC", 137: "NetBIOS", 138: "NetBIOS", 139: "NetBIOS",
        143: "IMAP", 161: "SNMP", 194: "IRC", 389: "LDAP", 443: "HTTPS", 445: "SMB", 465: "SMTPS",
        514: "Syslog", 587: "SMTP Submission", 631: "IPP", 993: "IMAPS", 995: "POP3S", 1080: "SOCKS",
        1433: "MSSQL", 1521: "Oracle DB", 1723: "PPTP", 2049: "NFS", 2082: "cPanel", 2083: "cPanel SSL",
        2181: "Zookeeper", 2222: "DirectAdmin", 2375: "Docker", 2376: "Docker SSL", 2483: "Oracle DB",
        2484: "Oracle DB SSL", 25565: "Minecraft", 2601: "Zebra", 3128: "Squid Proxy", 3306: "MySQL",
        3389: "RDP", 3690: "Subversion", 4000: "ICQ", 4040: "HTTP Proxy", 4369: "EPMAP", 5000: "UPnP",
        5432: "PostgreSQL", 5631: "pcAnywhere", 5900: "VNC", 5984: "CouchDB", 6379: "Redis",
        6660: "IRC", 6667: "IRC", 7001: "Splunk", 8000: "HTTP Alt", 8008: "HTTP Alt", 8080: "HTTP Proxy",
        8081: "HTTP Proxy", 8443: "HTTPS Alt", 8888: "HTTP Alt", 9200: "Elasticsearch", 11211: "Memcached",
        27017: "MongoDB", 27018: "MongoDB", 27019: "MongoDB"
    }
    return port_protocol_map.get(port, "Inconnu")

def scan_port(ip, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                protocol = identify_protocol(port)
                print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Port: {Fore.BLUE}{port:<5}{Fore.RED} | Statut: {Fore.GREEN}OUVERT{Fore.RED} | Protocole: {Fore.BLUE}{protocol}{Style.RESET_ALL}")
    except Exception:
        pass

def check_host_tcp(host, port=80):
    try:
        url = f"https://check-host.net/check-tcp?host={host}:{port}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and "request_id" in r.text:
            print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Requête envoyée à check-host.net...{Style.RESET_ALL}")
            request_id = r.json()["request_id"]
            time.sleep(3)
            result_url = f"https://check-host.net/check-result/{request_id}"
            result = requests.get(result_url, timeout=10).json()
            for node, data in result.items():
                if data and isinstance(data, list) and data[0] and data[0][0] == 'OK':
                    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Node: {Fore.BLUE}{node}{Fore.RED} | {Fore.GREEN}OUVERT{Style.RESET_ALL}")
                else:
                    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Node: {Fore.BLUE}{node}{Fore.RED} | {Fore.RED}FERMÉ ou INJOIGNABLE{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Erreur lors de la requête à check-host.net{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.RED}=== IP Port Scanner Black Falcon ==={Style.RESET_ALL}")
    cible = input(f"{Fore.BLUE}Entrez l'IP ou le domaine à scanner : {Style.RESET_ALL}").strip()
    try:
        ip = socket.gethostbyname(cible)
        print(f"{Fore.RED}Adresse IP résolue : {ip}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Impossible de résoudre {cible} : {e}{Style.RESET_ALL}")
        return

    infos = infos_ip(ip)
    print(f"{Fore.RED}--- Informations sur l'IP ---{Style.RESET_ALL}")
    for k, v in infos.items():
        print(f"{Fore.BLUE}{k} : {Fore.RED}{v}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Reverse DNS : {Fore.RED}{reverse_dns(ip)}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Google Maps : {Fore.RED}https://www.google.com/maps/search/?api=1&query={infos.get('Latitude','')},{infos.get('Longitude','')}{Style.RESET_ALL}")

    port_range = input(f"{Fore.BLUE}Ports à scanner (ex: 1-65535, 80,443,8080 ou vide pour ports populaires) : {Style.RESET_ALL}").replace(' ', '')
    if '-' in port_range:
        start, end = port_range.split('-')
        ports = range(int(start), int(end)+1)
    elif ',' in port_range:
        ports = [int(p) for p in port_range.split(',') if p.isdigit()]
    elif port_range.isdigit():
        ports = [int(port_range)]
    else:
        ports = [21, 22, 23, 25, 53, 69, 80, 110, 123, 135, 137, 138, 139, 143, 161, 194, 389, 443, 445, 465, 514, 587, 631, 993, 995, 1080, 1433, 1521, 1723, 2049, 2082, 2083, 2181, 2222, 2375, 2376, 2483, 2484, 25565, 2601, 3128, 3306, 3389, 3690, 4000, 4040, 4369, 5000, 5432, 5631, 5900, 5984, 6379, 6660, 6667, 7001, 8000, 8008, 8080, 8081, 8443, 8888, 9200, 11211, 27017, 27018, 27019]

    print(f"{Fore.RED}Scan local en cours...{Style.RESET_ALL}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(scan_port, ip, port, 1.0) for port in ports]
        concurrent.futures.wait(futures)

    print(f"{Fore.RED}Scan local terminé.{Style.RESET_ALL}")

    # Propose un scan externe via check-host.net
    ext = input(f"{Fore.BLUE}Voulez-vous tester un port via check-host.net ? (y/n) : {Style.RESET_ALL}").strip().lower()
    if ext == "y":
        port_ext = input(f"{Fore.BLUE}Port à tester (défaut 80) : {Style.RESET_ALL}").strip()
        port_ext = int(port_ext) if port_ext.isdigit() else 80
        check_host_tcp(cible, port_ext)

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()