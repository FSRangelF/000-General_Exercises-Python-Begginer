c = 1
while c < 10:
  print(c)
  c +=1
print('Fim')

n = 1
while n != 0:
  n = int(input('Digite um Valor: '))
print('Fim')

r = 'S'
while r == 'S':
  n = int(input('Digite um Valor: '))
  r = str(input('Quer Continuar? [S/N] ')).upper()
print('Fim')

n = 1
par = impar = 0
while n != 0:
  n = int(input('Digite um Valor: '))
  if n % 2 ==0:
    par += 1
  else:
    impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))