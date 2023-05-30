d= float(input('Qual a distancia da sua viagem? '))
print('Você irá iniciar uma viagem de {}km.'.format(d))
if d<= 200: 
    p = d * 0.50
else:
    preço = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(p))