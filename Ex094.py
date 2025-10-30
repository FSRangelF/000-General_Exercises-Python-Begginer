pessoa = dict()
cadastro = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F ')
    pessoa['idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    while True:
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if op in "SN":
            break
        print('ERRO! por favor, digite apenas S ou N ')
    if op == 'N':
        break
print('-='*40)
print(f' - O grupo tem {len(cadastro)} pessoas.')
somaidade = 0
for i in range(0, len(cadastro)):
    somaidade += cadastro[i]['idade']
med = somaidade / len(cadastro)
print(f' - A média de idade é de {med:5.2f} anos')
print(' - As mulheres cadastradas foram:', end=' ')
for i in cadastro:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end=' ')
print()
print(' - Lista das pessoas que estão acima da média de idade:\n')
for p in cadastro:
    if p['idade'] > med:
        for k, v in p.items():
            print(f'    {k} = {v}; ', end='')
    print()
print('Fim da Execução')
