def escreva(msg):
    l = len(msg) + 6
    print('~' * l)
    print(f'{msg:^{l}}')
    print('~' * l)


escreva('FRANCISCO RANGEL')
escreva('CURSO DE PYTHON NO YOUTUBE')
escreva('CEV')
