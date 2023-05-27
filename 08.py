medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
M = medida
dam = medida / 10
hec = medida / 100
km = medida / 1000

print(f'{medida} metros correspondem a:')
print(f'{mm} milimetros')
print(f'{cm} centimetros')
print(f'{dm} decimetros')
print(f'{M} metros')
print(f'{dam} decametros')
print(f'{hec} hectametros')
print(f'{km} kilometros')