peso = float(input('Qual seu peso? (kg) '))
altura = float (input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal ')
elif imc >= 18.5:
    print('Você está na faixa de peso normal ')
elif 25 <=  imc < 30:
    print('Você está em SOBREPESO! ')
elif 30 <= imc < 40:
    print('VocẼ está em OBESIDADE. Cuidado! ')
elif imc >=40:
    print('Você está em OBESIDADE MÓRBIDA. Cuidado! ')