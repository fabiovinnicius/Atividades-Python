from random import randint
n1= int (input('Digite um número de 1 a 5: '))
n2= randint(1,5)
if n1 == n2:
    print('Você acertou! ')
else:
    print('você errou :( o valor correto era {}'.format(n2))