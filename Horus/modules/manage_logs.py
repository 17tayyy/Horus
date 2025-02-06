import os,  readline
from termcolor import colored

def list_files(log_directory):
    files = [file for file in os.listdir(log_directory) if file.endswith(".log")]
    if files:
        print(colored("\n [+] Available files:\n", 'blue'))
        for file in files:
            print(colored(file, 'yellow'))
    else:
        print(colored("\n [+] No .log files found in the directory.", 'yellow'))

def view_file(log_directory, file_name):
    file_path = os.path.join(log_directory, file_name)
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print(colored(f"\n [+] Content of {file_name}:", 'blue'))
            print(file.read())
    else:
        print(colored(f"\n [+] The file {file_name} does not exist.", 'yellow'))

def delete_file(log_directory, file_name):
    file_path = os.path.join(log_directory, file_name)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        print(colored(f"\n [+] The file {file_name} has been deleted.", 'green'))
    else:
        print(colored(f"\n [+] The file {file_name} does not exist.", 'yellow'))

def read_logs(log_directory):
    logs = []

    for file in os.listdir(log_directory):
        if file.endswith(".log"):
            with open(os.path.join(log_directory, file), 'r') as f:
                for line in f:
                    data = line.strip().split(" | ")

                    if len(data) == 4:
                        timestamp, user, ip, command = data
                        logs.append({
                            'timestamp': timestamp,
                            'user': user,
                            'ip': ip,
                            'command': command
                        })

    return logs

def save_logs_to_file(logs, output_file):
    with open(output_file, 'w') as f:
        for log in logs:
            f.write(f"{log['timestamp']} | {log['user']} | {log['ip']} | {log['command']}\n")
    print(colored(f" [+] Logs saved to {output_file}", 'green'))

def menu():
    log_directory = "logs"
    
    try: 
        while True:
            print(colored("\n [+] Menu \n", 'blue'))
            print(colored("\t1. List .log files", 'yellow'))
            print(colored("\t2. View content of a file", 'yellow'))
            print(colored("\t3. Delete a file", 'yellow'))
            print(colored("\t4. Read and process logs", 'yellow'))
            print(colored("\t5. Exit", 'yellow'))
            
            option = input(colored("\n [+] Select an option (1-5): ", 'blue'))

            if option == '1':
                list_files(log_directory)
            elif option == '2':
                file_name = input(colored("\n [+] Enter the name of the file to view (e.g., file.log): ", 'blue'))
                view_file(log_directory, file_name)
            elif option == '3':
                file_name = input(colored("\n [+] Enter the name of the file to delete (e.g., file.log): ", 'blue'))
                delete_file(log_directory, file_name)
            elif option == '4':
                logs = read_logs(log_directory)
                output_file = input(colored("\n [+] Enter the name of the output file to save the processed logs: ", 'blue'))
                save_logs_to_file(logs, output_file)
            elif option == '5':
                print(colored("\n [!] Exiting...", 'red'))
                break
            else:
                print(colored("\n [!] Invalid option. Please select a valid option.", 'yellow'))

    except KeyboardInterrupt:
        print(colored("\n\n [+] Extiting...\n", 'red'))

def main():
    menu()

if __name__ == '__main__':
    main()
