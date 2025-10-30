s = 0
cont = 0
for c in range(0, 501, 3):
    if (c % 2) != 0:
        s = s + c
        cont = cont + 1
print(cont, s)