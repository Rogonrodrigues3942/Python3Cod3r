print('Aula #13 - Operadores lógicos. \n')

b1 = True
b2 = False
b3 =True

# Operador lógico 'and'
print(b1 and b2 and b3)

# Operador lógico 'or'
print(b1 or b2 or b3)

# Operador lógico '!='
print(b1 != b2 != b3)

# Operador lógico 'not' - inverter valor booleano.
print(not b1)
print(not b2)
print(not b3)

# Operador lógico  and combinando com'not'.
print(b1 and not b2 and b3)

# Utilizando operadores lógicos com booleanos e números 
# mesclando com operadores relacionais.
x = 4
y = 6
print(b1 and not b2 and x < y)