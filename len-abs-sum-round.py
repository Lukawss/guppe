"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho ( ou seja, o número de itens) de um iterável.

# Exemplo de len
print(len('Geek University'))

# Por debaixo dos panos, quando utilizamos a função len() o Python fas o seguinte:

# Dunder len
print('Geek Unbiversity'.__len__())

#Abs

abs() -> Retorna o valor absoluto de um númeto inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplo Abs

print(abs(-5))
print(abs(5))
print(abs(3.78))
print(abs(-3.78))

#Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
 incluindo o valor inicial.

#OBS: O valor inicial default = 0

# Exemplo Sum

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 35))

# Round

round() -> Retorna um número arredondado para  o digito de precisão após a casa decimal. Se a precisão não for
informada retorna o inteiro mais próximo da entrada.

# Exemplos Round

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.212121212129, 2))

print(round(1.2299999999999999, 2))
"""

