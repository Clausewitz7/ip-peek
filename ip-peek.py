import requests
import os
from colorama import Fore, init

init(autoreset=True)

my_ascii = fr"""{Fore.CYAN}
  ___ ___   ___ ___ ___ _  __
 |_ _| _ \ | _ \ __| __| |/ /
  | ||  _/ |  _/ _|| _|| ' < 
 |___|_|   |_| |___|___|_|\_\ .------.[Clausewitz7].------.
"""
print(my_ascii)

ip = input(f"{Fore.GREEN}Enter Target IP: ")
url = f'https://ipwho.is/{ip}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    os.system('cls' if os.name == 'nt' else 'clear')

    print(my_ascii)

    print(f"{Fore.GREEN}Target IP    : {Fore.MAGENTA}{data.get('ip')}")
    print(f"{Fore.GREEN}Country      : {Fore.MAGENTA}{data.get('country')} ({data.get('country_code')})") #{data.get('flag', {}).get('emoji', '')}
    print(f"{Fore.GREEN}City / Region: {Fore.MAGENTA}{data.get('city')}, {data.get('region')}")
    print(f"{Fore.GREEN}ISP          : {Fore.MAGENTA}{data.get('connection', {}).get('isp', 'N/A')}")
    print(f"{Fore.GREEN}Coordinates  : {Fore.MAGENTA}https://www.google.com/maps?q={data.get('latitude')},{data.get('longitude')}")

else:
    print(f"{Fore.GREEN}Error: {Fore.MAGENTA}https://http.cat/{response.status_code}")