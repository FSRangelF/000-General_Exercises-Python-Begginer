valor = float(input('Digite o valor da Casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite o prazo de pagamento em anos: '))

parcela = valor / (12*anos)

if (parcela/salario) > 0.3:
    print('EMPRESTIMO NEGADO. O valor da parcela é de R${:.2f} e é maior que 30% do salário.'.format(parcela))
else:
    print('EMPRESTIMO CONCEDIDO. Valor da parcela mensal é de R${:.2f}'.format(parcela))