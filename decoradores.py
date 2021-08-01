#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
"""
Decoradores (Decorators)

O que s�o decorators?

- Decorators s�o fun��es;
- Decorators envolvem outras fun�~pes e aprimoram seus comportamentos;
- Decorators tamb�m s�o exemplos de Higher Order Functions;
- Decorators tem uma sintaxe pr�pria, usando "@" (Syntac Sugar / A��car Sint�tco)

# Decorators com fun��es (Sintaxe n�o recomendada / Sem A��car Sint�tico)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer voc�')
        funcao()
        print('Tenha um �timo dia!')
    return sendo

def saudacao():
    print('Seja bem vindo(a) `a Geek University')

# Testando 1

# saudacao()

teste = seja_educado(saudacao)
teste()


# Testando 2

def raiva():
    print('EU TE ODEIO!!!!!!')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com Syntax Sugar (A��car Sint�tico)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voc�')
        funcao()
        print('Tenha um excelente dia!!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome � Lucas")


# Testando

apresentando()

"""

# OBS: N�o confunda Decorator com Decorator Function

