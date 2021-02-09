"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1  - Importando todo o módulo (Não recomendado).

import random

# random() -> gera um número real pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo o modulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em memória). Caso você saiba quais funções você precisa utiliar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos op nome do  pacote e o nome da função,
# separados por pornto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas
# uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo (Forma recomendada)

from random import random

# No import acima estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> Gerar um número real pseudo-aleatório entre valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7))

# randint() -> Gera valores pseudo-aleátorios entre os valores estabelecidos.

from random import randint

# Gerador de apostas para a mega-sena

for i in range(6):
    print(randint(1, 61), end=' ')

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""
from random import shuffle

# shuffle() -> Tema função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas)