lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*30)
print(f'voce digitou os valores {lista}')
print(f'O menor valor digitado foi {min(lista)} nas posiçôes ', end='')
for i, v in enumerate(lista):
    print(f'{i}..' if v == min(lista) else '', end='')
print(f' \nO maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    print(f'{i}..' if v == max(lista) else '', end='')
