"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1 ]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

#OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.


paises = ['', 'Argentina', '', 'Brasil', 'Chiile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

# A diferença em map() e filter() é:

# map() -> Recebe dois parâmetos, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.



usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários inativos no Twitter

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))


print(inativos)

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 1, usuarios))

print(inativos)
"""

# Combinas filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos que 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) > 3, nomes)))

print(lista)

