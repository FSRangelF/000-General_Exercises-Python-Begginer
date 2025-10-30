termo = int(input('Digite o primeiro termo: '))
razao = int(input('digite a razão: '))
ttermos = 0
mais = 10
c = 0
while mais != 0:
    ttermos = ttermos + mais
    while c < ttermos:
        pa = termo + c * razao
        print(pa, ' -> ', end='')
        c += 1
    mais = int(input('\ndigite a quantidade de termos adicionais a serem exibidos: '))
print('progressão finalizada com {} termos exibidos'.format(c))