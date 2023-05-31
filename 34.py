s= float(input('Digite o salário do funcionário R$ '))
if s<=1250: 
    n = s + (s * 15 / 100)
else: n = s + (s * 10 / 100)
print('O funcionario que ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, n))