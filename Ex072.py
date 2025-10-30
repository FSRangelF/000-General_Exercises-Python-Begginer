ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
op = 'S'
while op == 'S':
    while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {ext[n]}')
    op = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('Fim da Execução')