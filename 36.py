val= int(input('Digite o valor da casa que deseja comprar: R$ '))
sal= int(input('Digite seu salário: R$ '))
ano= int(input('Em quantos anos deseja estar financiando a casa? '))
prest= val / (ano * 12)
min= sal * 30 / 100
print('Para pagar uma casa de {} em {} anos'.format(val, ano), end='')
print(' a prestação será de R${:.2} '.format(prest))
if prest <= min:
    print('Seu empréstimo foi CONCEDIDO! ')
else: 
    print('Seu empréstimo foi NEGADO! ')