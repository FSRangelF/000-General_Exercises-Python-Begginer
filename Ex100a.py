from random import randint
from time import sleep


def sorteia(a, b):
    sort = list()
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(a, b)
        sort.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('Pronto!')
    return sort


def somapar(lista):
    s = 0
    for num in lista:
        if num % 2 == 0:
            s += num
    print(f'Somando os valores pares de {lista} temos {s}')


# Main
somapar(sorteia(1, 10))
