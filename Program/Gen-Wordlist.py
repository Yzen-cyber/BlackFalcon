from colorama import Fore, Style, init
import itertools

init(autoreset=True)

print(f"{Fore.RED}=== Générateur de Wordlist Black Falcon ==={Style.RESET_ALL}")
chars = input(f"{Fore.BLUE}Caractères à utiliser (ex: abc123) : {Style.RESET_ALL}").strip()
min_len = int(input(f"{Fore.BLUE}Longueur minimale : {Style.RESET_ALL}"))
max_len = int(input(f"{Fore.BLUE}Longueur maximale : {Style.RESET_ALL}"))
filename = input(f"{Fore.BLUE}Nom du fichier de sortie : {Style.RESET_ALL}").strip()

with open(filename, "w") as f:
    for l in range(min_len, max_len+1):
        for pwd in itertools.product(chars, repeat=l):
            f.write("".join(pwd) + "\n")

print(f"{Fore.GREEN}Wordlist générée dans {filename}{Style.RESET_ALL}")
input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")