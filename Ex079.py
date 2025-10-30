lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado, não vou adicionar')
    else:
        lista.append(n)
        print('Valor adicionado com sucesso')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')