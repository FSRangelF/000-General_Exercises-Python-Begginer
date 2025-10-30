dados = list()
pessoas = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
for i in range(0, len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    elif pessoas[i][1] > maior:
        maior = pessoas[i][1]
    elif pessoas[i][1] < menor:
        menor = pessoas[i][1]
print('-='*40)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')