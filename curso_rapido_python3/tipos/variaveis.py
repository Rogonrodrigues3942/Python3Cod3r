a = 3
b = 4.4

print(a + b)

text = 'Sua idade eh... '
idade = 23

#print(text + idade)
#print(text + str(idade) + ' anos.')

print(f'{text} {idade}')
print(3 * idade)
print(3* text)
print(4 * 'Bom dia!')

PI = 3.1415
raio = float(input("Informe o raio da circ: "))

import math
circ = PI*pow(raio,2)
print(circ)