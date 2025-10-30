from datetime import date

anocorrente = date.today().year

ano = int(input('informe o ano de nascimento: '))

idade = anocorrente - ano

if idade <= 9:
    print('{} Anos --- >  Categoria MIRIM'.format(idade))
elif idade <= 14:
    print('{} Anos --- >  Categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('{} Anos --- >  Categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('{} Anos --- >  Categoria SÊNIOR'.format(idade))
else:
    print('{} Anos --- >  Categoria MASTER'.format(idade))