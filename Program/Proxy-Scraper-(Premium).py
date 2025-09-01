from colorama import Fore, Style, init
import webbrowser
import time

init(autoreset=True)

def main():
    print(f"""{Fore.RED}
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝╚██╗ ██╔╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║   ██║█████╔╝  ╚████╔╝     ███████╗██║     ██████╔╝███████║██████╔╝███████╗
██╔═══╝ ██╔══██╗██║   ██║██╔═██╗   ╚██╔╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ╚════██║
██║     ██║  ██║╚██████╔╝██║  ██╗   ██║       ███████║╚██████╗██║  ██║██║  ██║██║     ███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝
{Style.RESET_ALL}""")
    print(f"{Fore.RED}Ce produit est premium et disponible uniquement sur notre Telegram.{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Ouverture du lien Telegram...{Style.RESET_ALL}")
    time.sleep(1)
    webbrowser.open_new_tab("https://t.me/RedTigerTools")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()