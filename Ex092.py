from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem)'))
if pessoa['ctps'] != 0:
     pessoa['contratação'] = int(input('Ano de Contratação'))
     pessoa['salário'] = float(input('Salário'))
     pessoa['aposentadoria'] = pessoa['idade'] + 35 - (date.today().year - pessoa['contratação'])
print('=-'*40)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
