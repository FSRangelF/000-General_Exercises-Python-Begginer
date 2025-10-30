ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'nNsS':
        resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    op = int(input('Mostrar nota de qual aluno? [999 interromper] '))
    if op == 999:
        print('Fim da Execução')
        break
    elif op < len(ficha):
        print(f'As notas de {ficha[op][0]} são {ficha[op][1]}')
print('<<< VOLTE SEMPRE >>>')
