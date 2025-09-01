import subprocess
import platform
import time
from colorama import Fore, Style, init

init(autoreset=True)

def ping_ip(host, count=4, timeout=1000):
    param_count = "-n" if platform.system().lower() == "windows" else "-c"
    param_timeout = "-w" if platform.system().lower() == "windows" else "-W"
    cmd = ["ping", param_count, str(count), param_timeout, str(timeout), host]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
        lines = output.splitlines()
        for line in lines:
            if "TTL=" in line or "ttl=" in line:
                print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Hôte: {Fore.BLUE}{host}{Fore.RED} | {Fore.BLUE}RÉPONSE{Style.RESET_ALL}")
            elif "Request timed out" in line or "Délai d’attente" in line or "100% packet loss" in line:
                print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Hôte: {Fore.BLUE}{host}{Fore.RED} | {Fore.RED}AUCUNE RÉPONSE{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Erreur lors du ping : {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.RED}=== IP Pinger Black Falcon ==={Style.RESET_ALL}")
    host = input(f"{Fore.BLUE}IP ou domaine à pinger : {Style.RESET_ALL}").strip()
    count_input = input(f"{Fore.BLUE}Nombre de pings (défaut 4, 0 = infini) : {Style.RESET_ALL}").strip()
    count = int(count_input) if count_input and count_input != "0" else 4
    timeout_input = input(f"{Fore.BLUE}Timeout en ms (défaut 1000) : {Style.RESET_ALL}").strip()
    timeout = int(timeout_input) if timeout_input else 1000

    try:
        if count_input == "0":
            while True:
                ping_ip(host, count=1, timeout=timeout)
                time.sleep(1)
        else:
            ping_ip(host, count=count, timeout=timeout)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Arrêté par l'utilisateur.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()