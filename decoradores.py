#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funç~pes e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntac Sugar / Açúcar Sintátco)

# Decorators com funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia!')
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

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Lucas")


# Testando

apresentando()

"""

# OBS: Não confunda Decorator com Decorator Function

