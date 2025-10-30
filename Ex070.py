print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)
menorpreco = valortotal = maior1000 = 0
maisbarato = ''
cont = 0
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    valortotal += preco
    cont += 1
    if preco >= 1000:
        maior1000 += 1
    if cont == 1 or preco < menorpreco:
        menorpreco = preco
        maisbarato = nome
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print('{:=^30}'.format('FIM DO PROGRAM'))
print(f'O valor total da compra foi de R${valortotal:.2f} para os {cont} produtos')
print(f'Temos {maior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} custando {menorpreco}')
