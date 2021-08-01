# -*- coding: utf-8 -*-
"""
Decorators com diferentes assinaturas


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, e de acompanhamento quero o {acompanhamento}, por favor.'


print(saudacao('Lucas'))

print(ordenar('Risoto', 'Batata Rústica'))


# Para resolver utiizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs)

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordernar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, e de acompanhamento quero o {acompanhamento}, por favor.'

print(saudacao('Lucasss'))

print(ordernar('Risoto', 'Batata Frita'))

# OBS: Vale lembrar que podemos utilizar parâmetro nomeados


"""

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, ** kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return  funcao(*args, ** kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(*args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(2, 12))
print(comida_favorita('pizza', 'churrasco'))