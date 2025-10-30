def leiaInt(val=''):
    while True:
        try:
            x = int(input(val))
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um numero inteiro válido\033[0:m')
            continue
        except KeyboardInterrupt:
            print('\033[1:31m\nO usuário preferiu não digitar este número\033[0:m')
            return 0
        else:
            return x



def leiaFloat(val=''):
    while True:
        try:
            x = str(input(val)).strip().replace(',', '.')
            x = float(x)
        except (ValueError, TypeError):
            print('\033[1:31mERRO! Digite um numero real válido\033[0:m')
        except KeyboardInterrupt:
            print('\033[1:31m\nO usuário preferiu não digitar este número\033[0:m')
            return 0
        else:
            return x



# MAIN
n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r}')
