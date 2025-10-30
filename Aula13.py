for c in range(0, 6):
    print('oi')
    print(c)
print('fim')
for c in range(6, 0, -1):
    print('oi')
    print(c)
print('fim')
for c in range(0, 7, 2):
    print('oi')
    print(c)
print('fim')

i = int(input('Início'))
f = int(input('fim'))
p = int(input('passo'))

for c in range(i, f+1, p):
    print(c)
print('fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um Valor'))
    s += n
print(s)