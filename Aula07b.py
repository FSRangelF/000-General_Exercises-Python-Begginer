n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto vale {}, \n a divisão vale {:.3f}'.format(s,m,d), end=' >>> ')
print('Divisão inteira é igual a {} e a potencia é {}'.format(di, e))
