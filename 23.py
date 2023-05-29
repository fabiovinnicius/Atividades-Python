numero=int(input('Informe um número: '))

uni = numero // 1 % 10

dez = numero // 10 % 10

cen = numero // 100 % 10

mil = numero // 1000 % 10

print(f' -- Analisando o número informado: {numero} \n'

f' Unidade do número informado: {uni} \n'

f' Dezena do número informado: {dez} \n'

f' Centena do número informado: {cen} \n'

f' Milhar do número informado: {mil}')