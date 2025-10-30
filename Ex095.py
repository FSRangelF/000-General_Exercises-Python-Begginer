jogador = dict()
lista = list()
gols = list()
cod = 0
while True:
    jogador.clear()
    print('-' * 60)
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['cod'] = cod
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for i in range(1, n+1):
        gols.append(int(input(f'Quantos gols marcados na partida {i}: ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())
    gols.clear()
    while True:
        op = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
        if op in 'NS':
            break
        print('ERRO! Opção inválida. Digite apenas S ou N')
    if op == 'N':
        break
    cod += 1
print('-=' * 30)
print(f'{"cod.":<5}{"nome":<15}{"gols":<35}{"total":<5}')
print('-' * 60)
for p in lista:
    print(f'{p["cod"]:<5}{p["nome"]:<15}{str(p["gols"]):<35}{p["total"]:^5}')
while True:
    print('-' * 60)
    m = int(input('Mostrar o levantamento de qual jogador? [999 para parar]: '))
    if m == 999:
        print('-' * 60)
        print(f'{"<<< FIM DA EXECUÇÃO >>>":-^60}')
        break
    elif m < len(lista):
        print(f'O jogador {lista[m]["nome"]} jogou {len(lista[m]["gols"])} partidas')
        for i, v in enumerate(lista[m]['gols']):
            print(f'   => Na partida {i+1} fez {v} gols.')
        print(f'Foi um total de {lista[m]["total"]} gols')
    else:
        print(f'Erro! Não existe jogador com código {m} tente novamente...')
print(f'{"<<< FIM DA EXECUÇÃO >>>":=^60}')
