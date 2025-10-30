pilha = list()
exp = list(str(input('Digite uma expressão: ')))
marca = 0
for i in exp:
    if i == '(':
        pilha.append(i)
    elif i == ')' and '(' in pilha:
        pilha.remove('(')
    elif i == ')' and '(' not in pilha:
        marca = 1
if len(pilha) == 0 and marca == 0:
    print('A expressão digitada é válida')
else:
    print('Sua expressão esta errada')
