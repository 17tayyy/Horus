# Horus 

Horus is a CNC full setup to manage a botnet and launch DDoS attacks. This repository contains the **CNC (Command & Control)** panel, where root can manage clients, view logs..., and the users can launch DDoS attacks.

## Images

### Client Panel
![image](https://github.com/user-attachments/assets/b335ecd1-a079-47e9-863b-027cfdd9cebb)

![image](https://github.com/user-attachments/assets/97d7512f-ceb0-4c05-8896-77d9837986c2)

![image](https://github.com/user-attachments/assets/ef2b3370-cbe3-4abc-8cad-e96f498cb426)

![image](https://github.com/user-attachments/assets/a40a06c4-2a83-4586-94e9-ba95d6a4cd44)

![hostdown](https://github.com/user-attachments/assets/a00c349e-d737-45ed-bc3c-1f204ccfa5b0)

![image](https://github.com/user-attachments/assets/65799fa7-8bfd-4304-a320-fbb01c082208)

![image](https://github.com/user-attachments/assets/e983fbc7-02c1-41ed-982c-b38ddf0407c4)

### Admin Panel
![image](https://github.com/user-attachments/assets/b5c99c6b-ab66-4ee3-bc70-06cdf66bb9ef)

![buena2](https://github.com/user-attachments/assets/df803f0d-15a0-4345-a37f-c817a33bcbaf)

![logs](https://github.com/user-attachments/assets/14058baa-7f54-4208-a8da-ffae5405361e)

![buena](https://github.com/user-attachments/assets/574280ea-61a0-41f1-aa03-96992341d636)

![image](https://github.com/user-attachments/assets/fa1f8681-dbc9-4ebc-aaa8-e659230cb899)

## Features:

- **Authentication**: It has an advanced login system, with a captcha to make it more safe.
- **Admin panel**: The admin panel allows for user management, advenced loggin, command and attack log viewing.
- **DDoS Attacks**: Launch DDoS attacks using various methods (HTTP, TCP, UDP, Amplification, etc.) API Required.
- **Activity Logging**: Commands and activities are logged for record-keeping.
- **VIP Access & Permissions**: Users have roles with restrictions such as the maximum number of concurrent attacks or the maximum attack duration.

## Installation

To make this system functionally follow this instructions:

  1. First you have to buy a linux VPS.
  2. In the VPS you have to create a new user called 'user'.
  3. Change the sshd_config file for the one in this repository
  4. Then you only have clone and move this repository to /opt/
  5. After doing this you only have to buy an API from some DDOS hire company
  6. Finally you only have to configure your API in the send_attacks.py
  7. Now you have your own CNC!

## Usage

  After installation the usage system it's so easy.
  1. Connect by SSH with the user 'user' in 2222 port and a captcha will appear if you pass it then a loggin will appear
  2. Enter the credentials of your user, defaults for root are 'root:root123'
  3. If you connect with root it send you to the admin panel but with other users it redirects to de DDOS panel
  4. From the admin panel you have total control off the CNC (view logs, add users, remove...)

  To rent the CNC to clients

  1. You create a discord or a telegram and get users
  2. You will have to give all clients the password of the user 'user' to make they can connect via SSH
  3. When a client buy the access you have to create a user from the Horus admin panel
  4. Give him all credentials and confirm he can connect.
  5. Start making more clients and buying more expensive plans of API if you wan't more power and concurrents
  6. That's all

## Important Disclaimers

1. This project is all done by me without any help from nobody.

2. This CNC needs an API to make de DDOS attacks, this is only the setup to sell the access or for personal use, and the methods are not free so they are not in this repo, to buy t.me/HorusBotnet

## Warning

**Horus** is a powerful tool and should be used ethically and legally. Unauthorized use on hots you do not own is illegal and could lead to legal consequences. Use this tool only on hosts you own or in controlled testing environments.
