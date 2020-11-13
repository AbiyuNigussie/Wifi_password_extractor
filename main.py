import subprocess
# Creator : Abiyu Nigussie  E-mail : abiyunigussie7@gmail.com
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode().split('\n')

wifis = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]
file = open('info.txt', 'a')
for wifi in wifis:
    passwords = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode().split('\n')
    passwords = [password.split(':')[1][1:-1] for password in passwords if "Key Content" in password]
    try:
        file.writelines(f'Name: {wifi}  Password: {passwords[0]} \n')
    except IndexError:
        file.writelines(f'Name {wifi}  Password: Cannot read! \n')
    if (wifi == wifis[len(wifis) - 1]):
        file.writelines('\n')
        break