#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
"""
POO - Atributos

Atributos -> Representam as caracter�sticas do objeto. Ou seja, pelo atributos
nos conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
-Atributos de Inst�ncia;
-Atributos de Classe;
- Atributos Din�mico;

# Atributos de inst�ncia: S�o atributs declarados dentro do m�todo construtor.

# OBS: M�todos construtos: E um m�todo especial utiliado para aconstru��o do objeto.

Em Python, por conven��o, ficou estabelecido que, todo atributo de uma classe � publico.
Ou seja, pode ser acessado em todo projeto.
Caso queiramos  demostrar que determinado atributo deve ser tratado com privado, ou seja,
qque deve ser acessado/utilizado somente dentro da pr�pria classe onde est� declarado,
utiliza-se __ duplo underscore no �nicio de seu nome.

Isso � conhecido tamb�m como Name Mangling.


#OBS: � apenas uma conven��o

user = Acesso('user@gmail.com', '123576')

print(user.email)

# print(user.senha) # AttributeError

print(user._Acesso__senha) # Temso acesso. Mas n�o dever�aramos fazer este acesso. (Name Mangling)

user.mostra_senha()
user.mostra_email()

# O que significa atributos de inst�ncia?

# Significa, que ao criarmos inst�ncias/objetos de uma classe, todas as inst�ncias
# ter�o estes atributos.

user1 = Acesso('user1@gamil.com', '123456')
user2 = Acesso('user2@gamil.com', '654321')

user1.mostra_email()
user2.mostra_email()


"""
# Classes com Atributo de Inst�ncia  P�blicos

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com Atributos Privados e p�blicos

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Atributos de Classe

p1 = Produto('Macbook Pro', 'Notebook', 9000)
p2 = Produto('Macbook Air','Notebook', 7000)


# Refatorar a classe Produto


class Produto:

    # Atributo de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Macbook Pro', 'Notebook', 9000)
p2 = Produto('Macbook Air', 'Notebook', 7000)

print(p1.id)
print(p2.id)


# Atributos Din�micos -> Um atributo de inst�ncia que pode ser criado em tempo de execu��o.

# OBS: O atributo din�mico ser� exclusivo da inst�ncia que o criou.

p1 = Produto('Macbook Pro', 'Notebook', 9000)
p2 = Produto('Macbook Air', 'Notebook', 7000)

# Criando um atributo din�mico em tempo de execu��o

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descri��o: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')

print(p1.__dict__)
print(p2.__dict__)


# Deletando atributos

del p2.peso
del p2.valor
del p2.descricao

print(p2.__dict__)

