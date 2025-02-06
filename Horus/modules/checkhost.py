import requests
import time
import os
import socket
from termcolor import colored
from urllib.parse import urlparse

def check_host(host):
    os.system("tput civis")
    url = f'https://check-host.net/check-http?host={host}&max_nodes=16'
    headers = {'Accept': 'application/json'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        check_host_data = response.json()
        print(colored(f"\n [+] Host check has started for: {colored(host, 'red')}", 'green'))
        print(colored(" [+] Please wait...", 'green'))
        print(colored(f" [+] Expected connections: {colored('16', 'red')}\n", 'green'))
        return check_host_data.get('request_id')
    else:
        print(colored(f"[!] Error fetching Check Host results: {response.text} (Status code: {response.status_code})", 'red'))
        return None

def check_results(request_id):
    url = f'https://check-host.net/check-result/{request_id}'
    headers = {'Accept': 'application/json'}
    
    retries = 10
    interval = 10

    for attempt in range(retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            check_results_data = response.json()
            if check_results_data:
                connections = 0
                print(colored("\n [+] Results:\n", 'green'))

                for node, details in check_results_data.items():
                    try:
                        if not details or not isinstance(details, list) or not details[0]:
                            continue

                        first_detail = details[0]

                        if len(first_detail) > 4 and first_detail[3] and first_detail[4]:
                            status_code = first_detail[3]
                            ip = first_detail[4]
                            print(f"    {colored('[-]', 'green')} {colored(node, 'green')}: {colored(status_code, 'red')} | {colored(ip, 'red')}")
                            connections += 1
                    except Exception:
                        continue

                print(colored(f"\n [+] Successful connections: {colored(connections, 'red')}\n", 'green'))
                
                if connections < 8:
                    print(colored(" [+] Host Down\n", 'green'))
                else:
                    print(colored(" [+] Host Up\n", 'green'))
                
                os.system("tput cnorm")
                return
            else:
                print(colored(f" [!] Attempt {attempt + 1}: Results still not ready. Retrying...", 'yellow'))

        else:
            print(colored(f" [!] Error fetching Check Results (Attempt {attempt + 1}): {response.text} (Status code: {response.status_code})", 'red'))

        time.sleep(interval)

    print(colored("\n [!] Results could not be fetched after multiple attempts.", 'red'))
    os.system("tput cnorm")

def is_valid_host(host):
    try:
        result = urlparse(host)
        if not all([result.scheme, result.netloc]):
            return False

        domain = result.netloc

        socket.gethostbyname(domain)
        return True 

    except (socket.gaierror, ValueError):
        return False 

def main(host):
    if is_valid_host(host):
        request_id = check_host(host)
        if request_id:
            time.sleep(5)
            check_results(request_id)
        else:
            print(colored("\n [!] Failed to start host check.\n", 'red'))
    else:
        print(colored("\n [!] Invalid Host or Non-existent Domain\n", 'red'))

if __name__ == "__main__":
    host_input = input(colored(" [+] Enter the host to check: ", 'green')) 
    main(host_input)
