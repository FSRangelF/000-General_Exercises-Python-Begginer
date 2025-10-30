num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
for c in num:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('-=' * 40)
print(f'A lista completa é {num}')
print(f'A lista e pares é {pares}')
print(f'A lista de impares é {impares}')
