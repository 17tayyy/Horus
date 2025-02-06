import requests
from termcolor import colored
import Horus
import os

def get_ip_info(ip, token=None):

    url = f"https://ipinfo.io/{ip}/json"
    headers = {}
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {f" [!] Error"}

def main(ip):
    os.system("tput civis")
    token = None
    info = get_ip_info(ip, token)
    if "error" in info:
        print(info["error"])
    else:
        Horus.sprint2(colored(f"\n [+] Information about {ip} :\n", 'green'))
        for key, value in info.items():
            Horus.sprint2(colored(f" [+] {key.capitalize()}: {value}", 'green'))
        print("\n")
    os.system("tput cnorm")

if __name__ == "__main__":
    main()
