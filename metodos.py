#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

"""
POO - M�todos

- M�todos (fun��es) -> Representam os comportamentos do objeto. Ou seja, as a��es
que este objeto pode realizar no seu sistema.

Em Python, dividimos os m�todos, em 2 grupos: M�todos de inst�ncia e M�todos de Classe.

# M�todos de Inst�ncia

# O m�todo dunder init __init__ � um m�todo especial chamado de construtor e sua
fun��o � construir o objeto a partir da classe.

OBS: Os m�todos/fun��es dunder em Python s�o chamados de m�todos m�gicos.

p1 = Produto('Playstation 4', 'Video Game', 2300)
user1 = Usuario('Lucas', 'de Souza Queiroz', 'lucas@gmail.com', 123456)

print(p1.desconto(50))
print(user1.nome_completo())
print(user1._Usuario__senha)
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp
class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Comfirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha n�o confere.....')

print('Usu�rio criado com sucesso!')

senha = input('Informe senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Accesso negado')

print(f'Senha User Criptografa: {user._Usuario__senha}')