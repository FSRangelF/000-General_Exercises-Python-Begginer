num1 = int(input('Digite o Primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 == num2:
    print('Não existe valor maior, os dois valores são iguais')
elif num1 > num2:
    print('o primeiro valor {} é maior que o segundo valor {}'.format(num1,num2))
elif num2 > num1:
    print('o segundo valor {} é maior que o primeiro valor {}'.format(num2, num1))