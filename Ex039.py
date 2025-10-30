from datetime import date

anocorrente = date.today().year
ano = int(input('informe o ano de nascimento: '))
anoalist = ano+18

if anocorrente < anoalist:
    prazo = anoalist - anocorrente
    print('Vc ainda ira se alistar. Aindam faltam {} para o alistamento'.format(prazo))
elif anocorrente == anoalist:
    print('Vc deve se alistar neste ano')
elif anocorrente > anoalist:
    prazo = anocorrente - anoalist
    print('Vc deveria ter se alistado a {} anos'.format(prazo))
