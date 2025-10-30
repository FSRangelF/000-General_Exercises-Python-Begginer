Mmaisvelho = str('')
Maioridadesmasc = 0
SIdades = 0
cont = 0
for c in range(1, 5):
  print('------------ {}ª Pessoa -----------'.format(c))
  nome = str(input('Nome: '))
  sexo = str(input('Sexo [M/F] '))
  idade = int(input('Informe a idade da pessoa No {} '.format(c)))
  if sexo.strip().upper() == 'M' and idade >= Maioridadesmasc:
    Maioridadesmasc = idade
    Mmaisvelho = nome
  if sexo.strip().upper() == 'F' and idade < 20:
    cont = cont + 1
  SIdades = SIdades + idade
media = float(SIdades/4)
print('A media das idades informadas é de {:.2f} anos'.format(media))
print('O nome do Homem mais velho é {} que tem {} anos'.format(Mmaisvelho,Maioridadesmasc))
print('Temos {} mulher(es) com menos de 20 anos'.format(cont))