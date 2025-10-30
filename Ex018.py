import math

num = float(input('Digite o valor do angulo em graus: '))
sin = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O seno do angulo {:.2f} é {:.2f}'.format(num, sin))
print('O cosseno do angulo {:.2f} é {:.2f}'.format(num, cos))
print('A tangente do angulo {:.2f} é {:.2f}'.format(num, tan))
