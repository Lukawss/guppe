"""
List Comprehension

-Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]


# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

res = [numero / 2 for numero in numeros]

print(res)

def funcao(num):
    return num * num


res = [funcao(numero) for numero in numeros ]

print(res)


#  List Comprehesion versus Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numero_dobrados = []

for numero in numeros:
    numero_dobradoo = numero * 2
    numero_dobrados.append(numero_dobradoo)


print(numero_dobrados)

# List Comprehension
print([numero * 10 for numero in numeros])

"""

nome = 'lucas de souza queiroz'

print([letra.upper() for letra in nome])

amigos = ['maria', 'joão', 'luan', 'daniel']

print([nome.title() for nome in amigos])


print([numero * numero for numero in range(1, 11)])


print([bool(valor) for valor in [0, [], '', True, 1, 3.15, 0.23]])

print([str(numero) for numero in [1, 2, 3, 4, 5]])
















