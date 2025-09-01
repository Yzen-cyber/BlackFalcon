import os
import time
import base64
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import piexif
    import exifread
    from PIL import Image
    import tkinter as tk
    from tkinter import filedialog
except ImportError as e:
    print(f"{Fore.RED}Module manquant : {e}. Installe-le avec pip install piexif exifread pillow{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
    exit(1)

def choose_image_file():
    print(f"{Fore.RED}=== Get Image Exif Black Falcon ==={Style.RESET_ALL}")
    try:
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        file = filedialog.askopenfilename(
            title="Choisissez une image",
            filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff"), ("Tous les fichiers", "*.*")]
        )
        if not file:
            raise Exception("Aucun fichier sélectionné.")
        print(f"{Fore.BLUE}Fichier sélectionné : {Fore.RED}{file}{Style.RESET_ALL}")
        return file
    except Exception:
        return input(f"{Fore.BLUE}Chemin de l'image : {Style.RESET_ALL}").strip()

def clean_value(value):
    if isinstance(value, bytes):
        try:
            return value.decode('utf-8', errors='replace')
        except:
            return base64.b64encode(value).decode('utf-8')
    elif isinstance(value, (list, tuple)):
        return ', '.join(str(v) for v in value)
    elif isinstance(value, dict):
        return {k: clean_value(v) for k, v in value.items()}
    else:
        return value

def get_all_exif(image_path):
    exif_data = {}

    # piexif
    try:
        exif_dict = piexif.load(image_path)
        for ifd in exif_dict:
            if isinstance(exif_dict[ifd], dict):
                for tag in exif_dict[ifd]:
                    tag_name = piexif.TAGS[ifd].get(tag, {"name": tag})["name"]
                    raw_value = exif_dict[ifd][tag]
                    exif_data[f"{tag_name}"] = clean_value(raw_value)
    except Exception:
        pass

    # exifread
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, details=True)
            for tag in tags:
                label = tag.split()[-1]
                if label not in exif_data:
                    exif_data[label] = clean_value(str(tags[tag]))
    except Exception:
        pass

    # PIL
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            depth = len(img.getbands())
            exif_data['Dimension'] = f"{width}x{height}"
            exif_data['Width'] = width
            exif_data['Height'] = height
            exif_data['Depth'] = depth
    except Exception as e:
        exif_data["Image Error"] = str(e)

    # Fichier
    try:
        file_stats = os.stat(image_path)
        exif_data['Name'] = os.path.basename(image_path)
        exif_data['Type'] = os.path.splitext(image_path)[1]
        exif_data['Creation date'] = time.ctime(file_stats.st_ctime)
        exif_data['Date modified'] = time.ctime(file_stats.st_mtime)
        exif_data['Attributes'] = oct(file_stats.st_mode)
        exif_data['Availability'] = 'Available' if os.access(image_path, os.R_OK) else 'Not available'
        exif_data['Offline Status'] = 'Online' if os.path.exists(image_path) else 'Offline'
    except Exception as e:
        exif_data["File Stats Error"] = str(e)

    if exif_data:
        max_key_length = max(len(k) for k in exif_data.keys())
        print(f"\n{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        for key, value in sorted(exif_data.items(), key=lambda x: x[0].lower()):
            print(f" {Fore.BLUE}{key.ljust(max_key_length)} : {Fore.RED}{str(value)}{Style.RESET_ALL}")
            time.sleep(0.01)
        print(f"{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n")
    else:
        print(f"{Fore.RED}Aucune information trouvée.{Style.RESET_ALL}")

def main():
    image_path = choose_image_file()
    print(f"{Fore.BLUE}Recherche des informations EXIF...{Style.RESET_ALL}")
    get_all_exif(image_path)
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()