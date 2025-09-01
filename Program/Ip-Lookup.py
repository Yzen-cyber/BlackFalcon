import requests
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Non résolu"

def main():
    print(f"{Fore.RED}=== Recherche GeoIP Black Falcon ==={Style.RESET_ALL}")
    cible = input(f"{Fore.BLUE}Entrez l'IP ou le domaine : {Style.RESET_ALL}").strip()
    try:
        ip = socket.gethostbyname(cible)
        print(f"{Fore.RED}Adresse IP résolue : {ip}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Impossible de résoudre {cible} : {e}{Style.RESET_ALL}")
        return

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        print(f"{Fore.RED}--- Informations GeoIP ---{Style.RESET_ALL}")
        for k in ["query", "country", "regionName", "city", "zip", "lat", "lon", "org", "as", "timezone"]:
            print(f"{Fore.BLUE}{k} : {Fore.RED}{data.get(k, 'Inconnu')}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Reverse DNS : {Fore.RED}{reverse_dns(ip)}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Google Maps : {Fore.RED}https://www.google.com/maps/search/?api=1&query={data.get('lat')},{data.get('lon')}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Erreur lors de la requête GeoIP : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()