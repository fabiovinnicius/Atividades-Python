num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 10):
    print('{} x {:2} = {}'.format(num, c, num*c))