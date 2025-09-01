import os
import sys
import time
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)

def center(text, width=100):
    lines = text.split('\n')
    return '\n'.join(line.center(width) for line in lines)

def print_slow(text, delay=0.001):  # effet d'écriture ultra rapide
    for char in text:
        print(Fore.RED + char + Style.RESET_ALL, end='', flush=True)
        time.sleep(delay)
    print()

def afficher_ascii_art():
    ascii_art = """
    
 /$$   /$$             /$$            /$$$$$$                                  /$$                        
| $$$ | $$            | $$           /$$__  $$                                | $$                        
| $$$$| $$  /$$$$$$  /$$$$$$        | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$__  $$|_  $$_/        |  $$$$$$  /$$__  $$ /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$$| $$$$$$$$  | $$           \____  $$| $$  \ $$| $$$$$$$$| $$        | $$    | $$  \__/| $$$$$$$$
| $$\  $$$| $$_____/  | $$ /$$       /$$  \ $$| $$  | $$| $$_____/| $$        | $$ /$$| $$      | $$_____/
| $$ \  $$|  $$$$$$$  |  $$$$/      |  $$$$$$/| $$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$      |  $$$$$$$
|__/  \__/ \_______/   \___/         \______/ | $$____/  \_______/ \_______/   \___/  |__/       \_______/
                                              | $$                                                        
                                              | $$                                                        
                                              |__/                                                     
"""
    os.system('cls' if os.name == 'nt' else 'clear')
    for line in ascii_art.split('\n'):
        print(Fore.RED + center(line) + Style.RESET_ALL)

def afficher_descriptif():
    desc = (
        "\n"
        "Author: Yzen\n"
        "Tool Name: NetSpectre\n"
        "Description:\n"
        "NetSpectre is an advanced multi-tool for cybersecurity and OSINT on Windows.\n"
        "It provides modules for network analysis, information gathering, automation,\n"
        "penetration testing, and more. Use it for learning, auditing, and legal research only.\n"
        "\n"
        "Press [D] at any time to open the Discord invite."
    )
    print()
    for line in desc.split('\n'):
        print_slow(center(line))
    print()
    print_slow(center("Press Enter to continue..."))
    input()

# Show logo and description at launch
afficher_ascii_art()
afficher_descriptif()

# --- Couleurs personnalisées ---
main_color   = Fore.RED
accent_color = Fore.RED
title_color  = Fore.RED
menu_color   = Fore.RED
info_color   = Fore.RED
reset        = Style.RESET_ALL

# --- Définition des options (noms de fichiers SANS .py) ---
options = {
    '1': "Website-Vulnerability-Scanner",
    '2': "Website-Info-Scanner",
    '3': "Website-Url-Scanner",
    '4': "Ip-Scanner",
    '5': "Ip-Port-Scanner",
    '6': "Ip-Pinger",
    '7': "Dox-Create",
    '8': "D0x-Tracker",
    '9': "Get-Image-Exif",
    '10': "Google-Dorking",
    '11': "Username-Tracker",
    '12': "Email-Tracker",
    '13': "Email-Lookup",
    '14': "Phone-Number-Lookup",
    '15': "Ip-Lookup",
    '16': "Instagram-Account",
    '17': "Phishing-Attack",
    '18': "Password-Zip-Cracked-Attack",
    '19': "Password-Hash-Decrypted-Attack",
    '20': "Password-Hash-Encrypted",
    '21': "Search-In-Database",
    '22': "Dark-Web-Links",
    '23': "Ip-Generator",
    '24': "Virus-Builder",
    '25': "Python-Obfuscator",
    '26': "Discord-Rat-(Premium)",
    '27': "Website-Dos",
    '28': "Proxy-Scraper",
    '29': "Roblox-Cookie-Login",
    '30': "Roblox-Cookie-Info",
    '31': "Roblox-Id-Info",
    '32': "Roblox-User-Info",
    '33': "Discord-Nitro-Generator",
    '34': "Ouvrir-discord-nuker.exe",
    '35': "Discord-Bot-Invite-To-Id",
    '36': "Discord-Server-Info",
    '37': "Discord-Webhook-Delete",
    '38': "Discord-Webhook-Generator",
    '39': "Discord-Webhook-Info",
    '40': "Discord-Webhook-Spammer"
}

def menu1():
    menu = f"""
[I] Info    [S] Site    [D] Discord                                                                                 [N] Next

├─ Analyse Réseau ──────────────┬─ Osint ───────────────────────────────┬─ Utilitaires ──────────────────────────────┐
│ [1] Scan vulnérabilité Web    │ [7] Dox Create                        │ [17] Phishing Attack                       │
│ [2] Scan infos Web            │ [8] Dox Tracker                       │ [18] Password Zip Crack                    │
│ [3] Scan URL Web              │ [9] Image Exif                        │ [19] Hash Decrypt                          │
│ [4] Scan IP                   │ [10] Google Dorking                   │ [20] Hash Encrypt                          │
│ [5] Scan ports IP             │ [11] Username Tracker                 │ [21] Search DB                             │
│ [6] Pinger IP                 │ [12] Email Tracker                    │ [22] Dark Web Links                        │
│                               │ [13] Email Lookup                     │ [23] Générateur IP                         │
│                               │ [14] Phone Lookup                     │                                            │
│                               │ [15] IP Lookup                        │                                            │
│                               │ [16] Instagram Account                │                                            │
└───────────────────────────────┴───────────────────────────────────────┴────────────────────────────────────────────┘
"""
    lines = menu.split('\n')
    for line in lines:
        print(Fore.RED + center(line) + Style.RESET_ALL)
    return ""

