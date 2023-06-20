print('\033[1;0;35m {:=^40}'.format('LOJALES'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
op= int(input('Qual é a opção? '))
if op == 1:
    total = preço - (preço * 10 / 100)
if op == 2:
    total = preço - (preço * 5 / 100)
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
if op == 3:
total = preço
parcela = total / 2
print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
if op == 4:
total = preço + (preço * 20 / 100)
totparc = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else: total = 0
print('\033[1;0;41mOPÇÃO INVÁLIDA de pagamento. Tente novamente.')