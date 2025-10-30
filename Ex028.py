from random import randint
from time import sleep

num = randint(0, 5)
print('-=-'*18)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*18)
num2 = int(input('Em que numero eu pensei: '))
print('processando....')
sleep(2)
if num == num2:
    print('Parabens, vc acertou... o numero que eu pensei foi mesmo o {}'.format(num))
else:
    print('Que pena, você disse {} e eu estava pensando em {}'.format(num2, num))