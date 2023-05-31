a1= float(input('Digite o primeira ângulo: '))
a2= float(input('Digite o segundo ângulo: '))
a3= float(input('Digite o terceiro ângulo: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ')
else:
    print('Os segmentos acima NÃO podem formar um triângulo! ')