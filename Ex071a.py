print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n = int(input('QUal Valor você quer sacar? R$ '))
c50 = c20 = c10 = c1 = 0
while n >= 50:
    n -= 50
    c50 += 1
while n >= 20:
    n -= 20
    c20 += 1
while n>= 10:
    n -= 10
    c10 += 1
while n > 0:
    n -= 1
    c1 += 1
print(f'Total de {c50} cedulas de R$50')
print(f'Total de {c20} cedulas de R$20')
print(f'Total de {c10} cedulas de R$10')
print(f'Total de {c1} cedulas de R$1')
print('=='*30)
print('Volte sempre ao banco CEV! Tenha um bom dia!')