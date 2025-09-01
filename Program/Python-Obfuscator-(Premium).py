import os
from colorama import Fore, Style, init
import base64

init(autoreset=True)

def obfuscate_code(code):
    # Simple obfuscation: base64 encode the code and wrap in a loader
    encoded = base64.b64encode(code.encode('utf-8')).decode('utf-8')
    loader = f"""import base64
exec(compile(base64.b64decode('{encoded}').decode('utf-8'), '<obfuscated>', 'exec'))
"""
    return loader

def main():
    print(f"{Fore.RED}=== Python Obfuscator Black Falcon ==={Style.RESET_ALL}")
    input_path = input(f"{Fore.BLUE}Chemin du fichier Python à obfusquer : {Style.RESET_ALL}").strip()
    if not os.path.isfile(input_path):
        print(f"{Fore.RED}Fichier introuvable.{Style.RESET_ALL}")
        return
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()
    obfuscated = obfuscate_code(code)
    output_path = input_path.replace(".py", "_obfuscated.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(obfuscated)
    print(f"{Fore.RED}Fichier obfusqué créé : {Fore.BLUE}{output_path}{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()