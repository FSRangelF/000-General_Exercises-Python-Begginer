dist = float(input('Informe a distância da viagem em km? '))
# if dist <= 200:
#    preco = dist * 0.5
# else:
#    preco = dist * 0.45
preco = dist * 0.5 if dist <= 200 else dist * 0.45
print('O preço da passagem será de R${:.2f}'.format(preco))
