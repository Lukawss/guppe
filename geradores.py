"""
Geradores

- Geradores (Generators) são iteráveis (Iteradores);

OBS: O contrário não é verdadeiro, ou seja nem todo iterator é um generetor.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

Funções:
    Utilizam return
    Retorna uma vez
    Quando executado, retorna um valor



Generator Functions;
    Utilizam yield
    Podem utilizar yield múltiplas vezes
    quando executada, retorna um generator


# Exemplo Generator Functions

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


# OBS: Uma generator Function não é um Generator, ela gera um generator!

gen = conta_ate(5)

#print(type(gen))

print(next(gen))

for n in gen:
    print(n)


"""

# Exemplo Generator Functions

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = list(conta_ate(10))

print(gen)







