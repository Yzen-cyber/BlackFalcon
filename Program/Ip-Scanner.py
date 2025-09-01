import socket
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def infos_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
        pays = data.get("country", "Inconnu")
        ville = data.get("city", "Inconnue")
        org = data.get("org", "Inconnu")
        asn = data.get("as", "Inconnu")
        region = data.get("regionName", "Inconnue")
        code_postal = data.get("zip", "Inconnu")
        timezone = data.get("timezone", "Inconnue")
        lat = data.get("lat", "Inconnu")
        lon = data.get("lon", "Inconnu")
        return {
            "Pays": pays,
            "Ville": ville,
            "Région": region,
            "Code postal": code_postal,
            "Fuseau horaire": timezone,
            "Latitude": lat,
            "Longitude": lon,
            "Organisation": org,
            "ASN": asn
        }
    except:
        return {
            "Pays": "Inconnu",
            "Ville": "Inconnue",
            "Région": "Inconnue",
            "Code postal": "Inconnu",
            "Fuseau horaire": "Inconnue",
            "Latitude": "Inconnu",
            "Longitude": "Inconnu",
            "Organisation": "Inconnu",
            "ASN": "Inconnu"
        }

def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Non résolu"

def scan_ports(target, ports):
    print(f"{Fore.BLUE}Scan des ports sur {target}...{Style.RESET_ALL}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Fore.RED}Port {port} ouvert{Style.RESET_ALL}")
                try:
                    service = socket.getservbyport(port)
                    print(f"{Fore.BLUE}  → Service : {service}{Style.RESET_ALL}")
                except:
                    pass
            else:
                print(f"{Fore.BLUE}Port {port} fermé{Style.RESET_ALL}")
            sock.close()
        except Exception as e:
            print(f"{Fore.RED}Erreur sur le port {port} : {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.RED}=== Scanner de ports IP Black Falcon ==={Style.RESET_ALL}")
    cible = input(f"{Fore.BLUE}Entrez l'IP ou le domaine à scanner : {Style.RESET_ALL}").strip()
    try:
        cible_ip = socket.gethostbyname(cible)
        print(f"{Fore.RED}Adresse IP résolue : {cible_ip}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Impossible de résoudre {cible} : {e}{Style.RESET_ALL}")
        return

    # Infos IP
    infos = infos_ip(cible_ip)
    rdns = reverse_dns(cible_ip)
    print(f"{Fore.RED}--- Informations sur l'IP ---{Style.RESET_ALL}")
    for k, v in infos.items():
        print(f"{Fore.BLUE}{k} : {Fore.RED}{v}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Reverse DNS : {Fore.RED}{rdns}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Google Maps : {Fore.RED}https://www.google.com/maps/search/?api=1&query={infos['Latitude']},{infos['Longitude']}{Style.RESET_ALL}")

    choix = input(f"{Fore.BLUE}Ports à scanner (ex: 21,22,80 ou 1-1024) : {Style.RESET_ALL}").strip()
    ports = set()
    for part in choix.split(','):
        if '-' in part:
            start, end = part.split('-')
            ports.update(range(int(start), int(end)+1))
        else:
            try:
                ports.add(int(part))
            except:
                pass
    if not ports:
        ports = {21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389}

    scan_ports(cible_ip, sorted(ports))
    input(f"{Fore.RED}Scan terminé. Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()