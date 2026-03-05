print('\nAula 19 - For #2\n\n')

pessoas = ['Gui', 'Rebeca']
adjs = ['sapeca', 'inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} é {a}.')


#* Exemplo 2: pass
for i in [1, 2, 3 ]:
    pass

#* Exemplo 3: continue
for i in range(1, 11):
    if i % 2:
        continue
    print('conitnue --> número = ', i)

#* Exemplo 4: break
for i in range(1, 11):
    if i == 5:
        break
    print('break --> Número = ', i)