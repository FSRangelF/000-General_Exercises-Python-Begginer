n = int(input('Digite um numero: '))
fat = 1
print('{}! = '.format(n), end='')
while n > 0:
  print('{}'.format(n), end='')
  print(' x ' if n > 1 else ' = ', end='')
  fat *= n
  n -= 1
print('{}'.format(fat), end='')
