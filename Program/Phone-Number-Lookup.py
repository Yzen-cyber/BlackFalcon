from colorama import Fore, Style, init
init(autoreset=True)

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print(f"{Fore.RED}Le module 'phonenumbers' n'est pas installé. Installe-le avec : pip install phonenumbers{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
    exit(1)

def main():
    print(f"{Fore.RED}=== Phone Number Lookup Black Falcon ==={Style.RESET_ALL}")
    phone_number = input(f"{Fore.BLUE}Numéro de téléphone (ex: +33612345678) : {Style.RESET_ALL}").strip()
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        status = "Valide" if phonenumbers.is_valid_number(parsed_number) else "Invalide"
        try:
            country_code = f"+{parsed_number.country_code}"
        except:
            country_code = "Inconnu"
        try:
            operator = carrier.name_for_number(parsed_number, "fr")
        except:
            operator = "Inconnu"
        try:
            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        except:
            type_number = "Inconnu"
        try:
            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else "Inconnue"
        except:
            timezone_info = "Inconnue"
        try:
            country = phonenumbers.region_code_for_number(parsed_number)
        except:
            country = "Inconnu"
        try:
            region = geocoder.description_for_number(parsed_number, "fr")
        except:
            region = "Inconnue"
        try:
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        except:
            formatted_number = "Inconnu"

        print(f"""
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
{Fore.BLUE}Numéro        : {Fore.RED}{phone_number}{Style.RESET_ALL}
{Fore.BLUE}Formaté       : {Fore.RED}{formatted_number}{Style.RESET_ALL}
{Fore.BLUE}Statut        : {Fore.RED}{status}{Style.RESET_ALL}
{Fore.BLUE}Indicatif     : {Fore.RED}{country_code}{Style.RESET_ALL}
{Fore.BLUE}Pays          : {Fore.RED}{country}{Style.RESET_ALL}
{Fore.BLUE}Région        : {Fore.RED}{region}{Style.RESET_ALL}
{Fore.BLUE}Fuseau horaire: {Fore.RED}{timezone_info}{Style.RESET_ALL}
{Fore.BLUE}Opérateur     : {Fore.RED}{operator}{Style.RESET_ALL}
{Fore.BLUE}Type          : {Fore.RED}{type_number}{Style.RESET_ALL}
{Fore.RED}────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
""")
    except Exception as e:
        print(f"{Fore.RED}Format invalide ou erreur : {e}{Style.RESET_ALL}")

    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()