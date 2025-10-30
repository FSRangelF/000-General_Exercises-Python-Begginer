m18 = qtdhomens = qtdM20 = 0
while True:
    print('--'*15, '\n     CADASTRE UMA PESSOA\n', '--' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        m18 += 1
    if sexo == 'M':
        qtdhomens +=1
    if sexo == 'F' and idade < 20:
        qtdM20 +=1
    print('--' * 15)
    op = ' '
    while op not in 'SN':
        op = str(input('Quer Continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'======= FIM DO PROGRAMA ======= \nTotal de pessoas com mais de 18 anos: {m18} \n'
      f'Ao todo temos {qtdhomens} homens cadastrados \n'
      f'E temos {qtdM20} mulheres com menos de 20 anos')
