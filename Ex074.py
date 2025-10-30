from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'os numeros gerados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior valor gerado foi {max(tupla)}') # print(f'O maior valor gerado foi {sorted(tupla)[-1]}')
print(f'O menor valor gerado foi {min(tupla)}') # print(f'O menor valor gerado foi {sorted(tupla)[0]}')
