from random import randint
from time import sleep
print('-='*24)
print(f'{"JOGA NA MEGA SENA":^48}')
print('-='*24)
n = int(input('Quantos jogos vc quer fazer? '))
m = int(input('Quantas dezenas? [6 a 20]'))
while m > 20 or m < 6:
    m = int(input('Quantas dezenas? [6 a 20]'))
print('-='*4, f'SORTEANDO {n} JOGOS DE {m} DEZENAS', '-='*4)
jogos = list()
jogo = list()
for i in range(0, n):
    for j in range(0, m):
        r = randint(1, 60)
        while r in jogo:
            r = randint(1, 60)
        jogo.append(r)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for i, v in enumerate(jogos):
    print(f'JOGO {i+1}: {v}')
    sleep(0.5)
print(f'{" < BOA SORTE! > ":-^48}')
