op = 4
while op != 5:
  if op == 4:
    print("\n" * 12)
    print('-='*20)
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('-='*20)
  print('''Selecione a opção desejada
  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos números
  [5] Sair do Programa''')
  op = int(input('->'))
  if op == 1:
    ans = n1 + n2
    print('A soma de {} e {} é igual a {}'.format(n1, n2, ans))
  elif op == 2:
    ans = n1 * n2
    print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, ans))
  elif op == 3:
      print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1,n2)))
  elif op == 4:
    print ("\n" * 12)
  elif op == 5:
    print('-='*20)
    print('Fim da Execução')
  else:
    print('Opção Inválida, tente novamente!')
