def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def soma2(*valores):
    s = 0
    for num in valores:
       s += num
    print(f'Somando os valores {valores} temos {s}')


def contador(*num):
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# programa principal
soma(4, 5)
soma(a=8, b=9)
soma(b=2, a=4)

contador(2, 1, 7)
contador(8, 9)
contador(4, 4, 7, 6, 2)

lista = [7, 2, 5, 0, 4]
dobra(lista)
print(lista)

soma2(3, 8)
soma2(3, 8, 7, 9)