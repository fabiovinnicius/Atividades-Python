from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
saldo= idade - 18
print('Quem nasceu em {} tem {} anos em {} '.format(nasc, idade, atual))
if idade == 18: print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18: print('Você terá que se alistar ainda não tem 18 anos. Ainda falta {} anos para o alistamento.')
elif idade > 18: print('Você deveria ter se alistado há {} anos.'.format(saldo))
