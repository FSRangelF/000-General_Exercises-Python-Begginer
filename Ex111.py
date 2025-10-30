from utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dorbo de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentando(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuindo(p, 13, True)}')
moeda.resumo(p, 80, 35)
