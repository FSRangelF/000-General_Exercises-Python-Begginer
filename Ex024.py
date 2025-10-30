nome = str(input('Digite o Nome da Cidade: ')).upper().strip()
print('O nome inicia-se com SANTO? {}'.format((nome[:5] == 'SANTO')))
print('O nome inicia-se com SANTO? {}'.format('SANTO' in nome.split()[0]))
