a1= int (input('Digite o primeiro segmento: '))
a2= int (input('Digite o segundo segmento: '))
a3= int (input('Digite o terceiro segmento: '))
if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ')
if a1 == a2 == a3:
    print('O segmentos formam um triangulo equilátero. ')
elif a1 != a2 != a3 != a1:    
    print('Os segmentos formam um triangulo escaleno. ')
else: print ('Os segmentos formam um triangulo isósceles. ')