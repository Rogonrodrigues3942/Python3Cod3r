def saudacao():
    print('\nBom dia!!')

# Sobrecarga
def saudacao():
    print('\nBoa tarde!!')

def saudar_pessoa(nome = 'Pessoa'):
    print(f'\nBom dia {nome}!!')

def saudar_pessoa_idade(nome = 'indvíduo', idade = 20):
    print(f'\nBom dia {nome}!!\nVocê nem para ter {idade} anos!!')

# Execucção direto pelo arquivo basic.
if __name__ == '__main__':
    saudacao()
    saudar_pessoa('Samuel')

#Trabalhando com retornos de funções
def soma_e_mult(a, b, x):
    return (a + b) * x