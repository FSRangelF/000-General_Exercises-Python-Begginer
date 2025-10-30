c = 0
termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
while c <= 10:
  pa = termo + c*razao
  print(pa, '-> ', end='')
  c += 1
print('acabou')
