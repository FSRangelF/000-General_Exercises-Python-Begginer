aluno = list()
sala = list()
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    sala.append(aluno[:])
    aluno.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*22)
print(f'{"No.":<4}{"NOME":<30}{"MÉDIA":^6}')
print('--'*22)
for i, p in enumerate(sala):
    print(f'{i:<4}{p[0]:<30}{((p[1]+p[2])/2):^6.1f}')
op = 0
while op != 999:
    print('-=' * 22)
    op = int(input('Mostrar nota de qual aluno? [999 interromper] '))
    if op < len(sala):
        print(f'As notas de {sala[op][0]} são [{sala[op][1]:.1f}, {sala[op][2]:.1f}]')
    else:
        print(f'Aluno inválido')
print('Fim da Execução')
