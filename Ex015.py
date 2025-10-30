d = int(input('Informe a quantidade de dias alugados: '))
km = float(input('Informe a quantidade de Kilometros rodados: '))
print('O total devido para {:.0f} dias e {:.2f}Km é de R${:.2f}'.format(d, km, ((60*d)+(km*0.15))))