def menu2():
    menu = f"""
[I] Info    [S] Site    [D] Discord                                                                                 [N] Next   [B] Back

├─ Outils Avancés ──────────────┬─ Roblox ──────────────────────────────┬─ Divers ───────────────────────────────────────────────────────────────┐
│ [24] Virus Builder            │ [29] Roblox Cookie Login              │ [33] Nitro Generator Discord                                           │
│ [25] Python Obfuscator        │ [30] Roblox Cookie Info               │ [34] discord-nuker.exe                                                 │
│ [26] Discord RAT (Premium)    │ [31] Roblox ID Info                   │ [35] Discord-Bot-Invite-To-Id                                          │
│ [27] Website DoS              │ [32] Roblox User Info                 │ [36] Discord-Server-Info                                               │
│ [28] Proxy Scraper            │                                       │ [37] Discord-Webhook-Delete                                            │
│                               │                                       │ [38] Discord-Webhook-Generator                                         │
│                               │                                       │ [39] Discord-Webhook-Info                                              │
│                               │                                       │ [40] Discord-Webhook-Spammer                                           │
└───────────────────────────────┴───────────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
"""
    lines = menu.split('\n')
    for line in lines:
        print(Fore.RED + center(line) + Style.RESET_ALL)
    return ""

def afficher_banniere():
    banniere = f"""

 /$$   /$$             /$$            /$$$$$$                                  /$$                        
| $$$ | $$            | $$           /$$__  $$                                | $$                        
| $$$$| $$  /$$$$$$  /$$$$$$        | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$__  $$|_  $$_/        |  $$$$$$  /$$__  $$ /$$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$$| $$$$$$$$  | $$           \____  $$| $$  \ $$| $$$$$$$$| $$        | $$    | $$  \__/| $$$$$$$$
| $$\  $$$| $$_____/  | $$ /$$       /$$  \ $$| $$  | $$| $$_____/| $$        | $$ /$$| $$      | $$_____/
| $$ \  $$|  $$$$$$$  |  $$$$/      |  $$$$$$/| $$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$      |  $$$$$$$
|__/  \__/ \_______/   \___/         \______/ | $$____/  \_______/ \_______/   \___/  |__/       \_______/
                                              | $$                                                        
                                              | $$                                                        
                                              |__/                                                        

"""
    for line in banniere.split('\n'):
        print(Fore.RED + center(line) + Style.RESET_ALL)
    print(Fore.RED + center('NetSpectre - Outils pentest, CyberCriminalité, CyberSécurité, Informations'.center(100)) + Style.RESET_ALL)

def afficher_menu(page):
    os.system('cls' if os.name == 'nt' else 'clear')
    afficher_banniere()
    if page == 1:
        menu1()
    elif page == 2:
        menu2()

def lancer_script(nom_script):
    if nom_script == "Ouvrir-discord-nuker.exe" or nom_script == "discord-nuker.exe":
        exe_path = os.path.join(os.getcwd(), "discord-nuker.exe")
        if os.path.exists(exe_path):
            print(Fore.RED + center("discord-nuker.exe a été ouvert !") + Style.RESET_ALL)
            os.startfile(exe_path)
        else:
            print(Fore.RED + center("discord-nuker.exe introuvable à cet emplacement : " + exe_path) + Style.RESET_ALL)
        print(Fore.RED + center("Appuyez sur Entrée pour continuer...") + Style.RESET_ALL)
        input()
        return
    chemin = os.path.join("Program", f"{nom_script}.py")
    if os.path.exists(chemin):
        os.system(f'python "{chemin}"')
    else:
        print(Fore.RED + center(f"Script {chemin} introuvable.") + Style.RESET_ALL)
        print(Fore.RED + center("Appuyez sur Entrée pour continuer...") + Style.RESET_ALL)
        input()

def ouvrir_invite_discord():
    # Remplace le lien ci-dessous par ton vrai lien d'invitation Discord si besoin
    invite_url = "https://discord.gg/psEmGwp4XF"
    print(Fore.RED + center("Opening Discord invite...") + Style.RESET_ALL)
    webbrowser.open(invite_url)

def main():
    page = 1
    while True:
        afficher_menu(page)
        prompt = center("Votre choix : ")
        choix = input(Fore.RED + prompt + Style.RESET_ALL).strip()
        if choix.upper() == 'D':
            ouvrir_invite_discord()
            print(Fore.RED + center("Appuyez sur Entrée pour continuer...") + Style.RESET_ALL)
            input()
            continue
        if choix.upper() in ['N', 'NEXT']:
            page = 1 if page == 2 else page + 1
            continue
        elif choix.upper() in ['B', 'BACK']:
            page = 2 if page == 1 else page - 1
            continue
        elif choix.upper() in ['I', 'INFO']:
            lancer_script("Info")
            continue
        elif choix.upper() in ['S', 'SITE']:
            lancer_script("Site")
            continue
        elif choix in options:
            lancer_script(options[choix])
            continue
        elif choix.startswith('0') and choix[1:] in options:
            lancer_script(options[choix[1:]])
            continue
        elif choix == '24':
            print(Fore.RED + center("Attention : Le builder de virus est réservé à Windows et peut être détecté par l'antivirus.") + Style.RESET_ALL)
            print(Fore.RED + center("Appuyez sur Entrée pour continuer...") + Style.RESET_ALL)
            input()
            lancer_script(options['24'])
            continue
        elif choix.upper() in ['Q', 'QUIT', 'EXIT']:
            print(Fore.RED + center("Fermeture de Black Falcon.") + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + center("Choix invalide.") + Style.RESET_ALL)
            print(Fore.RED + center("Appuyez sur Entrée pour continuer...") + Style.RESET_ALL)
            input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + center("Arrêté par l'utilisateur.") + Style.RESET_ALL)
    print(Fore.RED + center("Appuyez sur Entrée pour quitter...") + Style.RESET_ALL)
    input()