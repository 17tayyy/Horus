# Horus 

Horus is a CNC full setup to manage a botnet and launch DDoS attacks. This repository contains the **CNC (Command & Control)** panel, where root can manage clients, view logs..., and the users can launch DDoS attacks.

## Images

### Client Panel
![Captura de pantalla 2025-01-30 201608](https://github.com/user-attachments/assets/6a696c42-1d0a-4531-b06a-13d622b48751)

![Captura de pantalla 2025-01-30 201637](https://github.com/user-attachments/assets/7dbaae73-30e5-4b12-b3ea-4a54587a85e9)

![Captura de pantalla 2025-01-30 204822](https://github.com/user-attachments/assets/c3ec0600-64d7-4118-86ac-d0316d40e9fc)

![Captura de pantalla 2025-01-30 201918](https://github.com/user-attachments/assets/0787aa8f-8d1a-43b7-92bc-88d0c80c4ef6)

![Captura de pantalla 2025-01-30 202341](https://github.com/user-attachments/assets/8068f7c6-0945-4b0f-b19f-11d39f118712)

![hostdown](https://github.com/user-attachments/assets/afc8fd59-7e52-46fc-95f6-f01e13bf3c11)

![image](https://github.com/user-attachments/assets/070ebe60-7fe0-4d9f-a814-b4690b23123d)

![tirao](https://github.com/user-attachments/assets/099d1fb6-e4c5-4e2e-81f1-065f23847b78)

### Admin Panel
![Captura de pantalla 2025-01-30 202418](https://github.com/user-attachments/assets/54935891-d3db-499f-88a6-a5dcf15adebd)

![buena2](https://github.com/user-attachments/assets/0432e648-f25d-4d26-8b18-bb4fac6115ab)

![logs](https://github.com/user-attachments/assets/6b839cc9-bf45-4ac2-bb9a-2832bec60922)

![buena](https://github.com/user-attachments/assets/7489d2cd-900d-45ac-a733-b2134a60d1c3)

![Captura de pantalla 2025-01-30 202735](https://github.com/user-attachments/assets/4d4e622e-3c70-41ac-98b1-4688e3f6a0e3)

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

2. All the tests to make this repository have done in controled environments 

3. This CNC needs an API to make de DDOS attacks, this is only the setup to sell the access or for personal use, and the methods are not free so they are not in this repo, to buy t.me/HorusBotnet

## Warning

**Horus** is a powerful tool and should be used ethically and legally. Unauthorized use on hots you do not own is illegal and could lead to legal consequences. Use this tool only on hosts you own or in controlled testing environments.
