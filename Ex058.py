from random import randint
CPU = randint(0, 10)
cont = 1
print('Estou pensando em um número, você consegue adivinhar qual?')
n = int(input('Digite um numero de 0 a 10: '))
while n not in [0,1,2,3,4,5,6,7,8,9,10]:
  n = int(input('Numero inválido. Tente novamente. Digite um numero de 0 a 10: '))
while n != CPU:
    if n > CPU:
        n = int(input('Que pena, você errou. Tente novamente com um numero MENOR. Digite um numero de 0 a 10: '))
    else:
        n = int(input('Que pena, você errou. Tente novamente com um numero MAIOR. Digite um numero de 0 a 10: '))
    while n not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
      n = int(input('Numero inválido. Tente novamente. Digite um numero de 0 a 10: '))
    cont += 1
print('Parabéns você acertou na {}ª tentativa'.format(cont))
