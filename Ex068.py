from random import randint
cont = 0
print('-='*15)
print('  VAMOS JOGAR PAR OU IMPAR')
while True:
    print('-='*15)
    cpu = randint(1, 10)
    n = int(input('Digite um valor de 1 a 10: '))
    while n not in [0,1,2,3,4,5,6,7,8,9,10]:
        n = int(input('Numero invalido. Digite um valor de 1 a 10: '))
    op = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    while op not in 'PI':
        op = str(input('Opção inválida. Par ou Impar? [P/I] ')).strip().upper()[0]
    soma = n + cpu
    print('--'*15)
    print(f'Voce jogou {n} e o CPU {cpu}')
    if soma % 2 == 0:
        r = 'P'
        print(f'O Total de {soma} deu PAR')
    else:
        r = 'I'
        print(f'O Total de {soma} deu IMPAR')
    print('--' * 15)
    if op != r:
        print('Você PERDEU!')
        break
    print('Você VENCEU!')
    print('Vamos jogar novamente....')
print('-=' * 15)
print(f'GAME OVER! Você venceu {cont} vezes')