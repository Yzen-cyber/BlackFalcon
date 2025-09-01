import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except ImportError:
    print(f"{Fore.RED}Le module selenium n'est pas installé. Installe-le avec : pip install selenium{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
    sys.exit(1)

def main():
    print(f"{Fore.RED}=== Roblox Cookie Login Black Falcon ==={Style.RESET_ALL}")
    cookie = input(f"{Fore.BLUE}Cookie ROBLOSECURITY : {Style.RESET_ALL}").strip()
    print(f"""
{Fore.RED}01{Style.RESET_ALL} Chrome (Windows/Linux)
{Fore.RED}02{Style.RESET_ALL} Edge (Windows)
{Fore.RED}03{Style.RESET_ALL} Firefox (Windows)
""")
    browser = input(f"{Fore.BLUE}Choix du navigateur (1-3) : {Style.RESET_ALL}").strip()

    driver = None
    navigator = ""
    try:
        if browser in ['1', '01']:
            navigator = "Chrome"
            print(f"{Fore.RED}Démarrage de Chrome...{Style.RESET_ALL}")
            driver = webdriver.Chrome()
        elif browser in ['2', '02']:
            navigator = "Edge"
            print(f"{Fore.RED}Démarrage de Edge...{Style.RESET_ALL}")
            driver = webdriver.Edge()
        elif browser in ['3', '03']:
            navigator = "Firefox"
            print(f"{Fore.RED}Démarrage de Firefox...{Style.RESET_ALL}")
            driver = webdriver.Firefox()
        else:
            print(f"{Fore.RED}Choix invalide.{Style.RESET_ALL}")
            input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
            return

        driver.get("https://www.roblox.com/Login")
        time.sleep(2)
        print(f"{Fore.RED}Connexion avec le cookie...{Style.RESET_ALL}")
        driver.add_cookie({"name": ".ROBLOSECURITY", "value": cookie})
        driver.refresh()
        time.sleep(2)
        driver.get("https://www.roblox.com/users/profile")
        print(f"{Fore.RED}Connecté ! Le navigateur reste ouvert tant que le script tourne.{Style.RESET_ALL}")
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter et fermer le navigateur.{Style.RESET_ALL}")
        driver.quit()
    except Exception as e:
        print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")
        if driver:
            driver.quit()
        input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()