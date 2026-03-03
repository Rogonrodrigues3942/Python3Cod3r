print('\nAula #17 - Estrutura de Conrole -  FOR #01.\n')

#^ Forma básica de declaração.
print('\n#01 - Forma básica de declaração.')
for i in range(10):
    print('Valor de i:', i, 'na linha #', i + 1)

#^ Forma de limitação de delaração, com parâmetros de início e fim.
print('\n#02 - Forma de limitação de delaração, com parâmetros de início e fim.')
# print('\n\n')
for i in range(5, 10):
    print('Valor de i:', i, 'na linha #', i + 1)

#^ Forma de limitação de delaração e com intervalo de retorno: parâmetro de início, fim e intervalo de renderização.
print ('\n#03 - Forma de limitação de delaração e com intervalo de retorno: parâmetro de início, fim e intervalo de renderização.')
# print('\n\n')
for i in range(1, 100, 7):
    print('Valor de i:', i, 'na linha #', i + 1)

#^ Forma de limitação de delaração e com intervalo de retorno: parâmetro de início, fim e intervalo de renderização. Ordem decrescente.
print ('\n#04 - Forma de limitação de delaração e com intervalo de retorno: parâmetro de início, fim e intervalo de renderização.\nOrdem descrescente;')
# print('\n\n')
for i in range(50, 0, -7):
    print('Valor de i:', i, 'na linha #', i)

#^ Percorrendo um array (lista), utilizando o controle for.
print('\n#05 - Percorrendo um array (lista), utilizando o controle for.')
nums1 = [1, 3, 5, 7, 9]
for n in nums1:
    print(n, end =' ')

#^ Percorrendo um array (lista), utilizando o controle for.
print('\n#05 - Percorrendo um array (lista), utilizando o controle for.')
nums2 = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
for n in nums2:
    if n % 2 == 0:
        print(n, end =' ')

#^ Percorrendo uma string, utilizando o controle for.
print ('\n#06 - Percorrendo uma string, utilizando o controle for.')
texto = 'Python é muito amigável e simples!'
for t in texto:
    print(t)

#^ Percorrendo uma string(uma única linha), utilizando o controle for.
print ('\n#06 - Percorrendo uma string, utilizando o controle for.')
texto = 'Python é muito amigável e simples!'
for t in texto:
    print(t, end = ' ')