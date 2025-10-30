import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except Exception as error:
    print(f'\033[0;31mO Site Pudim não esta acessível no momento. \n# ERR {error.__class__} \033[m')
else:
    print(f'\033[0;32mO Site Pudim esta acessível.\033[m')
    print(site.read())
