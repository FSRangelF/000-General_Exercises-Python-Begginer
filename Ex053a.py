s = str(input('Digite uma frase qualquer: '))
st = s.upper().split()
s2 = str('')
i=0
for item in st:
  s2 = s2+st[i]
  i = i+1
j = len(s2)
sent_reverso = []
for c in range(0, j):
  sent_reverso.append(s2[c])
sent_reverso.reverse()
s = 0
for c in range(0, j):
  if sent_reverso[c] != s2[c]:
    s = s + 1
if s == 0:
  print('A frase digitada é um Palíndromo')
else:
  print('A frase digitada não é um Palíndromo')