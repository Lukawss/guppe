#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys

from random import choice

var = input("Digite seu nome: ").title()

usuario = var





def acesso(usuario):
    def chave():
        return choice(range(10000, 50000))
    return f' Seja bem vindo: {usuario} \n Chave de acesso: {chave()}'




print(acesso(usuario))