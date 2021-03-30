#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

"""
Fun��es de Maior Grandeza - Higher Order Functions - HOF

O que isso  significa?

- Quando uma linguagem de programa��o suporta HOF, indica que podemos ter fun��es
que retornam outras fun��es como resultado ou mesmo que podemos passar fun��es como
argumentos para outras fun��es, e at� mesmo criar vari�veis do tipo de fun��es
nos nossos programas.

OBS: Na se��o de fun��es, n�s utilizamos isso.

Em Python, as fun��es s�o cidad�es de primeira classa, First call citizien

# Exemplo - Definindo as fun��es

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


# Testando as fun��es

print(calcular(2, 4, somar))

print(calcular(4, 4, diminuir))

print(calcular(2, 5, multiplicar))

print(calcular(15, 3, dividir))

# Nested Functions - Fun��es Aninhadas

# Em Python podemos tamb�m ter fun��es dentro de fun��es , que s�o conhecidas por Nested Functions
# ou tamb�m Inner Functions (Fun��es Internas).

# Exemplo

from random import choice

def saudadacoes(pessoa):
    def humor():
        return choice(['E ai ', 'Suma daqui ', 'Gosto muito de voc� '])
    return humor() + pessoa


# Testando 
print(saudadacoes('Lucas'))

# Retornando fun��es de outras fun��es

from random import choice

def faz_me_rir():
    def rir():
        return choice(('kkkkkkkkkkk', 'hahahahahahahahahahahah', 'ehehehehehehehehehe'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())



"""
# Inner Functions (Fun��es Internas / Nested Functions) podem acessar o escopo de fun�oes mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkkkkkkkkkkkkk', 'heheheheheheheheheh', 'lalalalala'))
        return f' A {pessoa} sempre ri dessa forma {risada}'
    return dando_risada


rindo = faz_me_rir_novamente('Lucas ')

print(rindo())