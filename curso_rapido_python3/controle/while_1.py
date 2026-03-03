x = 0

while x != -1:
    x = float(input('Infome o número ou -1 para sair: ') )

print('Fim! 1')

#^ Cálculo de média de alunos.
nota = 0
qtde = 0
total = 0.0

while nota >= 0:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota >= 0:
        qtde += 1
        total +=nota


if nota >= 0:
    media = total / qtde
    print(f'A média da turma é: {media}')
    print(f'A turma tem {qtde} alunos.')

print('Fim! 2')

#^ Repetições decrementando
y= 10
while y:
    print(y)
    y -= 1

print('Fim! 3')