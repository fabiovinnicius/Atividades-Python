num= int(print('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção= int(input('Sua opção é: '))
if opção == 1:
    print('{} convertido para BINÁRIO é: '.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é: '.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é: '.format(num, hex(num)))