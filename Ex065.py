soma = cont = 0
numero = []
op = 'S'
while op in 'Ss':
    n = int(input('Digite um número: '))
    op = str(input('Deseja Continuar [S/N]: ')).upper().strip()[0]
    while op not in 'nNsS':
        print('Opção inválida, digite uma opção válida.')
        op = str(input('Deseja Continuar [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += n
    numero.append(n)
    if op == 'N':
        print('Foram digitados {} valores'.format(cont))
        print('O Maior Valor foi {}'.format(max(numero)))
        print('O Menor Valor foi {}'.format(min(numero)))
        print('A Média foi {}'.format(soma/cont))
