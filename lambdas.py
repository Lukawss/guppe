"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome ou funções anônimas.

# Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# Como utilizar a expressõ lambda?
calc = lambda x: 3 * x + 1

print(funcao(4))
print(funcao(7))

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' lucas', 'de souza queiroz'))
print(nome_completo('LUCAS', 'DE SOUZA QUEIROZ'))

# Em funções Python podemos ter nenhuma ou várias entradas, em lambda também

texto = lambda : 'Isto é uma Lambda'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x1, ......., xn: <expressão>

print(texto())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

autores = ['Issac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""
# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(funcao_quadratica(3, 0, 1)(2))
















