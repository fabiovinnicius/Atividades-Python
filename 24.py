c = str(input('Digite o nome da sua cidade: ')). strip()
c2 = c.split()
c3 = c2[0]
v = 'Santo' in c3
if v:
    print(f'A sua cidade {c} começa com Santo.')
else:
    print (f'A sua cidade {c} não começa com Santo.')