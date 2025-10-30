pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #valores que demandam aspas dentro de uma f-string precisam ser declaradas com aspas duplas
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
pessoas['idade'] = 22
pessoas['peso'] = 95
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

estado = dict()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy()) # copy é necessário para evitar a criação de relação entre a lista e o dicionario. O metodo de fatiamento [:] nao funciona em dicionario
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()