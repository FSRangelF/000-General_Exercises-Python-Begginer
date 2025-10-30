numero = int(input('Digite o numero inteiro a ser convertido: '))
print('Escolha:')
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
seletor = int(input('-> '))
if seletor == 1:
    conv = bin(numero)
    print('O valor de {} em binário é {}'.format(numero,conv[2:]))
elif seletor == 2:
    conv = oct(numero)
    print('O valor de {} em octal é {}'.format(numero,conv[2:]))
elif seletor == 3:
    conv = hex(numero)
    print('O valor de {} em hexadecimal é {}'.format(numero,conv[2:]))
else:
    print('Seleção inválida. selecione novamente:')

