print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n = int(input('QUal Valor você quer sacar? R$ '))
cedulas = [50, 20, 10, 1]
cont = 0
totced = 0
while True:

    if n >= cedulas[cont]:
        n -= cedulas[cont]
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${cedulas[cont]}')
        totced = 0
        cont += 1
        if n == 0:
            break
print('='*30)
print('Volte sempre ao banco CEV! Tenha um bom dia!')