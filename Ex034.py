sal = float(input('Digite o valor do Salário do funcionário: '))
if sal > 1250:
    aug = 0.10
else:
    aug = 0.15
print('O Funcionário receberá um aumento de {}% e seu novo salário será de {:.2f}'.format((100 * aug), sal * (1 + aug)))
