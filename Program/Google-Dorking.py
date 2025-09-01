import webbrowser
from colorama import Fore, Style, init
import time

init(autoreset=True)

def banner():
    print(f"{Fore.RED}=== Google Dorking Black Falcon ==={Style.RESET_ALL}")

def main():
    banner()
    url = "https://www.google.com/search?q="
    database = []

    print(f"""{Fore.RED}
 {Fore.BLUE}00{Fore.RED} Lancer la recherche
 {Fore.BLUE}01{Fore.RED} Mot-clé dans l'URL d'un site (inurl:)
 {Fore.BLUE}02{Fore.RED} Mot-clé dans le titre d'un site (intitle:)
 {Fore.BLUE}03{Fore.RED} Spécifier un site (site:)
 {Fore.BLUE}04{Fore.RED} Mot-clé exact dans les pages ("mot")
 {Fore.BLUE}05{Fore.RED} Mot-clé exclu des pages (-mot)
 {Fore.BLUE}06{Fore.RED} Extension de fichier (filetype:)
""")
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Plusieurs choix possibles, tape '00' pour lancer la recherche.{Style.RESET_ALL}")

    while True:
        choice = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Méthode de recherche -> {Style.RESET_ALL}").strip()
        if choice in ['0', '00']:
            break
        elif choice in ['1', '01']:
            request = "inurl:" + input(f"{Fore.BLUE}Mot-clé -> {Style.RESET_ALL}")
            database.append(request)
        elif choice in ['2', '02']:
            request = "intitle:" + input(f"{Fore.BLUE}Mot-clé -> {Style.RESET_ALL}")
            database.append(request)
        elif choice in ['3', '03']:
            request = "site:" + input(f"{Fore.BLUE}Domaine -> {Style.RESET_ALL}")
            database.append(request)
        elif choice in ['4', '04']:
            request = '"' + input(f"{Fore.BLUE}Mot-clé exact -> {Style.RESET_ALL}") + '"'
            database.append(request)
        elif choice in ['5', '05']:
            request = "-" + input(f"{Fore.BLUE}Mot-clé à exclure -> {Style.RESET_ALL}")
            database.append(request)
        elif choice in ['6', '06']:
            request = "filetype:" + input(f"{Fore.BLUE}Extension -> {Style.RESET_ALL}")
            database.append(request)
        else:
            print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")

    total_request = " ".join(database)
    search_url = url + total_request
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Requête totale : {Fore.BLUE}{total_request}{Style.RESET_ALL}")
    webbrowser.open(search_url.replace(" ", "%20").replace("\"", "%22"))
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}La page Google est lancée.{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()