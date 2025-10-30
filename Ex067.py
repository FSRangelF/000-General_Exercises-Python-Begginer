while True:
    print('-' * 12)
    n = int(input('Digite um numero inteiro [ou um negativo para parar]: '))
    print('-' * 12)
    if n < 0:
        print('fim da execução')
        break
    for c in range(1, 11):
        print('{:>2} x {:>2} = {:>2}'.format(n, c, n * c))
