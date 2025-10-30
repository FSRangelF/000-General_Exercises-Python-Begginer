preco = float(input('Digite o preço do produto: R$'))
print('Selecione a forma de pagamento:')
print('[1] A vista dinheiro/check')
print('[2] A vista no cartão')
print('[3] em até 2x no cartão')
print('[4] 3x ou mais no cartão')
seletor = int(input('-> '))
if seletor == 1:
    preco = preco*0.9
    print('O preço final do produto será de R${:.2f}'.format(preco))
elif seletor == 2:
    preco = preco*0.95
    print('O preço final do produto será de R${:.2f}'.format(preco))
elif seletor == 3:
    pparc = preco/2
    print('O preço final do produto será de R${:.2f} em 2 parcelas de {:.2f}'.format(preco, pparc))
elif seletor == 4:
    preco = preco*1.2
    parcelas = int(input('Qual o numer de parcelas?'))
    pparc = preco / parcelas
    print('O preço final do produto será de R${:.2f} em {} parcelas de {:.2f}'.format(preco, parcelas, pparc))
else:
    print('Opção invalida')