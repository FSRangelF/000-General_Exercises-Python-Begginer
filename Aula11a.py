import colorize

print('\033[0;30;41mteste\033[m ')
print('\033[4;33;44mteste\033[m ')
print('\033[1;35;43mteste\033[m ')
print('\033[30;42mteste\033[m ')
print('\033[1;30mteste\033[m ')
print('\033[7;30mteste\033[m ')
nome = 'João'
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pb':'\033[7;30m'}
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pb'], nome, cores['limpa']))
