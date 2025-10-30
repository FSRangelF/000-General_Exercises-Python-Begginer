numero = int(input('Digite o numero inteiro a ser convertido: '))
print('Escolha:')
print('[1] para binário')
print('[2] para octal')
print('[3] para hexadecimal')
seletor = int(input('-> '))
if seletor == 1:
    num = numero
    conv = str('')
    if num <= 1:
        conv = str(num.__str__() + conv)
    while num > 1:
        resto = num % 2
        num = num // 2
        conv = str(resto.__str__() + conv)
        if num <= 1:
            conv = str(num.__str__() + conv)
    print('O valor de {} em binário é {}'.format(numero,conv))
elif seletor == 2:
    num = numero
    conv = str('')
    if num <= 7:
        conv = str(num.__str__() + conv)
    while num > 7:
        resto = num % 8
        num = num // 8
        conv = str(resto.__str__() + conv)
        if num <= 7:
            conv = str(num.__str__() + conv)
    print('O valor de {} em octal é {}'.format(numero,conv))
elif seletor == 3:
    num = numero
    conv = str('')
    if num <= 15:
        if num == 10:
            conv = str("A" + conv)
        elif num == 11:
            conv = str("B" + conv)
        elif num == 12:
            conv = str("C" + conv)
        elif num == 13:
            conv = str("D" + conv)
        elif num == 14:
            conv = str("E" + conv)
        elif num == 15:
            conv = str("F" + conv)
        else:
            conv = str(num.__str__() + conv)
    while num > 15:
        resto = num % 16
        if resto == 10:
            conv = str("A" + conv)
        elif resto == 11:
            conv = str("B" + conv)
        elif resto == 12:
            conv = str("C" + conv)
        elif resto == 13:
            conv = str("D" + conv)
        elif resto == 14:
            conv = str("E" + conv)
        elif resto == 15:
            conv = str("F" + conv)
        else:
            conv = str(resto.__str__() + conv)
        num = num // 16
        if num <= 15:
            if num == 10:
                conv = str("A" + conv)
            elif num == 11:
                conv = str("B" + conv)
            elif num == 12:
                conv = str("C" + conv)
            elif num == 13:
                conv = str("D" + conv)
            elif num == 14:
                conv = str("E" + conv)
            elif num == 15:
                conv = str("F" + conv)
            else:
                conv = str(num.__str__() + conv)
    print('O valor de {} em hexadecimal é {}'.format(numero,conv))
else:
    print('Seleção inválida. selecione novamente:')

