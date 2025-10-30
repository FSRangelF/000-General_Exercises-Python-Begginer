sal = float(input('Digite o Valor do salário do funcionário: R$'))
aug = float(input('Digite o valor do percentual de aumento desejado: '))
print('O Salário original de R${:.2f} passará a ser de R${:.2f} após a efetivação do aumento de {}%.'.format(sal, sal*(1+(aug/100)), aug))
