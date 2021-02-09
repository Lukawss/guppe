"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""

# Exemplos

from collections import Counter

numeros = { num for num in range(1, 7)}
print(numeros)

numeros = { x ** 2 for x in range(11)}
print(numeros)

# Desafio

numeros = {x: x ** 2 for x in range(11)}
print(numeros)

letras = {letra for letra in 'Lucas de Souza Queiroz'}
print(letras)

