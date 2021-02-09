"""
Map

Com Map, fazemos mapeamento de valores para função


import math

def area(r):
     Calcula a área de um circulo com um raio 'r'.
    return math.pi * (r **2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma utilizando Map

# Map é uma função que receb dois parâmetro: O primeiro é a função, o segundo um iterável

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Map com Lambda
print(list (map(lambda r: math.pi * (r ** 2), raios)))

#OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.

"""
# Exemplos

cidades = [('Berlim', 29), ('Cairo',36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londreas', 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
