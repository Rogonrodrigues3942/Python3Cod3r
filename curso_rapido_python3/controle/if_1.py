print('Aula #15 - Estrutura de Conrole -  IF #01.\n')

nota = float(input('Informa a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Duas palavras> para béns!: P')
    print('Quadro de honra!')
    print ('Anota do aluno é: ', nota)
elif nota >= 6:
    print('Aluno está aprovado!')
    print ('Anota do aluno é: ', nota)
else:
    print('Aluno está reprovado!')
    print ('Anota do aluno é: ', nota)
    