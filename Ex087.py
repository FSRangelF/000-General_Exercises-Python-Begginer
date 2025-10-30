matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaP = soma3C = maior2L = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-='*20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
        if matriz[i][j] % 2 == 0:
            somaP += matriz[i][j]
        if j == 2:
            soma3C += matriz[i][j]
        if i == 1 and (j == 0 or matriz[i][j] > maior2L):
            maior2L = matriz[i][j]
    print('')
print('-='*20)
print(f'A soma dos valores pares é {somaP}')
print(f'A soma dos valores da terceira coluna é {soma3C}')
print(f'O maior valor da segunda linha é {maior2L}')
