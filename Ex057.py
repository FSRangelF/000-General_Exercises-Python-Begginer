sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
  sexo = str(input('Opção invalida, Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
