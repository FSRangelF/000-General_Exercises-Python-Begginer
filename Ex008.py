n = float(input('Digite o valor em metros: '))
print('{:.2f} metros equivale a\n{:.3f} kilometros\n{:.3f} hectometros\n{:.3f} decametros\n{:.1f} decimetros\n{:.0f} centímetros e\n{:.0f} milímetros'.format(n, (n/1000), (n/100), (n/10), (n*10), (n * 100), (n * 1000)))

