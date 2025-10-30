nome = str(input('Digite seu nome: '))
if nome == 'Francisco':
    print('que nome lindo vc tem!')
else:
    print('que nome normal vc tem...')
print('bom dia, {}'.format(nome))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('Parabéns, você foi aprovado!' if m >= 7 else 'Estude mais, você bombou!')
