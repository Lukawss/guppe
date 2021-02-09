"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla= (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'i': 434, 'f': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'i': 434, 'f': 129}
print(max(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))

print(max(valor1, valor2))

print(max(4, 67, 78))

print(max('Lucas', 'Ana', 'Bia', 'Weelington'))

min() -> Retorna o menor valor me um iterável ou o menor de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'i': 434, 'f': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'i': 434, 'f': 129}
print(min(dicionario.values()))

# Faça um programa que receba dois valores do usuário e mostre o maior

valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))

print(min(valor1, valor2))

print(min(4, 67, 78))

print(min('Lucas', 'Ana', 'Bia', 'Weelington'))

# Mais exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))
print(min(nomes))
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

"""

musicas = [
    {"musica": "Times Like These", "reproduzida": 12},
    {"musica": "Decode", "reproduzida":23},
    {"musica": "Blind Lights", "reproduzida": 60},
    {"musica": "The Only Exception", "reproduzida": 45}

]


print(max(musicas, key=lambda musica: musica["reproduzida"]))

print(min(musicas, key=lambda musica: musica["reproduzida"]))


# DESAFIO! Imprima somente o titulo da música mais e menos tocada

print(max(musicas, key=lambda musica: musica["reproduzida"])["musica"])
print(min(musicas, key=lambda musica: musica["reproduzida"])["musica"])

# DESAFIO! Como encontrar a música mais e menos tocada ser usar o max(), min() e lambda.

max = 0
for musica in musicas:
    if musica["reproduzida"] > max:
        max = musica["reproduzida"]

for musica in musicas:
    if musica["reproduzida"] == max:
        print(musica["musica"])

min = 99999
for musica in musicas:
    if musica["reproduzida"] < min:
        min = musica["reproduzida"]

for musica in musicas:
    if musica["reproduzida"] == min:
        print(musica["musica"])
