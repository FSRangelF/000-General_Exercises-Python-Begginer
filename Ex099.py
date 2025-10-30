from time import sleep

def maior(* valores):
    print('-='*40)
    print('Analisando valores passados...')
    for item in valores:
        print(item, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    print('O maior valor informado foi 0.' if len(valores) == 0 else f'O maior valor informado foi {max(valores)}.')


# Main
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()