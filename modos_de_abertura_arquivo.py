
#-*- coding:latin1 -*-
"""
Modos de Abertura de Arquivo
r -> Abre para leitura - padr�o
w -> Abre para escrita - sobrescreve caso o arquivo j� exista
x -> Abre para escrita somente se o arquivo na existir. Caso o arquivo exista, gera FileExistsError
a -> Abre para escrita, adicionando o conte�do ao final do arquivo
+ -> Abre para o modo de atualiza��o: Leitura e escrita

# OBS: Abrindo no modo 'a' -> append, se o arquivo n�o existir ser� criado. Caso exista o novo conte�do
ser� adiconado ao final SEMPRE. Com o modo 'a' n�o controlamos o cursor

http://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conte�do 2')
except FileExistsError:
    print('Arquivo j� existe')

# Exemplo a
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe um fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta.title())
            arquivo.write('\n')
        else:
            break

"""
with open('novo.txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo � ! \n')