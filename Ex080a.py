lista = list()
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista...')
    elif n < min(lista):
        lista.insert(0, n)
        print('Adicionado na posição 0 da lista...')
    elif n in lista:
        lista.insert(lista.index(n)+1, n)
        print(f'Adicionado na posição {lista.index(n)+1} da lista...')
    else:
        for cont in range(0, len(lista)):
            if n > lista[cont-1] and n < lista[cont]:
                lista.insert(cont, n)
                print(f'Adicionado na posição {cont} da lista...')
print('-='*40)
print(f'os valores digitados em ordem formar: {lista}')
