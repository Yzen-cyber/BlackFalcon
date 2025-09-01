import os
import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print(f"{Fore.RED}Le module 'phonenumbers' n'est pas installé. Installe-le avec : pip install phonenumbers{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")
    exit(1)

def number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        operator_phone = carrier.name_for_number(parsed_number, "fr")
        type_number_phone = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        country_phone = phonenumbers.region_code_for_number(parsed_number)
        region_phone = geocoder.description_for_number(parsed_number, "fr")
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_phone = timezones[0] if timezones else None
    except:
        operator_phone = "None"
        type_number_phone = "None"
        country_phone = "None"
        region_phone = "None"
        timezone_phone = "None"
    return operator_phone, type_number_phone, country_phone, region_phone, timezone_phone

def ip_info(ip):
    try:
        api = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()
    except:
        api = {}
    isp_ip = api.get("isp", "None")
    org_ip = api.get("org", "None")
    as_ip = api.get("as", "None")
    return isp_ip, org_ip, as_ip

def main():
    print(f"{Fore.RED}=== Dox Create Black Falcon ==={Style.RESET_ALL}")

    by =      input(f"{Fore.BLUE}Doxed By      : {Style.RESET_ALL}")
    reason =  input(f"{Fore.BLUE}Reason        : {Style.RESET_ALL}")
    pseudo1 = input(f"{Fore.BLUE}First Pseudo  : {Style.RESET_ALL}")
    pseudo2 = input(f"{Fore.BLUE}Second Pseudo : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Discord Information:{Style.RESET_ALL}")
    token_input = input(f"{Fore.BLUE}Token ? (y/n) : {Style.RESET_ALL}")
    if token_input.lower() in ["y", "yes"]:
        token = input(f"{Fore.BLUE}Token: {Style.RESET_ALL}")
        try:
            user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
            username_discord = user.get('username', 'None') + '#' + user.get('discriminator', 'None')
            display_name_discord = user.get('global_name', 'None')
            user_id_discord = user.get('id', 'None')
            avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar', '')}.png"
            email_discord = user.get('email', 'None')
            phone_discord = user.get('phone', 'None')
        except:
            username_discord = display_name_discord = user_id_discord = avatar_url_discord = email_discord = phone_discord = "None"
    else:
        token = "None"
        username_discord =     input(f"{Fore.BLUE}Username      : {Style.RESET_ALL}")
        display_name_discord = input(f"{Fore.BLUE}Display Name  : {Style.RESET_ALL}")
        user_id_discord =      input(f"{Fore.BLUE}Id            : {Style.RESET_ALL}")
        avatar_url_discord =   input(f"{Fore.BLUE}Avatar        : {Style.RESET_ALL}")
        email_discord =        input(f"{Fore.BLUE}Email         : {Style.RESET_ALL}")
        phone_discord =        input(f"{Fore.BLUE}Phone         : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Ip Information:{Style.RESET_ALL}")
    ip_public = input(f"{Fore.BLUE}Ip Publique   : {Style.RESET_ALL}")
    ip_local =  input(f"{Fore.BLUE}Ip Local      : {Style.RESET_ALL}")
    ipv6 =      input(f"{Fore.BLUE}Ipv6          : {Style.RESET_ALL}")
    vpn_pc =    input(f"{Fore.BLUE}VPN           : {Style.RESET_ALL}")
    isp_ip, org_ip, as_ip = ip_info(ip_public)

    print(f"\n{Fore.RED}Pc Information:{Style.RESET_ALL}")
    name_pc =         input(f"{Fore.BLUE}Name          : {Style.RESET_ALL}")
    username_pcc =    input(f"{Fore.BLUE}Username      : {Style.RESET_ALL}")
    displayname_pc =  input(f"{Fore.BLUE}Display Name  : {Style.RESET_ALL}")
    platform_pc =     input(f"{Fore.BLUE}Plateform     : {Style.RESET_ALL}")
    exploitation_pc = input(f"{Fore.BLUE}Exploitation  : {Style.RESET_ALL}")
    windowskey_pc =   input(f"{Fore.BLUE}Windows Key   : {Style.RESET_ALL}")
    mac_pc =          input(f"{Fore.BLUE}MAC Adress    : {Style.RESET_ALL}")
    hwid_pc =         input(f"{Fore.BLUE}HWID Adress   : {Style.RESET_ALL}")
    cpu_pc =          input(f"{Fore.BLUE}CPU           : {Style.RESET_ALL}")
    gpu_pc =          input(f"{Fore.BLUE}GPU           : {Style.RESET_ALL}")
    ram_pc =          input(f"{Fore.BLUE}RAM           : {Style.RESET_ALL}")
    disk_pc =         input(f"{Fore.BLUE}Disk          : {Style.RESET_ALL}")
    mainscreen_pc =   input(f"{Fore.BLUE}Screen Main   : {Style.RESET_ALL}")
    secscreen_pc =    input(f"{Fore.BLUE}Screen Sec    : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Number Information:{Style.RESET_ALL}")
    phone_number = input(f"{Fore.BLUE}Phone Number  : {Style.RESET_ALL}")
    brand_phone = input(f"{Fore.BLUE}Brand         : {Style.RESET_ALL}")
    operator_phone, type_number_phone, country_phone, region_phone, timezone_phone = number_info(phone_number)

    print(f"\n{Fore.RED}Personal Information:{Style.RESET_ALL}")
    gender =     input(f"{Fore.BLUE}Gender        : {Style.RESET_ALL}")
    last_name =  input(f"{Fore.BLUE}Last Name     : {Style.RESET_ALL}")
    first_name = input(f"{Fore.BLUE}First Name    : {Style.RESET_ALL}")
    age =        input(f"{Fore.BLUE}Age           : {Style.RESET_ALL}")
    mother =     input(f"{Fore.BLUE}Mother        : {Style.RESET_ALL}")
    father =     input(f"{Fore.BLUE}Father        : {Style.RESET_ALL}")
    brother =    input(f"{Fore.BLUE}Brother       : {Style.RESET_ALL}")
    sister =     input(f"{Fore.BLUE}Sister        : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Loc Information:{Style.RESET_ALL}")
    continent =   input(f"{Fore.BLUE}Continent     : {Style.RESET_ALL}")
    country =     input(f"{Fore.BLUE}Country       : {Style.RESET_ALL}")
    region =      input(f"{Fore.BLUE}Region        : {Style.RESET_ALL}")
    postal_code = input(f"{Fore.BLUE}Postal Code   : {Style.RESET_ALL}")
    city =        input(f"{Fore.BLUE}City          : {Style.RESET_ALL}")
    adress =      input(f"{Fore.BLUE}Adress        : {Style.RESET_ALL}")
    timezone =    input(f"{Fore.BLUE}Timezone      : {Style.RESET_ALL}")
    longitude =   input(f"{Fore.BLUE}Longitude     : {Style.RESET_ALL}")
    latitude =    input(f"{Fore.BLUE}Latitude      : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Social Information:{Style.RESET_ALL}")
    password = input(f"{Fore.BLUE}Password      : {Style.RESET_ALL}")
    email =    input(f"{Fore.BLUE}Email         : {Style.RESET_ALL}")

    print(f"\n{Fore.RED}Other:{Style.RESET_ALL}")
    other =    input(f"{Fore.BLUE}Other         : {Style.RESET_ALL}")
    database = input(f"{Fore.BLUE}DataBase      : {Style.RESET_ALL}")
    logs =     input(f"{Fore.BLUE}Logs          : {Style.RESET_ALL}")

    name_file = input(f"\n{Fore.BLUE}Choose the file name -> {Style.RESET_ALL}")
    if not name_file.strip():
        name_file = f'No Name {random.randint(1, 999)}'

    output_dir = os.path.join(os.getcwd(), "1-Output", "DoxCreate")
    os.makedirs(output_dir, exist_ok=True)
    dox_path = os.path.join(output_dir, f"D0x - {name_file}.txt")

    with open(dox_path, 'w', encoding='utf-8') as file:
        file.write(f'''
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
            Doxed By : {by}
            Reason   : {reason}
            Pseudo   : "{pseudo1}", "{pseudo2}"

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

DISCORD:
=====================================================================================
[+] Username     : {username_discord}
[+] Display Name : {display_name_discord}
[+] ID           : {user_id_discord}
[+] Avatar       : {avatar_url_discord}
[+] Token        : {token}
[+] E-Mail       : {email_discord}
[+] Phone        : {phone_discord}

INFORMATION:
=====================================================================================
+────────────Pc────────────+
[+] IP Publique  : {ip_public}
[+] Ip Local     : {ip_local}
[+] Ipv6         : {ipv6}
[+] Isp          : {isp_ip}
[+] Org          : {org_ip}
[+] As           : {as_ip}
[+] VPN Y/N      : {vpn_pc}
[+] Name         : {name_pc}
[+] Username     : {username_pcc}
[+] Display Name : {displayname_pc}
[+] Plateform    : {platform_pc}
[+] Exploitation : {exploitation_pc}
[+] Windows Key  : {windowskey_pc}
[+] MAC          : {mac_pc}
[+] HWID         : {hwid_pc}
[+] CPU          : {cpu_pc}
[+] GPU          : {gpu_pc}
[+] RAM          : {ram_pc}
[+] Disk         : {disk_pc}
[+] Screen Main      : {mainscreen_pc}
[+] Screen Secondary : {secscreen_pc}

+───────────Phone──────────+
[+] Phone Number : {phone_number}
[+] Brand        : {brand_phone}
[+] Operator     : {operator_phone}
[+] Type Number  : {type_number_phone}
[+] Country      : {country_phone}
[+] Region       : {region_phone}
[+] Timezone     : {timezone_phone}

+───────────Personal───────+
[+] Gender      : {gender}
[+] Last Name   : {last_name}
[+] First Name  : {first_name}
[+] Age         :  {age}
[+] Mother      : {mother}
[+] Father      : {father}
[+] Brother     : {brother}
[+] Sister      : {sister}

+────────────Loc───────────+
[+] Continent   : {continent}
[+] Country     : {country}
[+] Region      : {region}
[+] Postal Code : {postal_code}
[+] City        : {city}
[+] Address     : {adress}
[+] Timezone    : {timezone}
[+] Longitude   : {longitude}
[+] Latitude    : {latitude}

SOCIAL:
=====================================================================================
[+] Email    : {email}
[+] Password : {password}

OTHER:
=====================================================================================
{other}

DATABASE:
=====================================================================================
{database}

LOGS:
=====================================================================================
{logs}
''')

    print(f"{Fore.RED}Le DOX \"{name_file}\" a été enregistré dans : {Fore.BLUE}{dox_path}{Style.RESET_ALL}")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()