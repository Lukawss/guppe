"""
Sistema de Arquivos e Navegação

Para fazer uso de manioulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os

print(os.getcwd()) # -> Diretório de trabalho corrente, retorna o path

os.chdir('..') # -> Usado para mudar o diretório

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('C:\\users\\lucas'))

# Podemos identificar o sistema operacional

print(os.name)

print(os.getcwd())

res = os.path.join(os.getcwd(),'geek','university')

os. chdir(res)

print(os.getcwd())

# os.path.join(), recebe dois parâmetros, senod o primeiro o diretório atual e o segundo o
# o diret´rorio que será juntado ao atual


"""
import os

# Podemos listar os arquivos e diretórios com o listdir()

#print(os.listdir())

# Podemos listar os arquivos e diretórios com mais detalhes scandir()

scanner = os.scandir()

arquivos = list(scanner)

#print(arquivos)

#print(dir(arquivos[3].name))

print(arquivos[3].inode())
print(arquivos[3].is_dir())   # É um diretório?
print(arquivos[3].is_file())  # É um arquivo?
print(arquivos[3].is_symlink())  # É um link simbólico?
print(arquivos[3].name)  # Nome do arquivo
print(arquivos[3].path)  # Caminho até o arquivo
print(arquivos[3].stat()) # Estatísticas...

scanner.close()