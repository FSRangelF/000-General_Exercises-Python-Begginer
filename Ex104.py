def leiaInt(val=''):
    x = str(input(val))
    while not x.isnumeric():
        print('\033[1:31mERRO! Digite um numer inteiro válido\033[0:m')
        x = str(input(val))
    return x


# MAIN
n = leiaInt('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')