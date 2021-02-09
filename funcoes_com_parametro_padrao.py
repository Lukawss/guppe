"""
Funçãos com Parâmetro Padrão ( Default Paramters)

- Funções onde a passagem de parâmetros seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Geek University')

print()

# Exemplo  de função onde a pasagem de parâmetro seja obrigátoria

def quadrado(numero)
    return numero **


print(quadrado(3))
print(quadrado()) # TypeError


def exponecial(numero=3, potencia=2):
    return numero ** potencia

print(exponecial(5,3))
print(exponecial(3,2))

print(exponecial(2))
print(exponecial())

#OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# Exemplo

def mostra_informacao(nome='Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem Vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Lucas'))
print(mostra_informacao(nome='Teste'))

 Por que utilizar parâmetros com valor default?

 - Nos permite ser mais flexíveis nas funções;
 - Evita erros com parâmetros incorretos;
 - Nos permite trabalhar com exemplo mais legíveis de código;

 Quais tipo de dados podemos utilizar como valores default para parâmetros?

 - Números, string, floats, booleanos, listas, tuplas, dicionários, funções e etc;

 # Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 5))
print(mat(5, 1, subtracao))


# Escopo - Evitar problemas e confusões....

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Olá {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'

print(diz_oi())

print(prof) #NameError

# ATENÇÃO com variáveis globais ( Se puder evitar, evite)

total = 0

def incrementa():
    total = total + 1 # UnboundLocalError
    return total

print(incrementa())

# ATENÇÃO com variáveis globais ( Se puder evitar, evite)

total = 8

def incrementa():
    global total
    total = total + 2
    return total

print(incrementa())
print(incrementa())
print(incrementa())

"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 8

    def dentro():
        nonlocal contador
        contador = contador + 2
        return contador
    return dentro()

print(fora())
print(fora())

