"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('texto.txt'))

# Diretório

# Path relativo
print(os.path.exists('geek/university'))

# Path absoluto
print(os.path.exists('C:\\Users\\lucas\\Documents\\Udemy Python')


# Criando arquivos

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3

with open('arquivo-teste3.txt', 'w') as arquivo:
    pass

# Não funciona no windows

os.mknod('arquivo-teste4.txt')
os.mknod('C:\\Users\\lucas\\python.txt')

# Criando diretórios - únicos (um a um)

# Relativo
os.mkdir('templates')

# Absoluto
os.mkdir('C:\\users\\lucas\\teste')

# OBS: A função mkdir() cria um diretório se este não existir, caso exista teremos o FileExistsError
# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)

os.makedirs('templates/geek/university')

# FileError se já existir

# Diretórios

os.rename('templates2','geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Renomear arquivos e diretórios

# Arquivos
os.rename('templates/geek/university/teste.txt','templates/geek/university/teste2.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório eles
# não vão para lixeira, eles somem.

# Removendo arquivos
os.remove('arquivo-teste4.txt')

# OBS: No Windows- se o arquivo estiver em uso teremos um erro.

# OBS: Se o arquivo não existir termos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, termos um IsADirectoryError

# Removendo diretórios vazios

os.rmdir('templates')

# OBS: Se o diretório tiver conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma arvore de arquivos
for arquivo in os.scandir('templates'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Removendo uma arvore de diretórios vazios

os.removedirs('templates/geek/university/dados')


# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora!

# importando a biblioteca send2trash
from send2trash import send2trash


os.remove('para-excluir1.txt') # Não vai para lixeira

send2trash('para-excluir2.txt') # Vai para lixeira. Pode ser restaurado

Se o arquivo não existir teremos OSError

send2trash('exclusao')  # Envia também diretório para lixeira

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryFile() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join('arquivo_temporario.txt'),'w') as arquivo:
        arquivo.write('Geek University \n')
    input()

# OBS: Não funciona no Windows


# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University \n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever em bits 'b'.

https://docs.python.org/pt-br/3/library/os.html
"""

import os
import tempfile

