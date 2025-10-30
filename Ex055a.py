maior = 0
menor = 10000000000
for c in range(1, 6):
  peso = float(input('Digite o peso da pessoa No {} em Kilos: '.format (c)))
  if peso > maior:
    maior = peso
  if peso < menor:
    menor = peso
print('O maior peso informado foi de {}'.format(maior))
print('O menor peso informado foi de {}'.format(menor))