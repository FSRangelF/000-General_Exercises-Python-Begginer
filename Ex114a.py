import requests

url = 'http://www.pudim.com.br/'

try:
    r = requests.get(url)
    if r.status_code == 200:
        print(f'\033[0;32mO Site Pudim esta acessível.\033[m')
    else:
        print(f'\033[0;31mO Site Pudim não esta acessível no momento. \nStatus Code: {r.status_code} \033[m')
except Exception as error:
    print(f'\033[0;31mO Site Pudim não esta acessível no momento. \n# ERR {error.__class__} \033[m')
