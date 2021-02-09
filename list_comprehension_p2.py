"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas as nossas List Comprehension
"""

# Exemplos

# 1

numeros = list(range(1, 31))

print([numero for numero in numeros if numero % 2 == 0])
print([numero for numero in numeros if numero % 2 != 0])

# Refatorar

# Qualquer número par módulo de 2 é o 0 e 0 em Python é False. not False = True
print([numero for numero in numeros if not numero % 2])

# Qualquer número impar módulo 2 é 1, e 1 em Python é True
print([numero for numero in numeros if numero % 2])

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)

