def fatorial(n, show=False):
    """
    => Calcula o Fatorial de um número
    :param n: O numero a ser calculado
    :param show: (opcional) Mostrar o nao a conta
    :return: O valor do Fatorial de um numero n
    """
    f = 1
    s = str('')
    for c in range(n, 0, -1):
        f *= c
        if c == 1:
            s = s + str(f'{c} = ')
        else:
            s = s + str(f'{c} x ')
    s = s + str(f'{f}')
    if show:
        return s
    else:
        return f


help(fatorial)
print('-'*30)
print(fatorial(5))
print(fatorial(5, show=True))
