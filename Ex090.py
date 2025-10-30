aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Em Recupeção'
else:
    aluno['Situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
