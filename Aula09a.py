frase = ' Curso em Vídeo Python '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[0][3])
print(frase.replace('Python', 'Android'))
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
print('''Atualmente, a emissão de certificado individual custa R$40,00. Para incentivar 
e oferecer uma condição especial para os alunos que estão chegando agora, estamos oferecendo
R$50,00 de desconto na contratação do Plano Aluno Apoiador Anual.
Neste pacote, que tem custo original de R$ 200,00 anual, você pagará no primeiro ano R$150,00 
com direito a 12 créditos imediatos para emissão de certificados.''')

