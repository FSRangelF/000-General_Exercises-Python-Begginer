termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
for c in range (0, 10):
  pa = termo + c*razao
  print(pa, '-> ', end='')
print('acabou')