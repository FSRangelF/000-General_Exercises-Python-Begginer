from time import sleep

cont = 1
while cont <= 10:
    print(cont, "-> ", end='')
    cont += 1
print('FIM')

n = cont = soma = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('Foram digitados %d números e a soma deles é igual a %d' % (cont, soma)) # PYTHON 2
print('Foram digitados {} números e a soma deles é igual a {}'.format(cont, soma)) # PYTHON 3
print(f'Foram digitados {cont} números e a soma deles é igual a {soma}') # PYTHON 3.6

cont = 1
while True:
    print(cont, "-> ", end='')
    cont += 1
    sleep(0.5)
print('FIM')
