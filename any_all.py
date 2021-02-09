"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4])) # False, pois tem o 0

print(all([ 1, 2, 3, 4])) # True, pois todos o números são verdadeiros

print(all([])) # True, pois o iterábel esta vazio

print(all((1, 2, 3, 4))) # True, pois todos o números são verdadeiros

print(all({1, 2, 3, 4})) # True, pois todos o números são verdadeiros

print(all('Geek')) # True, pois é uam string

nomes = ['Lucas', 'Letica', 'Laura', 'Larissa']

print(all([nome[0] == 'L' for nome in nomes]))

# OBS: Um iterável vazio convertiso em boolean é False, mas no all() entende como True
print(all([letra for letra in 'qwer' if letra in 'aeiou']))

any() -> Retorna True se qualquer element do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, []]))  # False

nomes = ['Lucas', 'Letica', 'Laura', 'Larissa', 'Thamara']

print(any([nome[0] == 'L' for nome in nomes]))





