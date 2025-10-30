from datetime import date
ano = date.today().year
s = 0
for c in range(1,8):
  n = int(input('Digite o ano de nascimento a pessoa No {}: '.format (c)))
  if ano - n >= 21:
    s = s+1
print('Dentre as pessoas informadas {} são maiores de idade e {} são menores de idade'.format(s, 7-s))