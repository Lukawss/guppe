#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso  significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções como
argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são cidadões de primeira classa, First call citizien

# Exemplo - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(2, 4, somar))

print(calcular(4, 4, diminuir))

print(calcular(2, 5, multiplicar))

print(calcular(15, 3, dividir))

# Nested Functions - Funções Aninhadas

# Em Python podemos também ter funções dentro de funções , que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas).

# Exemplo

from random import choice

def saudadacoes(pessoa):
    def humor():
        return choice(['E ai ', 'Suma daqui ', 'Gosto muito de você '])
    return humor() + pessoa


# Testando 
print(saudadacoes('Lucas'))

# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('kkkkkkkkkkk', 'hahahahahahahahahahahah', 'ehehehehehehehehehe'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())



"""
# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funçoes mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkkkkkkkkkkkkk', 'heheheheheheheheheh', 'lalalalala'))
        return f' A {pessoa} sempre ri dessa forma {risada}'
    return dando_risada


rindo = faz_me_rir_novamente('Lucas ')

print(rindo())