#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Preservando metadatas com Wraps

Metadados -> S�o dados intr�secos em arquivos.

Wraps -> S�o fun��es que envolvem elementos com diversas finalidades.

# Problema 
def ver_log(funcao):
    def logar(*args, **kwargs):
       # Eu sou uma fun��o (logar) dentro de outra
        print(f'Voc� est� chamando: {funcao.__name__}')
        print(f'Aqui a documenta��o: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
   #Soma dois n�meros
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)


"""

# Resolu��o do Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma fun��o (logar) dentro de outra"""
        print(f'Voc� est� chamando: {funcao.__name__}')
        print(f'Aqui a documenta��o: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois n�meros"""
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)

