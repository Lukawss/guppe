"""
Seek e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt')

print(arquivo.read())

# seek() -> A função seek() é utilizada para a movimentação do cursor pelo arquivo. Ela recebe um
# parâmetro que indica onde queremos colocar o cursor.

# Movimentando o cursor pelo arquivp com a função seek()
arquivo.seek(0)

print(arquivo.read())

arquivo.seek(11)

print(arquivo.read())


arquivo = open('texto.txt')



# readline() -> função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))


# readlines()


print(arquivo.readlines())

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com um função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos como arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo

3- Fechar o arquivo;

# 1 - Abrir o arquivo;
arquivo = open('texto.txt')

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed) # Verifica se o arquivo está aberto ou fechado

# 3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)



"""

arquivo = open('texto.txt')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(10))



