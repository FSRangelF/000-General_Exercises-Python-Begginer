pares = list()
impares = list()
lista = [pares, impares]
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}o. valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
print('-='*40)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')

