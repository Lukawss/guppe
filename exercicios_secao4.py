with open('novo.txt', 'r') as arquivo, open('novo1.txt','a') as arquivo1:
    arquivo1.write('Teste')
    arquivo1.write('\n')
    for linha in arquivo.readlines():
        arquivo1.write(int(linha[1]))

