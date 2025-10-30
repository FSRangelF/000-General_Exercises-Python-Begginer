c = 0
loop = 0
termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
while c < 10:
  pa = termo + c*razao
  print(pa, ' -> ', end='')
  c += 1
while loop == 0:
  add = int(input('\ndigite a quantidade de termos adicionais a serem exibidos: '))
  if add == 0:
    loop = 1
  add = add + c
  while c < add:
    pa = termo + c*razao
    print(pa, ' -> ', end='')
    c += 1
print('progressão finalizada com {} termos exibidos'.format(c))