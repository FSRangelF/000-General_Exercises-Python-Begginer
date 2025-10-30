nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2

if media >= 7.0:
    print('Parabéns. Você foi APROVADO com média {:.1f}'.format(media))
elif media < 5.0:
    print('Você foi REPROVADO com média {:.1f}'.format(media))
else:
    print('Você está de RECUPERAÇÃO com média {:.1f}'.format(media))