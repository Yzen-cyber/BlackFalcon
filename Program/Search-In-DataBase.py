import os
from colorama import Fore, Style, init
import tkinter as tk
from tkinter import filedialog

init(autoreset=True)

def choose_folder():
    print(f"{Fore.RED}=== Search In DataBase Black Falcon ==={Style.RESET_ALL}")
    try:
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        folder = filedialog.askdirectory(title="Choisissez le dossier de la base de données")
        if not folder:
            raise Exception("Aucun dossier sélectionné.")
        print(f"{Fore.BLUE}Dossier sélectionné : {Fore.RED}{folder}{Style.RESET_ALL}")
    except Exception:
        folder = input(f"{Fore.BLUE}Chemin du dossier à scanner : {Style.RESET_ALL}").strip()
    return folder

def search_in_files(folder, search):
    files_searched = 0
    results_found = False
    for root_dir, dirs, files in os.walk(folder):
        for file in files:
            chemin_element = os.path.join(root_dir, file)
            try:
                with open(chemin_element, 'r', encoding='utf-8') as f:
                    line_number = 0
                    files_searched += 1
                    for line in f:
                        line_number += 1
                        if search in line:
                            results_found = True
                            line_info = line.strip().replace(search, f"{Fore.YELLOW}{search}{Fore.RED}")
                            print(f"""{Fore.RED}
- Dossier : {Fore.BLUE}{root_dir}{Fore.RED}
- Fichier : {Fore.BLUE}{file}{Fore.RED}
- Ligne   : {Fore.BLUE}{line_number}{Fore.RED}
- Résultat: {Fore.BLUE}{line_info}{Style.RESET_ALL}
""")
            except UnicodeDecodeError:
                try:
                    with open(chemin_element, 'r', encoding='latin-1') as f:
                        line_number = 0
                        files_searched += 1
                        for line in f:
                            line_number += 1
                            if search in line:
                                results_found = True
                                line_info = line.strip().replace(search, f"{Fore.YELLOW}{search}{Fore.RED}")
                                print(f"""{Fore.RED}
- Dossier : {Fore.BLUE}{root_dir}{Fore.RED}
- Fichier : {Fore.BLUE}{file}{Fore.RED}
- Ligne   : {Fore.BLUE}{line_number}{Fore.RED}
- Résultat: {Fore.BLUE}{line_info}{Style.RESET_ALL}
""")
                except Exception as e:
                    print(f"{Fore.RED}Erreur de lecture du fichier {file} : {e}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Erreur de lecture du fichier {file} : {e}{Style.RESET_ALL}")
    return results_found, files_searched

def main():
    folder = choose_folder()
    search = input(f"{Fore.BLUE}Mot ou chaîne à rechercher : {Style.RESET_ALL}").strip()
    print(f"{Fore.RED}Recherche en cours dans la base de données...{Style.RESET_ALL}")
    results_found, files_searched = search_in_files(folder, search)
    if not results_found:
        print(f"{Fore.RED}Aucun résultat trouvé pour \"{Fore.BLUE}{search}{Fore.RED}\".{Style.RESET_ALL}")
    print(f"{Fore.RED}Total de fichiers scannés : {Fore.BLUE}{files_searched}{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()