lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if op == 'N':
        break
print('-='*40)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
print(f'O valor 5 faz parte da lista e encontra-se na posição {lista.index(5)}' if 5 in lista else 'O valor 5 não faz parte da lista')
