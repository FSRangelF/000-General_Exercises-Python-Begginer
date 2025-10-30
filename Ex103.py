def ficha(nome='', gols=''):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


# MAIN
print('-'*30)
n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: ')).strip()
ficha(n, g)
