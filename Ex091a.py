from random import randint
from time import sleep
jogador = dict()
jogadas = list()
maior = 0
cont = 1
print('Valores Sorteados:')
for i in range(0, 4):
    jogador['Def'] = 'jogador_'+str(i+1)
    jogador['Score'] = randint(1, 6)
    jogadas.append(jogador.copy())
for i in range(0, len(jogadas)):
    print(f'O {jogadas[i]["Def"]} tirou {jogadas[i]["Score"]}')
    sleep(0.5)
n = len(jogadas)
for i in range(0, n):
    for i in range(0, n):
        if i == 0 or jogadas[i]['Score'] > maior:
            maior = jogadas[i]['Score']
    c = 1
    j = 0
    while c <= n:
        if jogadas[j]['Score'] == maior:
            print(f'{cont}º Lugar: {jogadas[j]["Def"]} com {jogadas[j]["Score"]}')
            sleep(0.5)
            cont += 1
            del jogadas[j]
            n = len(jogadas)
            break
        c += 1
        j += 1
