"""
Levantando os próprios erros com raise

raise -> Lança exceçôes

OBS: I raise não é uma função. É uma palavra reservada, assim com def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro

A forma geral de utilização é:

raise TipoDo Error('Mensagem de erro')

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor pecisa ser uma string')
    else:
        print(f'O texto {texto} será impresso na cor {cor}')


colore('Olá', 'azul')


def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor pecisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar nesta listagem: {cores}')
    else:
        print(f'O texto {texto} será impresso na cor {cor}')


colore('Olá', 'azul')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.

"""

# Exemplo real

def colore(texto, cor):
    cores = ['verde', 'amarelo', 'azul', 'branco']
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor pecisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa estar nesta listagem: {cores}')
    else:
        print(f'O texto {texto} será impresso na cor {cor}')


colore('Olá', 'azul')