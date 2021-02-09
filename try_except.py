"""

O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Prevenindo assim que o programa pare
de funcionar e o usúario receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Ops, aconteceu algum problema')

OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar
de forma esepecífica.

# Exemplo - Tratando erro específico

try:
    geek()
except NameError:
    print('Ops, aconteceu algum problema')

try:
    len(5)
except TypeError:
    print('Ops, aconteceu algum problema')

try:
    len(5)
except TypeError as erro:
    print(f'A aplicação gerrou o seguinte erro: {erro}') # detalhando o erro

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')

"""
dic = {"nome": "Lucas"}

def pega_valor(a, b):
    try:
        return a[b]
    except KeyError:
        return None
    except TypeError:
        return None

print(pega_valor(dic,9))