jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
gols = list()
for i in range(1, n+1):
    gols.append(int(input(f'Quantos gols marcados na partida {i}: ')))
jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)
print('-='*40)
print(jogador)
print('-='*40)
for i, v in jogador.items():
    print(f'o campo {i} tem o valor {v}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')