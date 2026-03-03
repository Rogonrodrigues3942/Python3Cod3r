print('\nBrincando com comando while.\n')

y = True
controle = 1

while y:
    print(controle)
    controle += 1
    if controle > 10:
        y = False
        print('\n\nFim de while!\n')