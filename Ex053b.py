frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso = junto[::-1]
print('Voce digitou a frase {} e o Inverso é {}'.format(junto, inverso))
if inverso == junto:
  print('Temos um PALINDROMO')
else:
  print('A frase digitada não é um PALINDROMO')