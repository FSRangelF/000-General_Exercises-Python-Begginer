from random import randint
from time import sleep


def sorteia(sort):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n = randint(1, 10)
        sort.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')


def somapar(lista):
    s = 0
    for num in lista:
        if num % 2 == 0:
            s += num
    print(f'Somando os valores pares de {lista} temos {s}')


# Main
numero = list()
sorteia(numero)
somapar(numero)
