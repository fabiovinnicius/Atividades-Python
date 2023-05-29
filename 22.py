n = str(input('Digite um nome completo: '))

nn = n.split()[0]

print('O nome completo em maiúscula é {}.'.format(n.upper()))

print('O nome completo em minúscula é {}.'.format(n.lower()))

print('O total de letras do nome sem espaço é {}'.format(len(n) - n.count(' ')))

print('A quantidade de letras do primeiro nome é', len(nn))