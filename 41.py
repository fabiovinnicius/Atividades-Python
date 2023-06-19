from datetime import date
atual = date.today().year
ano= int (input('Ano de nascimento: '))
idade = atual - ano
if idade <= 9:
    print('Atleta Mirim')
elif idade <= 14: 
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade < 25:
    print('Atleta Sênior')
elif idade >= 25:
    print('Atleta MASTER')