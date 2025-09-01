import re
import requests
import dns.resolver
from colorama import Fore, Style, init
import time

init(autoreset=True)

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
    except:
        domain_all = None

    try:
        name = email.split('@')[0]
    except:
        name = None

    try:
        domain = re.search(r"@([^@.]+)\.", email).group(1)
    except:
        domain = None
    try:
        tld = f".{email.split('.')[-1]}"
    except:
        tld = None

    try:
        mx_records = dns.resolver.resolve(domain_all, 'MX')
        mx_servers = [str(record.exchange) for record in mx_records]
        info["mx_servers"] = mx_servers
    except Exception:
        info["mx_servers"] = None

    try:
        spf_records = dns.resolver.resolve(domain_all, 'SPF')
        info["spf_records"] = [str(record) for record in spf_records]
    except Exception:
        info["spf_records"] = None

    try:
        dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
        info["dmarc_records"] = [str(record) for record in dmarc_records]
    except Exception:
        info["dmarc_records"] = None

    # Détection Google Workspace / Microsoft 365
    info["google_workspace"] = False
    info["microsoft_365"] = False
    mx_servers = info.get("mx_servers", [])
    if mx_servers:
        for server in mx_servers:
            if "google.com" in server:
                info["google_workspace"] = True
            elif "outlook.com" in server or "protection.microsoft.com" in server:
                info["microsoft_365"] = True

    return info, domain_all, domain, tld, name

def main():
    print(f"{Fore.RED}=== Email Lookup Black Falcon ==={Style.RESET_ALL}")
    email = input(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Email -> {Style.RESET_ALL}").strip()
    print(f"{Fore.BLUE}[{time.strftime('%H:%M:%S')}] {Fore.RED}Recherche des informations...{Style.RESET_ALL}")
    info, domain_all, domain, tld, name = get_email_info(email)

    try:
        mx_servers = info["mx_servers"]
        mx_servers = ' / '.join(mx_servers) if mx_servers else None
    except:
        mx_servers = None

    try:
        spf_records = info["spf_records"]
        spf_records = ' / '.join(spf_records) if spf_records else None
    except:
        spf_records = None

    try:
        dmarc_records = info["dmarc_records"]
        dmarc_records = ' / '.join(dmarc_records) if dmarc_records else None
    except:
        dmarc_records = None

    google_workspace = info.get("google_workspace", False)
    microsoft_365 = info.get("microsoft_365", False)

    print(f"""
{Fore.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
{Fore.BLUE}Email      : {Fore.RED}{email}{Style.RESET_ALL}
{Fore.BLUE}Name       : {Fore.RED}{name}{Style.RESET_ALL}
{Fore.BLUE}Domain     : {Fore.RED}{domain}{Style.RESET_ALL}
{Fore.BLUE}Tld        : {Fore.RED}{tld}{Style.RESET_ALL}
{Fore.BLUE}Domain All : {Fore.RED}{domain_all}{Style.RESET_ALL}
{Fore.BLUE}Servers    : {Fore.RED}{mx_servers}{Style.RESET_ALL}
{Fore.BLUE}Spf        : {Fore.RED}{spf_records}{Style.RESET_ALL}
{Fore.BLUE}Dmarc      : {Fore.RED}{dmarc_records}{Style.RESET_ALL}
{Fore.BLUE}Google WS  : {Fore.RED}{google_workspace}{Style.RESET_ALL}
{Fore.BLUE}Microsoft 365 : {Fore.RED}{microsoft_365}{Style.RESET_ALL}
{Fore.RED}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}
""")
    input(f"{Fore.RED}Appuyez sur Entrée pour quitter.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()