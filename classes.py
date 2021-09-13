#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
"""
POO - Classes

Em POO, Classes nada mais s�o do que modelos de objetos  do mundo real sendo representados
computacionalmente.

Imagina que voc� queira fazer um sistema para automatizar o controle das l�mpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracter�sticas do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da l�mpada, possivelmente
    ir�amos querer saber se a l�mpada � 110 ou 220 volts, se ela � branca, amarela, vermelha ou
    outra cor, qual � a luminosidade dela e etc.
    
    - M�todos (fun��es) -> Representam os comportamentos do objeto. OU seja, as a��es que este
    objeto pode realizar no seu sistema. No caso da l�mpada, por exemplo, um comportamento comum
    que muito provavelmente ir�amos querer representar no nosso sistema � o de ligar e desligar 
    a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de c�digo que ainda n�o est�
implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por conven��o o nome com inicial
em mi�sculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em mai�sculo,
todas juntas.

OBS: Quando estamos planejnaod um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que ser�o mapeados para classes de entidade.
"""

class Lampada:
    pass

class ContaCorrente:
    pass


lamp = Lampada()
print(type(lamp))

