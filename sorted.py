"""
Sorted

OBS: Não confuda, apesar do nome com a função sort() que já estudamos em Listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para order.

OBS: O sorted(), SEMPRE retorna uma  lista com os elementos do iterável ordenados

# Exemplo

numeros = {56, 3, 45, 12, 1, 5, 231}
print(numeros)
print(sorted(numeros))


# Adicionando parâmetros ao sorted()
numeros = [56, 3, 45, 12, 1, 5, 231]

print(numeros)

print(sorted(numeros))

print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo númeto de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))


"""

# Exemplo

musicas = [
    {"musica": "Times Like These", "reproduzida": 12},
    {"musica": "Decode", "reproduzida": 23},
    {"musica": "Blind Lights", "reproduzida": 60},
    {"musica": "The Only Exception", "reproduzida": 45}

]

# Da menos tocada para a  mais tocada
print(sorted(musicas, key=lambda musica: musica["reproduzida"]))

# Da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica["reproduzida"], reverse=True))

# Ordenação em ordem alfabética
print(sorted(musicas, key=lambda musica: musica["musica"]))

