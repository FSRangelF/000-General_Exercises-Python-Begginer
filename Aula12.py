nome = str(input('Qual o seu nome '))
if nome == 'Gustavo':
    print('que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome =='João':
    print('seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('belo nome feminino')
else:
    print('Seu nome é bem normal')
print('tenha um bom dia {}'.format(nome))