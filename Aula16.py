# Tuplas

lanche = ('Hamburguer', 'Suco', 'pizza', 'pudim')
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3:])

# Tuplas são imutaveis e não podem ser alteradas em tempo de execuçã
# uma vez feita a atribuição os valores não pode ser alterados
# por isso as linhas de comando abaixo retrnarão erro:
# lanche[1] = 'refrigerante'
# print(lanche[1])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('fim do laço')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('fim do laço')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}')
print('fim do laço')

a = (2, 5, 4)
b = (5, 8, 1, 2)

print(sorted(a)) # retona uma lista dos elementos da tupla ordenados, mantendo a tupla sem alteração
print(a)
print(sorted(b))
print(b)

c = a + b # a concatenação de tuplas não é reflexiva (a + b) != (b + a)
d = b + a

print(c)
print(d)

print(len(c))
print(c.count(5)) #retorna a quantidade de ocorrencias de um determinado elemento
print(d.index(2)) #retorna a posição da primeira ocorrencia de um determinado elemento

pessoa = ('Gustavo', 39, 'M', 99) # diferentemente de vetores, as tuplas aceitam multiplos tipos de dados
print(pessoa)

del(pessoa) # permite apagar a tupla toda em tempo de execução