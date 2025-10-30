n = int(input('Digite o numero de termos da Sequência: '))
a = b = c = 0
cont = 1
while cont <= n:
    if b == 0:
        print(' {} ->'.format(c), end='')
        b = c = 1
    else:
        print(' {} ->'.format(c), end='')
        c = a + b
        a = b
        b = c
    cont += 1
print(' Fim da Execução')