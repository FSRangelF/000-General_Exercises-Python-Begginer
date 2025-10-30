from time import sleep
c = ['\033[m',          # 0 - sem cor
     '\033[41m',        # 1 - vermelho
     '\033[42m',        # 2 - verde
     '\033[43m',        # 3 - amarelo
     '\033[44m',        # 4 - azul
     '\033[45m',        # 5 - roxo
     '\033[30;47m']        # 6 - cinza


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    t = len(msg) + 6
    print(c[cor], end='')
    print('~' * t)
    print(f'{msg:^{t}}')
    print('~' * t)
    print(c[0], end='')
    sleep(1)


# MAIN
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)
