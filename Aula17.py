num = [2, 5, 9, 1]
print(num)
num[2] = 3
num.append(7) # adiciona um elemento ao fim da lista
print(num)
num.insert(2, 0) # insere um elemento na lista no indice indicado
print(num)
num.sort() # reorganiza a lista de modo crescente
print(num)
num.sort(reverse=True) #reorganiza a lista de modo decrescente
print(num)
num.pop() # elimina o elemnto do indicie indicado ou o ultimo elemnteo qdo nenhum parametro é declarado
print(num)
num.insert(2, 2)
print(num)
num.remove(2) # remove o primeiro elemento encontrado
print(num)

if 4 in num: # laço para evitar erro ao tentar remover um elemento inexistente
    num.remove(4)
    print(num)

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('fim da lista')

a = [2, 3, 4, 7]
b = a # ao igualar listas se cria uma ligação entre elas
c = a[:] # para se criar uma COPIA da lista original de modo que ao alterar a copia a original não seja afetada é necessario declarar dessa forma
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
b[2] = 8 # ao alterar um elemento de uma lista as demais listas ligadas tbm são alteradas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
