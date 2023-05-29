import math

a = float(input('Qual é o ângulo?  '))

sen = round(math.sin(math.radians(a)), 2)

cos = round(math.cos(math.radians(a)), 2)

tan = round(math.tan(math.radians(a)), 2)

degrees = math.floor(math.degrees(math.asin(sen)))

print(f'O valor do seno é igual a {sen}, o do cos é {cos} e o da tangente é {tan}')

print(f'o ângulo, novamente, equivale a {degrees}')