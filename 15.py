d = int(input(' Quantas diárias foram alugadas?'))

km = float(input('Quantos quilômetros foram rodados?'))

p = d * 60 + km * 0.15

print('O valor a ser pago pelo aluguel equivale a R$ {}! ' .format(p))
