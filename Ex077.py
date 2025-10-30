palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for i in range(0, len(palavras)):
    p = str(palavras[i])
    print(f'Na palavra {p.upper()} temos ', end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('')
