def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 65 or 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 18:
        return f'Com {idade} anos: VOTO NEGADO'


# MAIN
print('-'*30)
n = int(input('Em que ano você nasceu? '))
print(voto(n))
