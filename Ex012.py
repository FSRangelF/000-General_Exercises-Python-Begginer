n = float(input('Digite o Valor do produto: R$'))
d = float(input('Digite o percentual de desconto desejado: '))
print('O produto sairá de R${:.2f} por R${:.2f} com {}% de desconto!'.format(n, n*(1-(d/100)), d))
