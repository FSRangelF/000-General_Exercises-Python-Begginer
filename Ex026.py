frase = str(input('Digite uma frase qualquer: ')).strip()
print('A frase digitada possui {} letras "A"s'.format(frase.upper().count('A')))
print('A primeira letra "A" encontra-se na posição {}'.format(frase.upper().find('A')+1))
print('A última letra "encontra-se na posição {}'.format(frase.upper().rfind('A')+1))