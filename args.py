"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que  começe por asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é *args

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em um tupla. Então desde de já lembre-se que tuplas são imutáveis .

# Exemplos

def soma(num1, num2, num3):
    return num1 + num2 + num3


print(type(soma))

print(soma(3, 3, 3))

# Entendendo o args

def soma(*args):
    return sum(args)


print(soma(1, 2, 3))
print(soma(5, 5, 9))
print(soma(10, 5.5, 10.3))


def verifica(*args):
    if 'Lucas' in args and 'Souza' in args:
        return 'Bem vindo Lucas de Souza'
    return 'Olá Visitante'

print(verifica('Lucas', 'Souza'))
print(verifica('Teste', 'Lucas'))

"""
def soma(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]
tupla = (1, 2, 3, 4, 5, 6, 7,)

print(soma(*tupla, *numeros))

# OBS: O asterisco serve para informar o Python que estamos
# passando como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar estes dados.