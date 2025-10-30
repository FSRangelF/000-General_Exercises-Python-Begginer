print('\033[1;34m-=\033[m'*20)
print('\033[1;31m     Analizador de Triangulos V1.0\033[m')
print('\033[1;34m-=\033[m'*20)
a = float(input('Digite o valor do primeiro segmento de reta: '))
b = float(input('Digite o valor do segundo segmento de reta: '))
c = float(input('Digite o valor do terceiro segmento de reta: '))
if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < (a + c)) and (abs(a - b) < c < (a + b)):
    print('Os três segmentos de reta {:.0f}, {:.0f} e {:.0f} informados \033[1;31mFORMAM\033[m um trinagulo'.format(a, b, c))
else:
    print('Os três segmentos de reta {:.0f}, {:.0f} e {:.0f} informados \033[1;31mNÃO FORMAM\033[m um trinagulo'.format(a, b, c))
