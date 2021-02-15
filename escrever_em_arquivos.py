"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
# da mesma forma, se abrirmos um arquivo para escrita não podemos lê-lo, somente escrever.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Está função recebe uma string como parâmetro, caso contrário teremos um TypeError

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado em um novo será criado, dessa forma todo
o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'W' - write (escrita)

# Forma Pythônica
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados\n')
    arquivo.write('Outro podemos escrever quantas linhas quisermos.\n')
    arquivo.write('Mais esta é a última linhaaa.\n')

with open('geek.txt', 'w') as arquivo:
    arquivo.write('Lucas de Souza Queiroz \n' * 1000)    
"""
with open('frutas.txt','w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta.title() + '\n')
        else:
            break    