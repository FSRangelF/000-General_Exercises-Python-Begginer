from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rank = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"<<< RANKING DOS JOGADORES >>>":=^40}')
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(0.5)
