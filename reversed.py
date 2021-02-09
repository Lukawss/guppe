"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em lista.

Já a função reversed() funciona com qualquer iterável.

Sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento reroenado para uma Lista, Tupla ou Conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordemdos elementos
# Conjunto
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Lucas de Souza Queiroz'))))

# Slice de strings
print('Lucas de Souza Queiro'[:: - 1])

# Podemos utilizar o reversed() para fazer um loop reverso
for n in range(1, 21):
    print(n, end=' ')

print('\n')

for n in reversed(range(1, 21)):
    print(n, end=' ')

print('\n')

for n in range(21, -1, -1):
    print(n, end=' ')
