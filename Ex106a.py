def mostra(val):
    t = len(val) + 6
    print('~' * t)
    print(f'{val:^{t}}')
    print('~' * t)


while True:
    print('\033[42m', end='')
    mostra('SISTEMA DE AJUDA PyHELP')
    print('\033[m', end='')
    op = str(input('Função ou Bibliteca > ')).lower().strip()
    if op == 'fim':
        print('\033[41m', end='')
        mostra('ATÉ LOGO!')
        break
    print('\033[44m', end='')
    mostra(f'Acessando o manual do comando "{op}"')
    print('\033[47m', end='')
    help(op)
