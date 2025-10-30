def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f}m é de {a:.1f}m2.')


# Main
print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
