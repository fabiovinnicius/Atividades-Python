from random import randint
from time import sleep
n1= randint(0, 2)
n2= int (input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual é a sua jogada? '''))
print('-=' * 11)
sleep(1)
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!')
sleep(1)
print('-=' * 11)
if n1 == 0:
    print('''Computador jogou pedra''')
elif n1== 1:
    print('''Computador jogou papel''')
elif n1 == 2:
    print('''Computador jogou tesoura''')
if n2 == 0:
    print('''Jogador jogou pedra''')
elif n2== 1:
    print('''Jogador jogou papel''')
elif n2 == 2:
    print('''Jogador jogou tesoura''')
if n1 == n2:
    print('Não houve um ganhador')
elif n2 == 0 and n1 ==1:
    print('Computador ganhou!!')
elif n2 == 1 and n1 ==0:
    print('Jogador ganhou!!')
elif n2 == 1 and n1 == 2:
    print('Computador ganhou!!')
elif n2 == 2 and n1 == 0:
    print('Computador ganhou!!')
else: print('Jogador ganhou!!')
print('-=' * 11)
print('Fim de jogo')