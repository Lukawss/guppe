"""
Tipo Booleano

Algebra Booleana, criada por Gerorge Boole

2 constantes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negado (not):
"""
Fazendo a negação, se o valor booleanoo for verdadeiro o resultado será falso,
se for flaso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""
print(not ativo)

logado = False


# ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operaçãoo binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiros

True and True -> True
True and False -> False
False and False -> False
False and False -> False
"""