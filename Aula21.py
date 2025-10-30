def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numeor: '))
print(f'O fatorial de {num} é {fatorial(num)}')

print(par(num))