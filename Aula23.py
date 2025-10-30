try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'tivemos um problema com o tipo de dado digitado')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario não digitou os dados')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print(f'Fim da Execução')