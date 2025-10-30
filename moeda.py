def metade(n=0, f=False):
    if f:
        return f'R${n/2:.2f}'
    else:
        return n/2


def dobro(n, f=False):
    if f:
        return f'R${n*2:.2f}'
    else:
        return n*2


def aumentando(n=0, p=0, f=False):
    if p != 0:
        if f:
            return f'R${n * (1 + (p / 100)):.2f}'
        else:
            return n * (1 + (p / 100))
    else:
        if f:
            return f'R${n:.2f}'
        else:
            return n


def diminuindo(n=0, p=0, f=False):
    if p != 0:
        if f:
            return f'R${n * (1 - (p / 100)):.2f}'
        else:
            return n * (1 - (p / 100))
    else:
        if f:
            return f'R${n:.2f}'
        else:
            return n


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n, pa, pr):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço Analisado:":<30}{moeda(n):>10}')
    print(f'{"Dobro do Preço:":<30}{dobro(n, True):>10}')
    print(f'{"Metade do Preço:":<30}{metade(n, True):>10}')
    print(f'{pa}{"% de aumento:":<28}{aumentando(n, pa, True):>10}')
    print(f'{pr}{"% de redução:":<28}{aumentando(n, pr, True):>10}')
    print('-' * 40)