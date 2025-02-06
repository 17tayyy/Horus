import os
import random
import string
from datetime import datetime
import readline
from termcolor import colored

file_path = "logins/logins.txt"

def list_users():
    if not os.path.exists(file_path):
        print(colored(" [!] logins.txt not found.", 'red'))
        return
    print(colored("\n [+] Current Users:", 'cyan'))
    with open(file_path, "r") as file:
        for line in file:
            print(colored(line.strip(), 'yellow'))

def generate_secure_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def add_user():
    os.system("clear")
    print(colored("\n [+] Add a New User", 'green'))
    username = input(colored(" [+] Enter username: ", 'blue')).strip()
    choose_password = input(colored(" [+] Generate Password? (y/n): ", 'blue')).strip()
    if choose_password == "y":
        password = generate_secure_password()
    else:
        password = input(colored(" [+] Enter Password: ", 'blue')).strip()

    expiration_date = input(colored(" [+] Enter expiration date (DD/MM/YYYY): ", 'blue')).strip()
    concurrents = input(colored(" [+] Enter concurrents: ", 'blue')).strip()
    max_time = input(colored(" [+] Enter max time: ", 'blue')).strip()
    vip_access = input(colored(" [+] Enter vip access: ", 'blue')).strip()

    try:
        datetime.strptime(expiration_date, "%d/%m/%Y")
    except ValueError:
        print(colored(" [!] Invalid date format.", 'red'))
        return

    with open(file_path, "a") as file:
        file.seek(0, os.SEEK_END)
        if file.tell() > 0:
            file.write("\n")  
        file.write(f"{username}:{password}:{expiration_date}:{concurrents}:{max_time}:{vip_access}")
    
    print(colored(f" [+] User added successfully.", 'green'))
    print(colored(f" [+] Credentials: {username}:{password}", 'yellow'))

def remove_user():
    print(colored("\n [+] Remove a User", 'green'))
    username = input(colored(" [+] Enter username to remove: ", 'blue')).strip()
    if not os.path.exists(file_path):
        print(colored(" [!] logins.txt not found.", 'red'))
        return

    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        found = False
        for line in lines:
            if line.startswith(f"{username}:"):
                found = True
            else:
                file.write(line)

    if found:
        print(colored(" [+] User removed successfully.", 'green'))
    else:
        print(colored(" [!] User not found.", 'red'))

def clear_screen():
    os.system("clear")

def menu():
    try:
        while True:
            print(colored("\n [+] User Management Menu\n", 'blue'))
            print(colored("\t1. List Users", 'yellow'))
            print(colored("\t2. Add User", 'yellow'))
            print(colored("\t3. Remove User", 'yellow'))
            print(colored("\t4. Exit", 'yellow'))
            print(colored("\t5. Clear", 'yellow'))
            choice = input(colored("\n [+] Enter choice: ", 'blue')).strip()

            if choice == "1":
                list_users()
            elif choice == "2":
                add_user()
            elif choice == "3":
                remove_user()
            elif choice == "4":
                print(colored("\n [!] Exiting...", 'red'))
                break
            elif choice == "5":
                clear_screen()
            else:
                print(colored(" [!] Invalid choice.", 'red'))

    except KeyboardInterrupt:
        print(colored("\n\n [+] Extiting...\n", 'red'))


if __name__ == "__main__":
    menu()
