numero = int(input('Digite o Número '))
s = 0
if numero == 1:
  print('o numero {} não é primo'.format(numero))
else:
  for c in range(1, numero+1):
    if numero % c == 0:
      s = s + 1
  if s <= 2:
    print('o numero {} é primo'.format(numero))
  else:
    print('o numero {} não é primo'.format(numero))