num = str(input('Digite um numero entre 0 e 9999 ')).strip()
# print('Tratamento de Cadeia de Caracteres\nunidade: {}\n\ndezena:  {}\ncentena: {}\nmilhar:  {}'.format(num[3], num[2], num[1], num[0]))
# Este método fica incompleto sem a utilização de condicionais e portanto da erros
num2 = int(num)
mil = num2//1000
cent = (num2%1000)//100
dez = ((num2%1000)%100)//10
un = (((num2%1000)%100)%10)
print('Tratamento Matemático 1\n\nunidade: {}\ndezena:  {}\ncentena: {}\nmilhar:  {}'.format(un,dez, cent, mil))
un2 = num2//1 %10
dez2 = num2//10 %10
cent2 = num2//100 %10
mil2 = num2//1000 %10
print('Tratamento Matemático 2\n\nunidade: {}\ndezena:  {}\ncentena: {}\nmilhar:  {}'.format(un2,dez2, cent2, mil2))