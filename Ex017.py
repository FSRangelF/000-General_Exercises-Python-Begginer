import math

op = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
# hip = math.sqrt(math.pow(op, 2) + math.pow(adj, 2))
hip = math.hypot(op, adj)
print('A hipotenusa é: {:.2f}'.format(hip))
