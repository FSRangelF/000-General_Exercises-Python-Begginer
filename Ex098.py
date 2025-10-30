from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    p = abs(p)
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if f >= i:
        for c in range(i, f+1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    if f < i:
        for c in range(i, f-1, -p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    print('FIM')


# main
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input(f'{"Início: ":<8}'))
f = int(input(f'{"Fim: ":<8}'))
p = int(input(f'{"Passo: ":<8}'))
contador(i, f, p)


