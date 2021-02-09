"""
Generators Expression
Em aulas anteriores nós estudamos:
 - List Comprehension;
 - Dictionary  comprehension;
 - Set Comprehension;

Não vimos:
 - Tuple Comprehension... porque elas se chamam Generators

nomes = ['Lucas', 'Leticia', 'Laura', 'Larissa','Karen']

print(any([nome[0] == 'L' for nome in nomes]))

# List Comprehension
res = [nome[0] == 'L' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'L' for nome in nomes)
print(type(res))
print(res)

# Qual é a função de getsizeof()? -> Retorna a quantidade de bytres em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string está ocupando em memória. Quanto amsior a string, mais espaço ocupa.
print(getsizeof('Lucas'))
print(getsizeof('Lucas de Souza Queiroz'))
print(getsizeof(10000))
print(getsizeof(90))
print(getsizeof(23.9090))
print(getsizeof(False))
print(getsizeof(True))


# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f' List Comprehension: {list_comp} bytes')
print(f' Set Comprehension: {set_comp} bytes')
print(f' Dictionary Comprehension: {dic_comp} bytes')
print(f' Generator Expression: {gen} bytes')


"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(11))
print(gen)

for num in gen:
    print(num)







