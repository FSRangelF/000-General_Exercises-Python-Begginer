# import time
from datetime import date

ano = int(input('Digite o ao a ser analizado ou "0" para o ano atual: '))
if ano == 0:
    #    ano = int(time.strftime('%Y', time.localtime()))
    ano = date.today().year
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
