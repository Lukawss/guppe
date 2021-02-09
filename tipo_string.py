"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas ->'''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4]) # Slice de string

print(nome[5:15]) # Slice de string

# [   0,        1]
# ['Geek', 'Uniiversity']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = 'Geek University'

"""
[:: -1] -> Comeca do primeiro elemento,vá até o último elemento e inverta
"""
print(nome[:: -1]) # Inversão da string Pythônico

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socoram me subino onibus em marrocos' # Palíndromo
print(texto)
print(texto[::-1])
