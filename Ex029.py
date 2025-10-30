vel = float(input('digite a velocidade do carro: '))
if vel > 80:
    print('MULTADO. Você trafegou acima da velocidade permitida de 80km/h.')
    print('Sua velocidade foi de {}Km/h e vc tera de pagar uma multa de R${:.2f}'.format(vel, ((vel-80)*7)))
print('Tenha um bom dia, Dirija com Segurança')
