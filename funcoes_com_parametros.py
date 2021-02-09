"""
Funções com Parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralemnte temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não pssuem entrda;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função

def quadrado(var):
    return var * var

print(quadrado(5))
print(quadrado(7))

valor = quadrado(4)

print(valor)


def cantar_parabens(nome):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a/o {nome}!')

cantar_parabens('Lucas')


# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrda
# em uma função  quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplos


def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(c, d, e):
    return (c + d) * e

print(soma( 10, 95))
print(multiplica(9, 2))
print(outra(9 , 3, 'Teste '))

# OBS: Se a gente informar um número errado de parâmetro ou argumento, teremos TypeError

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Meu nome completo é {nome} {sobrenome}'


print(nome_completo('Lucas', 'de Souza Queiroz'))


# Diferença entre Parâmetros e Argumentos

# Parâmetro são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá=los, podemos
# utiizar qualquer ordem

nome = 'Lucas'
sobrenome = 'Queiroz'

print(sobrenome, nome)

print(nome_completo(sobrenome=sobrenome, nome=nome))

"""

# Erro comum na utilização do return

def soma_impares(num):
    total = 0
    for a in num:
        if a % 2 != 0:
            total = total + a
    return total

if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9, 10, 13]
    print(soma_impares(lista))

