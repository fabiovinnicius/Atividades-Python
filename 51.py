primeiro = int (input('Primeiro termo: '))
razão = int (input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, 10, razão):
    print('{}'.format(c), end= '➝')
print('ACABOU! ')