peso = int(input('digite o peso em Kg: '))
altura = float(input('digite a altura em metros: '))

imc = peso / (altura * altura)
print('seu IMC é igual a {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc >= 25 and imc <= 30:
    print('SOBREPESO')
elif imc >=30 and imc <=40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MORBIDA')