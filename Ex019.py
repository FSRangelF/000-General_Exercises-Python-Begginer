# import math
import random

n1 = input('Digite o primeiro nome ')
n2 = input('Digite o segundo nome ')
n3 = input('Digite o terceiro nome ')
n4 = input('Digite o quarto nome ')
# num = math.ceil(4*random.random())
# print(num)
# if num == 1 : print('O aluno escolhido é: {}'.format(n1))
# if num == 2 : print('O aluno escolhido é: {}'.format(n2))
# if num == 3 : print('O aluno escolhido é: {}'.format(n3))
# if num == 4 : print('O aluno escolhido é: {}'.format(n4))
lista = [n1, n2, n3, n4]
escolha = random.choice(lista)
print('O aluno escolhido é {}'.format(escolha))
