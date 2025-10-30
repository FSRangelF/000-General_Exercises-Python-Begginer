nome = str(input('Digite o nome completo: ')).title().strip().split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome nome: {}'.format(nome[int(len(nome)-1)]))
