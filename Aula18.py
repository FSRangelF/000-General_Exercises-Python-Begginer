teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:]) # [:] indica a copia de dados, do contrario as listas ficam ligadas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[1][0])
print(galera[1][1])
teste.clear()
for c in range(0, 3):
    teste.append(str(input('Nome: ')))
    teste.append(int(input('Idade: ')))
    galera.append(teste[:])
    teste.clear()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')