from colorama import Fore, Style, init
import socket
import concurrent.futures
import time

init(autoreset=True)

def scan_tcp(ip, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"{Fore.GREEN}[TCP] Port {port} ouvert{Style.RESET_ALL}")
    except Exception:
        pass

def scan_udp(ip, port, timeout=1.0):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(timeout)
            sock.sendto(b"Test", (ip, port))
            try:
                data, _ = sock.recvfrom(1024)
                print(f"{Fore.GREEN}[UDP] Port {port} ouvert (réponse reçue){Style.RESET_ALL}")
            except socket.timeout:
                print(f"{Fore.YELLOW}[UDP] Port {port} (pas de réponse, peut être ouvert ou filtré){Style.RESET_ALL}")
    except Exception:
        pass

def main():
    print(f"{Fore.RED}=== Port Scanner TCP/UDP Black Falcon ==={Style.RESET_ALL}")
    cible = input(f"{Fore.BLUE}IP ou domaine à scanner : {Style.RESET_ALL}").strip()
    try:
        ip = socket.gethostbyname(cible)
    except Exception as e:
        print(f"{Fore.RED}Impossible de résoudre {cible} : {e}{Style.RESET_ALL}")
        return

    port_range = input(f"{Fore.BLUE}Ports à scanner (ex: 1-100,80,443) : {Style.RESET_ALL}").replace(' ', '')
    if '-' in port_range:
        start, end = port_range.split('-')
        ports = range(int(start), int(end)+1)
    elif ',' in port_range:
        ports = [int(p) for p in port_range.split(',') if p.isdigit()]
    elif port_range.isdigit():
        ports = [int(port_range)]
    else:
        ports = [21, 22, 53, 80, 443, 445, 3389, 8080]

    mode = input(f"{Fore.BLUE}Mode (tcp/udp/both) : {Style.RESET_ALL}").strip().lower()
    print(f"{Fore.RED}Scan en cours...{Style.RESET_ALL}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        if mode in ("tcp", "both"):
            for port in ports:
                executor.submit(scan_tcp, ip, port)
        if mode in ("udp", "both"):
            for port in ports:
                executor.submit(scan_udp, ip, port)

    print(f"{Fore.RED}Scan terminé.{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()